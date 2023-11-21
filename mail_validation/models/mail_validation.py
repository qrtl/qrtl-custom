# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MailValidation(models.Model):
    _name = "mail.validation"
    _description = "Mail Validation"

    name = fields.Char(required=True)
    model = fields.Selection(selection="_list_all_models", required=True)
    validation_type = fields.Selection(
        selection=[
            ("by_domain", "By domain"),
            ("by_py_code", "By python code"),
        ],
        required=True,
        default="by_py_code",
        help="By python code: allow to define any arbitrary check\n"
        "By domain: limited to a selection by an odoo domain",
    )
    domain = fields.Char()
    code = fields.Text(
        "Python Code",
        help="Python code executed to check the mail validation "
        "Use block = True to block the sending mail",
    )

    @api.model
    def _list_all_models(self):
        return self.env["ir.filters"]._list_all_models()
