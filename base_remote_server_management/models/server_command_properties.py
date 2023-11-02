# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import paramiko

from odoo import api, fields, models


class ServerCommandProperties(models.Model):
    _name = "server.command.properties"

    name = fields.Char("Property", required=True)
    base_remote_server_id = fields.Many2one("base.remote.server", "Server")
    command = fields.Char("Command", required=True)
    property_value = fields.Text("Value", compute="_compute_property_value", store=True)

    @api.multi
    @api.depends("command")
    def _compute_property_value(self):
        for prop in self:
            if prop.command:
                ssh = paramiko.SSHClient()
                key = paramiko.RSAKey.from_private_key_file(
                    prop.base_remote_server_id.private_key_path
                )
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(
                    prop.base_remote_server_id.server_ip,
                    port=prop.base_remote_server_id.ssh_port,
                    username=prop.base_remote_server_id.ssh_user,
                    pkey=key,
                )
                _stdin, stdout, _stderr = ssh.exec_command(prop.command)
                prop.property_value = stdout.read().decode("ascii").strip("\n")
                ssh.close()
