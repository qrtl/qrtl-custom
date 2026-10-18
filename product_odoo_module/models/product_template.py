# Copyright 2024-2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_odoo_module = fields.Boolean()
    odoo_version_id = fields.Many2one("product.odoo.version")
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
        for rec in self:
            rec.amount = rec.list_price * rec.loc * rec.popularity_factor
            rec.amount_incl_mig = rec.amount * 2
