# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProtectedAttachment(models.Model):
    _name = "protected.attachment"
    _description = "Protected Attachment"

    object_id = fields.Many2one(
        comodel_name="mail.thread",
        ondelete="cascade",
        required=True,
        copy=False,
    )
    attachment = fields.Binary(string="File", required=True)
    attachment_name = fields.Char(string="File Name", readonly=True)
