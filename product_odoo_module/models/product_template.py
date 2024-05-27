# Copyright 2024 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_odoo_module = fields.Boolean()
    technical_name = fields.Char()
    license_type = fields.Selection(
        [("agpl-3", "AGPL-3"), ("lgpl-3", "LGPL-3"), ("other", "Other proprietary")],
        help="Select the type of license",
    )
