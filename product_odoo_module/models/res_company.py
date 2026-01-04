# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    module_fee_formula = fields.Text(
        help="Python expression to compute suggested monthly fee. "
        "Available variables: base_price, source_type_code, customer_count, "
        "license_name, loc, standard_rate. "
        "Example: base_price * (0.8 if source_type_code == 'oca' else 1.0)",
    )
    module_standard_rate = fields.Monetary(
        string="Standard Rate per 100 LOC",
        help="Standard price per 100 lines of code for module fee calculation.",
    )
