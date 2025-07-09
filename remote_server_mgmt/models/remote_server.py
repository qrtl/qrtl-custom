# Copyright 2020-2025 Quartile
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class RemoteServer(models.Model):
    _name = "remote.server"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Remote Server"

    name = fields.Char("Description/Usage", required=True)
    partner_id = fields.Many2one("res.partner")
    server_ip = fields.Char("IP")
    ssh_user = fields.Char("SSH User")
    ssh_port = fields.Integer("SSH Port")
    private_key_path = fields.Char()
    active = fields.Boolean(default=True)
    server_command_properties_ids = fields.One2many(
        "server.command.properties",
        "remote_server_id",
        string="Command Properties",
    )
    server_static_properties_ids = fields.One2many(
        "server.static.properties", "remote_server_id", string="Static Properties"
    )
    server_url_ids = fields.One2many(
        "remote.url", "remote_server_id", string="Access URL(s)"
    )
    database_ids = fields.One2many(
        "remote.database", "remote_server_id", string="Odoo Database(s)"
    )
    odoo_version = fields.Char(required=True)
    # managed_by_qrtl = fields.Boolean(default=True)
    tag_ids = fields.Many2many("remote.server.tag", string="Tags")
    service_provider = fields.Char()
    storage_size = fields.Integer("Storage(GB)")
    vcore = fields.Float("vCore")
    ram_size = fields.Integer("RAM(GB)")
    tsl_provider = fields.Char("TSL Provider")
    web_server = fields.Char()
    os = fields.Char("OS")
    backup_location = fields.Char()
    remark = fields.Text()

    def action_read_remote_server(self):
        self.ensure_one()
        return {
            "name": self.display_name,
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "remote.server",
            "res_id": self.id,
        }

    def sync_command_properties(self):
        for prop in self.server_command_properties_ids:
            prop._compute_property_value()
