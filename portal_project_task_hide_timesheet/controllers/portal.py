# Copyright 2019 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.exceptions import MissingError
from odoo.http import request

from odoo.addons.hr_timesheet.controllers.portal import (
    TimesheetProjectCustomerPortal,
)


class TimesheetProjectCustomerPortal(TimesheetProjectCustomerPortal):
    def _show_task_report(self, task_sudo, report_type, download):
        # The /my/tasks/<id>?report_type= route only renders the timesheet
        # report. When timesheets are hidden from the portal, block it so the
        # data is not reachable through the download URL.
        if not request.env["account.analytic.line"]._show_portal_timesheets():
            raise MissingError(request.env._("There is nothing to report."))
        return super()._show_task_report(task_sudo, report_type, download)
