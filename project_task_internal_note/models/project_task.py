# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    internal_note = fields.Text("Internal Note", help="e.g. problem, solution/proposal, test point, answere point, Unclear and each estimate step/time.")

