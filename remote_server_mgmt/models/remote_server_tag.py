# Copyright 2020-2025 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from random import randint

from odoo import fields, models


class RemoteServerTag(models.Model):
    _name = "remote.server.tag"
    _description = "Remote Server Tag"
    _order = "sequence, id"

    def _default_color(self):
        return randint(1, 11)

    name = fields.Char("Name", required=True, translate=True)
    sequence = fields.Integer("Sequence", default=0)
    color = fields.Integer("Color Index", default=lambda self: self._default_color())
