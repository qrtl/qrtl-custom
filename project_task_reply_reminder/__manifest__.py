# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Project Task Reply Reminder",
    "summary": "Remind the assignee of customer messages left without a reply",
    "category": "Project",
    "version": "16.0.1.0.0",
    "author": "Quartile",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": ["project_task_reply_stage"],
    "data": [
        "data/ir_config_parameter_data.xml",
        "data/mail_activity_type_data.xml",
        "data/ir_cron_data.xml",
    ],
    "maintainers": ["yostashiro", "aungkokolin1997"],
    "installable": True,
}
