# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AdditionalInfoLine(models.Model):
    _name = "additional.info.line"
    _description = "Additional info line"
    _rec_name = "url"

    url = fields.Char("URL")
    remark = fields.Text("Remarks")
    sequence = fields.Integer(index=True, default=1)
