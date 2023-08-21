# Copyright 2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.depends("task_id", "task_id.project_id")
    def _compute_project_id(self):
        # QRTL EDIT
        # Remove auto assign when project_id of task is changed
        # for line in self:
        # if not line.task_id.project_id or line.project_id == line.task_id.project_id:
        #     continue
        # line.project_id = line.task_id.project_id
        pass

    @api.onchange("task_id")
    def _onchange_task_id(self):
        self.project_id = self.task_id.project_id
