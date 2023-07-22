# Copyright 2023 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    group_id = fields.Many2one(
        "account.analytic.group",
        related="account_id.group_id",
        store=True,
        readonly=True,
        compute_sudo=True,
    )
