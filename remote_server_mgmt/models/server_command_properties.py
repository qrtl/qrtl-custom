# Copyright 2020-2025 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

import paramiko

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ServerCommandProperties(models.Model):
    _name = "server.command.properties"
    _description = "Server Command Properties"

    name = fields.Char("Property", required=True)
    remote_server_id = fields.Many2one("remote.server", "Server")
    command = fields.Char(required=True)
    property_value = fields.Text("Value", compute="_compute_property_value", store=True)

    @api.depends("command")
    def _compute_property_value(self):
        for prop in self:
            if prop.command and prop.remote_server_id:
                ssh = paramiko.SSHClient()
                try:
                    key = paramiko.RSAKey.from_private_key_file(
                        prop.remote_server_id.private_key_path
                    )
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(
                        prop.remote_server_id.server_ip,
                        port=prop.remote_server_id.ssh_port,
                        username=prop.remote_server_id.ssh_user,
                        pkey=key,
                    )
                    _stdin, stdout, _stderr = ssh.exec_command(prop.command)
                    prop.property_value = stdout.read().decode("ascii").strip("\n")
                except (paramiko.SSHException, FileNotFoundError) as e:
                    raise UserError(_("An error occurred: {}".format(e))) from e
                finally:
                    ssh.close()
