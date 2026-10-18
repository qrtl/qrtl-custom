# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductOdooVersion(models.Model):
    _name = "product.odoo.version"
    _description = "Odoo Version"
    _order = "name desc"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
