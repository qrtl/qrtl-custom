# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    group_id = fields.Many2one(
        'account.analytic.group',
        related='account_id.group_id',
        store=True,
        readonly=True,
        compute_sudo=True,
    )
