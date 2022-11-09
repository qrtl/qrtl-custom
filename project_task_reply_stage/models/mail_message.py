# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model_create_multi
    def create(self, values_list):
        messages = super(MailMessage, self).create(values_list)
        for message in messages:
            if not (
                message.model == "project.task"
                and message.subtype_id
                and not message.subtype_id.internal
            ):
                continue
            task = self.env["project.task"].browse(message.res_id)
            if task.state == "draft":
                continue
            user = message.author_id.user_ids[:1]
            if user and user.has_group("base.group_user"):
                continue
            reply_stage = task.project_id.customer_reply_stage_id
            if reply_stage:
                task.sudo().write({"stage_id": reply_stage.id})
                continue
            reply_stage_id = int(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("project_task_reply_stage.customer_reply_stage_id")
            )
            if reply_stage_id in task.project_id.type_ids.ids:
                task.sudo().write({"stage_id": reply_stage_id})
        return messages
