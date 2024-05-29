# Copyright 2024 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    license_type = fields.Selection(
        [("agpl-3", "AGPL-3"), ("lgpl-3", "LGPL-3"), ("other", "Other proprietary")],
        help="Select the type of license",
    )
    complexity = fields.Selection([("high", "High"), ("mid", "Mid"), ("low", "Low")])
    popularity_factor = fields.Float()
    loc = fields.Integer(string="Lines of Code")
    amount = fields.Float(compute="_compute_amount", store=True)
    amount_incl_mig = fields.Float(compute="_compute_amount", store=True)

    @api.depends("list_price", "popularity_factor", "loc")
    def _compute_amount(self):
        for product in self:
            product.amount = (
                product.list_price * product.loc * product.popularity_factor
            )
            product.amount_incl_mig = product.amount * 2
