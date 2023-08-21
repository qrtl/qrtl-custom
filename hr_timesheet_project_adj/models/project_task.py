# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, models
from odoo.exceptions import UserError


class ProjectTask(models.Model):
    _inherit = "project.task"

    def _get_timesheet(self):
        if self._context.get("task_write"):
            # To avoid updating the project of existing timesheet records.
            return self.env["account.analytic.line"]
        return super(ProjectTask, self)._get_timesheet()

    def write(self, values):
        if (
            "project_id" in values
            and not values.get("project_id")
            and self._get_timesheet()
        ):
            raise UserError(
                _(
                    "This task must be part of a project because"
                    "there are some timesheets linked to it."
                )
            )
        self = self.with_context(task_write=True)
        return super().write(values)
