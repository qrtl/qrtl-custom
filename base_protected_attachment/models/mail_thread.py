# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    protected_attachment_ids = fields.One2many(
        comodel_name="protected.attachment",
        inverse_name="object_id",
        string="Protected Attachments",
    )
