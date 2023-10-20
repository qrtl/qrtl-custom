# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import urllib

from odoo import api, models, fields


class BaseRemoteUrl(models.Model):
    _name = 'base.remote.url'

    name = fields.Char("Domain", required=True)
    base_remote_server_id = fields.Many2one('base.remote.server', 'Server')
    base_remote_database_id = fields.Many2one('base.remote.database', 'Database')
    valid = fields.Boolean('URL Valid', compute='_compute_valid')

    @api.multi
    def _compute_valid(self):
        for url in self:
            url.valid = False
            try:
                code = urllib.request.urlopen("http://%s" % url.name).getcode()
                if code == 200:
                    url.valid = True
            except Exception:
                pass
