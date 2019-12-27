# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Auto-update Replied Task's Stage",
    "category": "Project",
    "version": "12.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co/",
    "licence": "AGPL-3",
    "depends": ["project", "project_stage_state"],
    "description": """
This module adds 'Customer's Update Stage' to project and general settings.
When non-internal user send an update to the task, the stage will be update
automatically.
    """,
    "data": ["views/project_project_views.xml", "views/res_config_settings_views.xml"],
    "installable": True,
}
