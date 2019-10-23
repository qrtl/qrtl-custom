# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class HelpdeskTeam(models.Model):
    _inherit = 'helpdesk.team'

    customer_reply_stage_id = fields.Many2one(
        'helpdesk.stage',
        string='Customer\'s Update Stage',
    )
