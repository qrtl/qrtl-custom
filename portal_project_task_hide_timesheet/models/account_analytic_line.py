# Copyright 2019 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _show_portal_timesheets(self):
        # Hide timesheet information from the portal task page and list. This
        # is the core hook driving the "show_portal_timesheets" template
        # variable; the report controller is gated on it as well so the
        # timesheet report cannot be downloaded via ?report_type=.
        return False
