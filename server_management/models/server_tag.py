# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl

from odoo import fields, models


class ServeTag(models.Model):
    _name = "server.tag"
    _description = "Server Category"

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string="Color Index")
