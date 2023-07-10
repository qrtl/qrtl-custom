# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountAnalyticGroup(models.Model):
    _name = "account.analytic.group"
    _description = "Analytic Categories"

    sequence = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()
    parent_path = fields.Char(index=True)
    company_id = fields.Many2one("res.company", string="Company")
