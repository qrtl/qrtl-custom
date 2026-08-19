# Copyright 2026 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models


class Website(models.Model):
    _inherit = "website"

    def _get_sitemap_base_url(self):
        """Return the base URL to build sitemap <loc> entries from.

        A falsy return means "keep Odoo's default", i.e. the requesting host.

        ``domain`` is normalised on write by ``Website._handle_domain``, which
        prepends ``https://`` when the scheme is missing and strips trailing
        slashes, so in practice it already carries a scheme. The guards here
        cover values that did not go through that path -- a direct SQL update, a
        database predating it -- and restore the single trailing slash that
        ``url_root`` is expected to end with.
        """
        self.ensure_one()
        domain = (self.domain or "").strip()
        if not domain:
            return False
        if "://" not in domain:
            domain = "https://" + domain
        return domain.rstrip("/") + "/"
