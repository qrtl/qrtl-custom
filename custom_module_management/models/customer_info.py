# Copyright 2024 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class CustomerInfo(models.Model):
    _name = "custom.module.customerinfo"

    partner_id = fields.Many2one("res.partner", required=True)
    product_id = fields.Many2one(
        "product.product",
        ondelete="cascade",
        required=True,
        domain=[("is_odoo_module", "=", True)],
    )
    repo = fields.Char(string="Repository")
    amount = fields.Float(related="product_id.amount", store=True)
    amount_incl_mig = fields.Float(related="product_id.amount_incl_mig", store=True)
