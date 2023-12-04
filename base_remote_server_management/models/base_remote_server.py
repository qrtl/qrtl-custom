# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class BaseRemoteServer(models.Model):
    _name = "base.remote.server"

    name = fields.Char("Description/Usage", required=True)
    server_ip = fields.Char("IP", required=True)
    ssh_user = fields.Char("SSH User", required=True)
    ssh_port = fields.Integer("SSH Port Number", required=True)
    private_key_path = fields.Char(required=True)
    active = fields.Boolean(default=True)
    server_command_properties_ids = fields.One2many(
        "server.command.properties",
        "base_remote_server_id",
        string="Command Properties",
    )
    server_static_properties_ids = fields.One2many(
        "server.static.properties", "base_remote_server_id", string="Static Properties"
    )
    server_url_ids = fields.One2many(
        "base.remote.url", "base_remote_server_id", string="Access URL(s)"
    )
    database_ids = fields.One2many(
        "base.remote.database", "base_remote_server_id", string="Odoo Database(s)"
    )
    partner_id = fields.Many2one("res.partner", required=True)
    remark = fields.Text()

    def sync_command_properties(self):
        for prop in self.server_command_properties_ids:
            prop._compute_property_value()
