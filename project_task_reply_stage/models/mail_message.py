# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model
    def create(self, vals):
        res = super(MailMessage, self).create(vals)
        if (
            res.model == "project.task"
            and res.subtype_id
            and not res.subtype_id.internal
        ):
            task = self.env["project.task"].browse(res.res_id)
            if (
                task.state != "draft"
                and res.author_id.user_ids
                and not res.author_id.user_ids[0].has_group("base.group_user")
            ):
                if task.project_id and task.project_id.customer_reply_stage_id:
                    task.sudo().write(
                        {"stage_id": task.project_id.customer_reply_stage_id.id}
                    )
                else:
                    reply_stage = self.env["project.task.type"].browse(
                        int(
                            self.env["ir.config_parameter"]
                            .sudo()
                            .get_param(
                                "project_task_reply_stage.customer_reply_stage_id"
                            )
                        )
                    )
                    if task.project_id in reply_stage.project_ids:
                        task.sudo().write({"stage_id": reply_stage.id})
        return res
