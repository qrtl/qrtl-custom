# Copyright 2023 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class AccountAnalyticGroup(models.Model):
    _name = "account.analytic.group"
    _description = "Analytic Account Group"
    _order = "sequence, name"

    sequence = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()
    company_id = fields.Many2one("res.company", string="Company")
