# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    ticket_deadline = fields.Date(string="Deadline", copy=False)
