# Copyright 2020-2025 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

import logging
from urllib.request import urlopen

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class RemoteUrl(models.Model):
    _name = "remote.url"
    _description = "Remote URL"

    name = fields.Char("Domain", required=True)
    remote_server_id = fields.Many2one("remote.server", "Server")
    remote_database_id = fields.Many2one("remote.database", "Database")
    valid = fields.Boolean("URL Valid", compute="_compute_valid")

    @api.depends("name")
    def _compute_valid(self):
        for url in self:
            url.valid = False
            if not url.name:
                continue
            try:
                response = urlopen(f"http://{url.name}", timeout=10)
                # Assuming that we want to store any 2xx status as a valid URL
                url.valid = 200 <= response.getcode() < 300
            except Exception as e:
                _logger.error(
                    "An error occurred while validating URL '{}': {}".format(
                        url.name, e
                    )
                )
