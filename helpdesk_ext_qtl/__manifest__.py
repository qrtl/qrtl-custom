# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Extension for Helpdesk functions',
    'category': 'Helpdesk',
    'version': '12.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.quartile.co/',
    'licence': 'AGPL-3',
    'depends': [
        'helpdesk'
    ],
    'summary':"""""",
    'description': """
This module adds the following features to the Helpdesk function:
- Add deadline field to the ticket.
- Add settings to enable the automated update in ticket's state when there 
is a reply from customer.
    """,
    'data': [
        'views/helpdesk_team_views.xml',
        'views/helpdesk_ticket_views.xml',
    ],
    'installable': True,
}
