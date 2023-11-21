# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    ignore_mail_validation = fields.Boolean()

    def _check_mail_validation_by_py_code(self, validation_record):
        expr = validation_record.code
        space = {"self": self}
        try:
            safe_eval(
                expr, space, mode="exec", nocopy=True
            )  # nocopy allows to return 'result'
        except Exception as e:
            _logger.exception(e)
            raise UserError(
                _(
                    "Error when evaluating the mail.validation"
                    " validation:\n %(name)s \n(%(error)s)"
                )
                % {"name": validation_record.name, "error": e}
            ) from e
        return space.get("block", False)

    def _check_mail_validation_by_domain(self, validation_record):
        domain = validation_record.domain
        if self.sudo().filtered_domain(safe_eval(domain)):
            return True
        else:
            return False

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, **kwargs):
        if not self.ignore_mail_validation:
            # Check if there's a domain set for this model in the mail.validation model
            mail_validation = (
                self.env["mail.validation"].sudo().search([("model", "=", self._name)])
            )
            if mail_validation:
                for validation in mail_validation:
                    if validation.validation_type == "by_py_code":
                        is_matched_record = self._check_mail_validation_by_py_code(
                            validation
                        )
                    else:
                        is_matched_record = self._check_mail_validation_by_domain(
                            validation
                        )
                    # If the current record is not part of the matching records, don't validate
                    if is_matched_record:
                        raise ValidationError(
                            _("Mail Validation block to send email for this record.")
                        )
        return super().message_post(**kwargs)
