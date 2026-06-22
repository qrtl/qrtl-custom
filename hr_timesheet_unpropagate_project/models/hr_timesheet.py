# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _compute_project_id(self):
        # Avoid updating the project of existing timesheet records which are already
        # validated or not owned by the current user.
        self = self.filtered(
            lambda x: not x.validated and x.employee_id.user_id == self.env.user
        )
        return super()._compute_project_id()
