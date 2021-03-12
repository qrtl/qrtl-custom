# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AdditionalInfo(models.AbstractModel):
    _name = "additional.info"
    _description = "Additional Info"

    additional_info_ids = fields.Many2many(
        comodel_name='additional.info.line')
