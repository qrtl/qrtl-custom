# Copyright 2020-2025 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Remote Servers Management",
    "version": "16.0.1.0.0",
    "category": "Others",
    "author": "Quartile",
    "website": "https://www.quartile.co",
    "license": "LGPL-3",
    "external_dependencies": {"python": ["paramiko"]},
    "depends": ["mail"],
    "data": [
        "security/remote_server_mgmt_security.xml",
        "security/ir.model.access.csv",
        "views/remote_server_mgmt_menu.xml",
        "views/remote_server_tag_views.xml",
        "views/remote_server_views.xml",
    ],
    "installable": True,
}
