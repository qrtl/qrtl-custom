# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project task additional info",
    "version": "12.0.1.0.0",
    "author": 'QUARTILE LIMITED,'
              'Odoo Community Association (OCA)',
    "website": 'https://www.quartile.co/',
    "category": "Usability",
    "license": "AGPL-3",
    "depends": [
        "base_additional_info",
        "project",
    ],
    "data": [
        "security/ir.model.access.csv",
        
        'views/project_task_view.xml',
    ],
    'installable': True,
}
