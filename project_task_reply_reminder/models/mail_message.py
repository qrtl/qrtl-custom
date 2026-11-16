# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model_create_multi
    def create(self, values_list):
        messages = super().create(values_list)
        for message in messages.filtered(
            lambda m: m.model == "project.task"
            and m.subtype_id
            and not m.subtype_id.internal
        ):
            task = self.env["project.task"].sudo().browse(message.res_id)
            user = message.author_id.user_ids[:1]
            if not (user and user.has_group("base.group_user")):
                task._mark_customer_reply_pending()
            # Stage-change tracking also uses a public subtype; it is not a reply.
            elif message.message_type in ("comment", "email"):
                task._clear_customer_reply()
        return messages
