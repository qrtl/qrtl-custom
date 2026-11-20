# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model_create_multi
    def create(self, values_list):
        messages = super().create(values_list)
        # Tracking notifications use public subtypes too, and those authored by
        # OdooBot have no active user, so only real messages count.
        for message in messages.filtered(
            lambda m: m.model == "project.task"
            and m.message_type in ("comment", "email")
            and m.subtype_id
            and not m.subtype_id.internal
        ):
            task = self.env["project.task"].sudo().browse(message.res_id)
            user = message.author_id.user_ids[:1]
            if user and user.has_group("base.group_user"):
                task._clear_customer_reply()
            else:
                task._mark_customer_reply_pending()
        return messages
