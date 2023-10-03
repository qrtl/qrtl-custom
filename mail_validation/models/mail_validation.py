# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MailValidation(models.Model):
    _name = "mail.validation"
    _description = "Mail Validation"

    _sql_constraints = [
        ("model_unique", "UNIQUE(model_id)", "The model can only be added once!")
    ]

    model_id = fields.Selection(
        selection="_list_all_models", string="Model", required=True
    )
    domain = fields.Text(
        default="[]",
        required=True,
        help="""Enter a domain expression for mail validation.
        Example: [('partner_id', '!=', self.project_id.commercial_partner_id.id)]""",
    )

    @api.model
    def _list_all_models(self):
        return self.env["ir.filters"]._list_all_models()
