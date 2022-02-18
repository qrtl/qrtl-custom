# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProjectTask(models.Model):
    """Added Internal Note in the Project Task."""

    _inherit = 'project.task'

    internal_note = fields.Text("Internal Notes", help="Do you need some help?")
    not_understand = fields.Text("Not understand", help="What we plan to check or investigate, or trouble with")
    
    estimate_step_time = fields.Text("Estimated steps and man-hours", help="This is a helpful message.")
    problem = fields.Text("Problem", help="What's the problem?")
    solution = fields.Text("Solution", help="What needs to be done to solve the problem?")
    test_point = fields.Text("Needs to be tested", help="What's need to fill before to approve")
    answere_point = fields.Text("Points to be answered", help="What do we need to tell them?")

