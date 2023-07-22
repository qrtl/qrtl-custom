# Copyright 2023 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Account Analytic Group",
    "category": "Analytic",
    "license": "LGPL-3",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "version": "16.0.1.0.0",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/analytic_group_views.xml",
        "views/analytic_account_views.xml",
    ],
    "installable": True,
}
