# Copyright 2024 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    customer_infos = fields.One2many("custom.module.customerinfo", "product_id")
