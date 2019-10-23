# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class MailMessage(models.Model):
    _inherit = 'mail.message'

    @api.model
    def create(self, vals):
        res = super(MailMessage, self).create(vals)
        if res.model == 'helpdesk.ticket' and res.subtype_id and \
                not res.subtype_id.internal:
            ticket = self.env['helpdesk.ticket'].browse(res.res_id)
            if ticket.team_id and ticket.stage_id.sequence != 0:
                team_members = ticket.team_id.member_ids.mapped('partner_id')
                if res.author_id not in team_members and \
                        ticket.team_id.customer_reply_stage_id:
                    ticket.stage_id = \
                        ticket.team_id.customer_reply_stage_id
        return res
