# Copyright 2026 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import re

from odoo.tests import tagged
from odoo.tests.common import HttpCase

CANONICAL = "https://sitemap-test.example.com"
# A host that is not the canonical one and never should be: the shape of the
# incident this module exists to prevent is a request arriving on the server's
# own IP address.
FOREIGN_HOST = "172.16.31.42"


@tagged("-at_install", "post_install")
class TestSitemapRoute(HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.website = cls.env["website"].search([], limit=1)

    def _fetch_locs(self, host):
        # /sitemap.xml serves a 12h-cached attachment, so without clearing it
        # the response says nothing about what this request would generate.
        self.env["ir.attachment"].search(
            [("type", "=", "binary"), ("url", "=like", "/sitemap%")]
        ).unlink()
        response = self.url_open("/sitemap.xml", headers={"Host": host})
        self.assertEqual(response.status_code, 200)
        locs = re.findall(r"<loc>([^<]+)</loc>", response.text)
        self.assertTrue(locs, "the sitemap came back with no <loc> entries")
        return locs

    def test_foreign_host_does_not_reach_the_locs(self):
        """Every <loc> uses website.domain, whatever host asked for the sitemap."""
        self.website.domain = CANONICAL
        offenders = [
            loc
            for loc in self._fetch_locs(FOREIGN_HOST)
            if not loc.startswith(CANONICAL + "/")
        ]
        self.assertFalse(
            offenders[:5],
            "sitemap entries built from the request host instead of website.domain",
        )

    def test_request_host_leaks_in_without_a_domain(self):
        """Odoo's unguarded behaviour, which is what this module intercepts.

        Kept as a test because it is the counterfactual: should it ever fail,
        either Odoo now anchors the sitemap itself -- making this module
        redundant -- or the override stopped honouring an empty domain.
        """
        self.website.domain = ""
        locs = self._fetch_locs(FOREIGN_HOST)
        self.assertTrue(
            any(FOREIGN_HOST in loc for loc in locs),
            "expected the request host in the <loc> entries when no domain is set",
        )
