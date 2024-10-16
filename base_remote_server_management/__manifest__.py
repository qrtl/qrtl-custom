# Copyright 2020 Quartile
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Remote Servers Management",
    "summary": "Remote Servers Management",
    "version": "16.0.1.0.0",
    "category": "Others",
    "author": "Quartile",
    "website": "https://www.quartile.co",
    "license": "LGPL-3",
    "external_dependencies": {"python": ["paramiko"]},
    "depends": [
        "base",
    ],
    "data": [
        "views/base_remote_server_views.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
