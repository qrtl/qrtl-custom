# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ModuleBusinessImpact(models.Model):
    _name = "module.business.impact"
    _description = "Module Business Impact"
    _order = "sequence, name"

    name = fields.Char(required=True)
    description = fields.Char()
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
