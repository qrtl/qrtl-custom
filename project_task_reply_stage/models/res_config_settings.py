# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    customer_reply_stage_id = fields.Many2one(
        "project.task.type", string="Customer's Update Stage"
    )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env["ir.config_parameter"].sudo().get_param
        res.update(
            customer_reply_stage_id=int(
                get_param(
                    "project_task_reply_stage.customer_reply_stage_id", default=False
                )
            )
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "project_task_reply_stage.customer_reply_stage_id",
            self.customer_reply_stage_id.id,
        )
