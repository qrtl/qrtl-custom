# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Invite(models.TransientModel):
    _inherit = "mail.wizard.invite"

    send_mail = fields.Boolean(
        default=False,
        help="If checked, the partners will receive an \
            email warning they have been added in the document's followers.",
    )
