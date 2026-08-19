# Copyright 2026 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import http
from odoo.http import request

from odoo.addons.website.controllers.main import Website as WebsiteController


class Website(WebsiteController):
    @http.route()
    def sitemap_xml_index(self, **kwargs):
        """Anchor the sitemap to website.domain instead of the request host.

        Odoo builds every <loc> from request.httprequest.url_root and caches the
        rendered sitemap for 12 hours in an ir.attachment keyed only by website
        id -- no host in the cache key. A single request arriving on a
        non-canonical host therefore rewrites the sitemap that every other host
        then serves, search engines included.
        """
        base_url = request.website._get_sitemap_base_url()
        if base_url:
            # url_root is a werkzeug cached_property, whose __set__ replaces the
            # cached value; the assignment lives only for this request.
            request.httprequest.url_root = base_url
        return super().sitemap_xml_index(**kwargs)
