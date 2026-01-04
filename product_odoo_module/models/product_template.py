# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_odoo_module = fields.Boolean(
        default=False,
        help="Enable this for products that represent maintained Odoo modules. "
        "Module products are typically Service products (no stock).",
    )
    source_type_id = fields.Many2one("module.source.type", string="Source Type")
    module_technical_name = fields.Char(string="Technical Name")
    module_repo_url = fields.Char(string="Repository URL")
    module_notes = fields.Text(string="Notes")
    business_impact_id = fields.Many2one("module.business.impact")
    module_license_id = fields.Many2one("module.license", string="License")
    module_complexity_id = fields.Many2one(
        "module.complexity",
        string="Complexity",
    )
    customer_module_count = fields.Integer(compute="_compute_customer_module_count")

    @api.depends("product_variant_ids")
    def _compute_customer_module_count(self):
        counts = {}
        if self.ids:
            data = self.env["customer.module.info"].read_group(
                [("product_tmpl_id", "in", self.ids), ("active", "=", True)],
                ["product_tmpl_id"],
                ["product_tmpl_id"],
            )
            counts = {
                item["product_tmpl_id"][0]: item["product_tmpl_id_count"]
                for item in data
            }
        for record in self:
            record.customer_module_count = counts.get(record.id, 0)

    def action_view_customer_modules(self):
        self.ensure_one()
        action = self.env.ref("product_odoo_module.action_customer_module").read()[0]
        action["domain"] = [("product_tmpl_id", "=", self.id)]
        action["context"] = dict(
            self.env.context,
            default_product_tmpl_id=self.id,
            search_default_active=1,
        )
        return action
