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
        arch = etree.fromstring(result["arch"])
        if view_type == "form" and "ignore_mail_validation" in self._fields:
            id_elem = """<field name="ignore_mail_validation"/>"""
            id_elem = etree.fromstring(id_elem)
            form = arch.xpath("//form")[0]
            partner_field = form.xpath('//field[@name="partner_id"]')
            if partner_field:
                parent = partner_field[0].getparent()
                index = parent.index(partner_field[0])
                parent.insert(index + 1, id_elem)
            else:
                form.insert(0, id_elem)
        result["arch"] = etree.tostring(arch)
        return result
