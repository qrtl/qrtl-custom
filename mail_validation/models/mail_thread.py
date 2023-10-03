# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    ignore_mail_validation = fields.Boolean()

    def get_evaluated_domain(self, domain_str):
        # Define a limited local context where only 'self' is accessible
        local_context = {"self": self}

        # Use eval to evaluate the domain within this context
        # pylint: disable=eval-used,eval-referenced
        domain = eval(domain_str, {}, local_context)
        return domain

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, **kwargs):
        if not self.ignore_mail_validation:
            # Check if there's a domain set for this model in the mail.validation model
            mail_validation = (
                self.env["mail.validation"]
                .sudo()
                .search([("model_id", "=", self._name)], limit=1)
            )
            if mail_validation:
                domain = self.get_evaluated_domain(mail_validation.domain)
                matching_records = self.search(domain)
                # If the current record is not part of the matching records, don't validate
                if self in matching_records:
                    raise ValidationError(
                        _("Mail Validation block to send email for this record.")
                    )
        return super().message_post(**kwargs)
