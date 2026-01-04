# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_module_count = fields.Integer(compute="_compute_customer_module_count")

    @api.depends("child_ids")
    def _compute_customer_module_count(self):
        counts = {}
        if self.ids:
            data = self.env["customer.module.info"].read_group(
                [("partner_id", "in", self.ids), ("active", "=", True)],
                ["partner_id"],
                ["partner_id"],
            )
            counts = {item["partner_id"][0]: item["partner_id_count"] for item in data}
        for partner in self:
            partner.customer_module_count = counts.get(partner.id, 0)

    def action_view_customer_modules(self):
        self.ensure_one()
        action = self.env.ref("product_odoo_module.action_customer_module").read()[0]
        action["domain"] = [("partner_id", "=", self.id)]
        action["context"] = dict(
            self.env.context,
            default_partner_id=self.id,
            search_default_active=1,
        )
        return action
