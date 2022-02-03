# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.constrains("task_id", "project_id")
    def _check_task_project(self):
        """Overriding the standard method."""
        pass
