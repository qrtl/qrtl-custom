# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models


class ProjectTask(models.AbstractModel):
    _name = "project.task"
    _inherit = ["project.task", "additional.info"]
