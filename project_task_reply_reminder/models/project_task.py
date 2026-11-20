# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from datetime import timedelta

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    customer_reply_pending_since = fields.Datetime(readonly=True, copy=False)
    customer_reply_due = fields.Datetime(readonly=True, copy=False)
    customer_reply_reminded = fields.Boolean(readonly=True, copy=False)

    def write(self, vals):
        res = super().write(vals)
        if "stage_id" in vals:
            self.filtered(
                lambda t: t.customer_reply_pending_since
                and t.stage_id != t._get_customer_reply_stage()
            )._clear_customer_reply()
        return res

    def _get_customer_reply_stage(self):
        self.ensure_one()
        if self.project_id.customer_reply_stage_id:
            return self.project_id.customer_reply_stage_id
        stage_id = int(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("project_task_reply_stage.customer_reply_stage_id", 0)
        )
        return self.project_id.type_ids.filtered(lambda s: s.id == stage_id)

    def _mark_customer_reply_pending(self):
        hours = float(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("project_task_reply_reminder.hours", 8)
        )
        now = fields.Datetime.now()
        # A follow-up while already pending keeps the original due time.
        for task in self.filtered(
            lambda t: not t.customer_reply_pending_since
            and t.stage_id == t._get_customer_reply_stage()
        ):
            calendar = task.company_id.resource_calendar_id
            due = calendar and calendar.plan_hours(hours, now, compute_leaves=True)
            task.write(
                {
                    "customer_reply_pending_since": now,
                    "customer_reply_due": due or now + timedelta(hours=hours),
                }
            )

    def _clear_customer_reply(self):
        tasks = self.filtered("customer_reply_pending_since")
        tasks.activity_feedback(
            ["project_task_reply_reminder.mail_activity_type_customer_reply"]
        )
        tasks.write(
            {
                "customer_reply_pending_since": False,
                "customer_reply_due": False,
                "customer_reply_reminded": False,
            }
        )

    @api.model
    def _cron_remind_customer_reply(self):
        tasks = self.search(
            [
                ("customer_reply_due", "<=", fields.Datetime.now()),
                ("customer_reply_reminded", "=", False),
            ]
        )
        for task in tasks:
            user = task.user_ids[:1] or task.project_id.user_id
            if user:
                task.activity_schedule(
                    "project_task_reply_reminder.mail_activity_type_customer_reply",
                    user_id=user.id,
                )
        tasks.customer_reply_reminded = True
