# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class ProjectTask(models.Model):
    _inherit = "project.task"

    def _get_timesheet(self):
        if self._context.get("task_write"):
            # To avoid updating the project of existing timesheet records.
            return self.env["account.analytic.line"]
        return super()._get_timesheet()

    def write(self, values):
        self = self.with_context(task_write=True)
        return super().write(values)
