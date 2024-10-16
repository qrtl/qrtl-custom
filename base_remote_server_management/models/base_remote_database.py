# Copyright 2020 Quartile
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class BaseRemoteDatabase(models.Model):
    _name = "base.remote.database"

    name = fields.Char("Database Name", required=True)
    base_remote_server_id = fields.Many2one("base.remote.server", "Server")
    server_url_ids = fields.One2many(
        "base.remote.url", "base_remote_database_id", string="URL(s)"
    )
