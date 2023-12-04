# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import logging
from urllib.request import urlopen

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class BaseRemoteUrl(models.Model):
    _name = "base.remote.url"

    name = fields.Char("Domain", required=True)
    base_remote_server_id = fields.Many2one("base.remote.server", "Server")
    base_remote_database_id = fields.Many2one("base.remote.database", "Database")
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
