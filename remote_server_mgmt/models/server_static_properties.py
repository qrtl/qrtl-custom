# Copyright 2020-2025 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ServerStaticProperties(models.Model):
    _name = "server.static.properties"
    _description = "Server Static Properties"

    name = fields.Char("Property", required=True)
    remote_server_id = fields.Many2one("remote.server", "Server")
    property_value = fields.Text("Value", required=True)
