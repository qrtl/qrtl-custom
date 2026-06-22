# Copyright 2024 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields
from odoo.tests.common import TransactionCase


class TestAccountAnalyticGroup(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = cls.env["account.analytic.group"].create({"name": "Group A"})
        cls.plan = cls.env["account.analytic.plan"].create({"name": "Test Plan"})
        cls.account = cls.env["account.analytic.account"].create(
            {
                "name": "Test Account",
                "plan_id": cls.plan.id,
                "group_id": cls.group.id,
            }
        )

    def test_line_group_id_follows_account(self):
        # account.analytic.line.group_id is a stored related field on
        # account_id.group_id; it must be set on creation and recomputed
        # when the account's group changes.
        line = self.env["account.analytic.line"].create(
            {
                "name": "Test Line",
                "account_id": self.account.id,
                "amount": 100.0,
                "date": fields.Date.today(),
            }
        )
        self.assertEqual(line.group_id, self.group)
        new_group = self.env["account.analytic.group"].create({"name": "Group B"})
        self.account.group_id = new_group
        self.assertEqual(line.group_id, new_group)
