# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl

from odoo import fields, models


class ServerServer(models.Model):
    _name = "server.server"
    _description = "Servers"

    name = fields.Char(string="Server Name", required=True)
    partner_id = fields.Many2one("res.partner", required=True)
    url = fields.Char(required=True)
    info = fields.Text(string="General Information")
    tags = fields.Many2many("server.tag")
    active = fields.Boolean(default=True)
