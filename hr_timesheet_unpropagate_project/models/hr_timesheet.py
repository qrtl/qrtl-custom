# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _compute_project_id(self):
        model = self._context.get("params", {}).get("model")
        if model and model == "project.task":
            # Avoid updating the project of existing timesheet records when project
            # assignment is changed in the task.
            return
        super()._compute_project_id()
