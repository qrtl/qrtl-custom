# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    customer_reply_stage_id = fields.Many2one(
        "project.task.type",
        string="Customer's Update Stage",
        help="Stage that will be applied to the task when non-internal users "
        "reply to the task.",
    )
