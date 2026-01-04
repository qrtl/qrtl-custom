from datetime import date

from odoo.exceptions import ValidationError
from odoo.tests import common


class TestCustomerModule(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.partner = self.env["res.partner"].create({"name": "Test Partner"})
        self.product_template = self.env["product.template"].create(
            {
                "name": "Module A",
                "detailed_type": "service",
            }
        )
        self.product_variant = self.product_template.product_variant_id

    def test_overlap_constraint(self):
        model = self.env["customer.module.info"]
        model.create(
            {
                "partner_id": self.partner.id,
                "product_id": self.product_variant.id,
                "monthly_fee": 100.0,
                "date_start": date(2026, 1, 1),
                "date_end": date(2026, 6, 30),
            }
        )
        with self.assertRaises(ValidationError):
            model.create(
                {
                    "partner_id": self.partner.id,
                    "product_id": self.product_variant.id,
                    "monthly_fee": 120.0,
                    "date_start": date(2026, 6, 1),
                    "date_end": date(2026, 12, 31),
                }
            )
        model.create(
            {
                "partner_id": self.partner.id,
                "product_id": self.product_variant.id,
                "monthly_fee": 120.0,
                "date_start": date(2026, 7, 1),
                "date_end": date(2026, 12, 31),
            }
        )
