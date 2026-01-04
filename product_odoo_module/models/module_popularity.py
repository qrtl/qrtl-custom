# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ModulePopularity(models.Model):
    _name = "module.popularity"
    _description = "Module Popularity"
    _order = "sequence, id"

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(default=10)
    factor = fields.Float(default=1.0, help="Multiplier for fee calculation.")
    active = fields.Boolean(default=True)
