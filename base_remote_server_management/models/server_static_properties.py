# Copyright 2020 Quartile
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ServerStaticProperties(models.Model):
    _name = "server.static.properties"

    name = fields.Char("Property", required=True)
    base_remote_server_id = fields.Many2one("base.remote.server", "Server")
    property_value = fields.Text("Value", required=True)
