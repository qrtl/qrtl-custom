# Copyright 2019-2020 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "follower_default_send_mail_false",
    "summary": """
        Sets the send_mail field to False by default
        when adding a new follower
    """,
    "author": "Quartile Limited, " "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Uncategorized",
    "version": "12.0.0.0.1",
    "depends": ["base", "mail"],
    "data": ["views/views.xml", "views/templates.xml"],
}
