# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model_create_multi
    def create(self, values_list):
        messages = super(MailMessage, self).create(values_list)
        for message in messages:
            if not (
                message.model == "helpdesk.ticket"
                and message.subtype_id
                and not message.subtype_id.internal
            ):
                continue
            ticket = self.env["helpdesk.ticket"].browse(message.res_id)
            if not (ticket.team_id and ticket.stage_id.sequence != 0):
                continue
            team_members = ticket.team_id.member_ids.mapped("partner_id")
            if (
                message.author_id not in team_members
                and ticket.team_id.customer_reply_stage_id
            ):
                ticket.stage_id = ticket.team_id.customer_reply_stage_id
        return messages
