# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from datetime import timedelta

from freezegun import freeze_time

from odoo import Command
from odoo.tests.common import TransactionCase, new_test_user


class TestProjectTaskReplyReminder(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.manager = new_test_user(
            cls.env, login="reply_pm", groups="project.group_project_manager"
        )
        cls.member = new_test_user(
            cls.env, login="reply_member", groups="project.group_project_user"
        )
        cls.customer = cls.env["res.partner"].create({"name": "Customer"})
        stage_vals = {"state": "open", "sequence": 1}
        cls.open_stage = cls.env["project.task.type"].create(
            dict(stage_vals, name="In Progress")
        )
        cls.reply_stage = cls.env["project.task.type"].create(
            dict(stage_vals, name="Need to Reply")
        )
        cls.project = cls.env["project.project"].create(
            {
                "name": "Client Project",
                "user_id": cls.manager.id,
                "type_ids": [Command.set((cls.open_stage | cls.reply_stage).ids)],
                "customer_reply_stage_id": cls.reply_stage.id,
            }
        )
        cls.task = cls.env["project.task"].create(
            {
                "name": "Task",
                "project_id": cls.project.id,
                "stage_id": cls.open_stage.id,
                "user_ids": False,
            }
        )
        cls.activity_type = cls.env.ref(
            "project_task_reply_reminder.mail_activity_type_customer_reply"
        )

    def _post(self, author, subtype_xmlid="mail.mt_comment", message_type="comment"):
        self.task.sudo().message_post(
            body="Message",
            author_id=author.id,
            message_type=message_type,
            subtype_xmlid=subtype_xmlid,
        )

    def _reminders(self):
        return self.task.activity_ids.filtered(
            lambda a: a.activity_type_id == self.activity_type
        )

    def _run_cron_after_due(self):
        with freeze_time(self.task.customer_reply_due + timedelta(minutes=1)):
            self.env["project.task"]._cron_remind_customer_reply()

    def test_follow_up_keeps_due(self):
        """A customer follow-up must not push the reminder further out."""
        with freeze_time("2026-11-17 08:00:00"):
            self._post(self.customer)
        self.assertEqual(self.task.stage_id, self.reply_stage)
        due = self.task.customer_reply_due
        self.assertTrue(due)
        with freeze_time("2026-11-17 11:00:00"):
            self._post(self.customer)
        self.assertEqual(self.task.customer_reply_due, due)

    def test_reminder_lifecycle(self):
        """Falls back to the PM, is not duplicated, and closes on a public reply."""
        self._post(self.customer)
        self._run_cron_after_due()
        self._run_cron_after_due()
        self.assertEqual(self._reminders().user_id, self.manager)
        self._post(self.member.partner_id, subtype_xmlid="mail.mt_note")
        self.assertTrue(self._reminders())
        self._post(self.member.partner_id)
        self.assertFalse(self._reminders())
        self.assertFalse(self.task.customer_reply_pending_since)

    def test_odoobot_notification_does_not_start_clock(self):
        """OdooBot has no active user, so its notifications must not pass for a customer."""
        self._post(
            self.env.ref("base.partner_root"),
            subtype_xmlid="project.mt_task_new",
            message_type="notification",
        )
        self.assertFalse(self.task.customer_reply_pending_since)

    def test_leave_reply_stage_clears(self):
        """Moving the task out of the reply stage stops the reminder."""
        self._post(self.customer)
        self.task.stage_id = self.open_stage
        self.assertFalse(self.task.customer_reply_due)
