# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


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
        "lst_price",
        "loc",
        "source_type_id",
        "product_tmpl_id.customer_module_count",
        "module_license_id",
        "module_complexity_id",
    )
    def _compute_suggested_fee(self):
        company = self.env.company
        formula = company.module_fee_formula
        standard_rate = company.module_standard_rate or 0.0
        for record in self:
            if not formula:
                record.suggested_fee = record.lst_price
                continue
            try:
                local_vars = {
                    "base_price": record.lst_price or 0.0,
                    "source_type_code": record.source_type_id.code or "",
                    "customer_count": record.product_tmpl_id.customer_module_count or 1,
                    "license_name": record.module_license_id.name or "",
                    "loc": record.loc or 0,
                    "standard_rate": standard_rate,
                    "complexity_factor": record.module_complexity_id.factor or 1.0,
                }
                record.suggested_fee = safe_eval(formula, local_vars)
            except Exception:
                record.suggested_fee = record.lst_price

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
