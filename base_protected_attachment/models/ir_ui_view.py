# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from lxml import etree

from odoo import api, models


class Base(models.AbstractModel):
    _inherit = "base"

    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        result = super(Base, self).get_view(
            view_id=view_id, view_type=view_type, **options
        )
        if view_type == "form" and "protected_attachment_ids" in self._fields:
            arch = etree.fromstring(result["arch"])

            notebook_elem = arch.find(".//notebook")
            if notebook_elem is None:
                notebook_elem = etree.SubElement(arch, "notebook")
                sheet = arch.find(".//sheet")
                if sheet is not None:
                    sheet.append(notebook_elem)
                else:
                    arch.append(notebook_elem)

            # Create a new tab/page for the protected attachments
            page_elem = etree.SubElement(
                notebook_elem, "page", string="Protected Attachments"
            )

            # Add the one2many field to the new tab/page
            field_elem = etree.SubElement(
                page_elem, "field", name="protected_attachment_ids"
            )
            field_elem.set("options", '{"editable": "top"}')

            # Define the tree structure for the one2many field
            # tree_elem = etree.SubElement(field_elem, 'tree', editable="top")
            # etree.SubElement(tree_elem, 'field', name="attachment")
            # etree.SubElement(tree_elem, 'field', name="attachment_name")

            # Update the architecture of the view
            result["arch"] = etree.tostring(arch, encoding="unicode")
        return result
