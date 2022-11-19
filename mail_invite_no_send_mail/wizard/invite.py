# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Invite(models.TransientModel):
    _inherit = "mail.wizard.invite"

    send_mail = fields.Boolean(
        default=False,
    )
