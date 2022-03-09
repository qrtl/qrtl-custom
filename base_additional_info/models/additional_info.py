# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class AdditionalInfo(models.AbstractModel):
    _name = "additional.info"
    _description = "Additional Info"

    additional_info_ids = fields.Many2many(comodel_name="additional.info.line")
