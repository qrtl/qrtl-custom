# Copyright 2023 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Account Analytic Group",
    "summary": "Restore the Analytic Group feature removed from core in 16.0",
    "category": "Analytic",
    "license": "LGPL-3",
    "author": "Quartile",
    "website": "https://www.quartile.co",
    "maintainers": ["AungKoKoLin1997"],
    "version": "19.0.1.0.0",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/analytic_group_views.xml",
        "views/analytic_account_views.xml",
    ],
    "installable": True,
}
