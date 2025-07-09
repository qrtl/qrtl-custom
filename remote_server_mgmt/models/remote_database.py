# Copyright 2020-2025 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class RemoteDatabase(models.Model):
    _name = "remote.database"
    _description = "Remote Database"

    name = fields.Char("Database Name", required=True)
    remote_server_id = fields.Many2one("remote.server", "Server")
    server_url_ids = fields.One2many(
        "remote.url", "remote_database_id", string="URL(s)"
    )
