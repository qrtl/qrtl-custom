# Copyright 2024-2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Product Odoo Module",
    "version": "16.0.1.0.0",
    "category": "Product",
    "author": "Quartile",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": ["product"],
    "data": [
        "data/menuitem_data.xml",
        "security/ir.model.access.csv",
        "views/product_odoo_version_views.xml",
        "views/product_template_views.xml",
        "views/res_company_views.xml",
    ],
}
