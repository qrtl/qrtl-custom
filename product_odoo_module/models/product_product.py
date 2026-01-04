# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    is_odoo_module = fields.Boolean(related="product_tmpl_id.is_odoo_module")
    source_type_id = fields.Many2one("module.source.type", string="Source Type")
    module_complexity_id = fields.Many2one("module.complexity", string="Complexity")
    module_license_id = fields.Many2one("module.license", string="License")
    loc = fields.Integer(string="Lines of Code")
    suggested_fee = fields.Float(
        compute="_compute_suggested_fee",
        help="Suggested monthly fee computed from company formula.",
    )

    @api.model_create_multi
    def create(self, vals_list):
        products = super().create(vals_list)
        for product in products:
            vals = {}
            if not product.source_type_id and product.product_tmpl_id.source_type_id:
                vals["source_type_id"] = product.product_tmpl_id.source_type_id.id
            if (
                not product.module_complexity_id
                and product.product_tmpl_id.module_complexity_id
            ):
                vals[
                    "module_complexity_id"
                ] = product.product_tmpl_id.module_complexity_id.id
            if (
                not product.module_license_id
                and product.product_tmpl_id.module_license_id
            ):
                vals["module_license_id"] = product.product_tmpl_id.module_license_id.id
            if vals:
                product.write(vals)
        return products

    @api.depends(
        "loc",
        "source_type_id",
        "module_license_id",
        "module_complexity_id",
        "module_popularity_id",
        "customer_module_count",
    )
    def _compute_suggested_fee(self):
        company = self.env.company
        standard_rate = company.module_standard_rate or 0.0
        for rec in self:
            source_type_factor = rec.source_type_id.factor or 1.0
            license_factor = rec.module_license_id.factor or 1.0
            complexity_factor = rec.module_complexity_id.factor or 1.0
            popularity_factor = rec.module_popularity_id.factor or 1.0
            customer_count = rec.customer_module_count or 1
            rec.suggested_fee = (
                100
                + rec.loc
                / 100
                * standard_rate
                * source_type_factor
                * complexity_factor
                * license_factor
                * popularity_factor
                / (customer_count * 0.7)
            )

    def action_view_customer_modules(self):
        self.ensure_one()
        action = self.env.ref("product_odoo_module.action_customer_module").read()[0]
        action["domain"] = [("product_tmpl_id", "=", self.product_tmpl_id.id)]
        action["context"] = dict(
            self.env.context,
            default_product_tmpl_id=self.product_tmpl_id.id,
            search_default_active=1,
        )
        return action
