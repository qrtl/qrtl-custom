# Copyright 2026 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests.common import TransactionCase


class TestSitemapBaseUrl(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.website = cls.env["website"].search([], limit=1)

    def _assert_base_url(self, domain, expected):
        self.website.domain = domain
        self.assertEqual(
            self.website._get_sitemap_base_url(),
            expected,
            "unexpected sitemap base URL for domain %r" % (domain,),
        )

    def test_domain_becomes_the_base_url(self):
        self._assert_base_url("https://www.example.com", "https://www.example.com/")

    def test_trailing_slash_is_not_doubled(self):
        # The sitemap template appends a page path that already starts with a
        # slash, so the base URL must end with exactly one.
        self._assert_base_url("https://www.example.com/", "https://www.example.com/")

    def test_explicit_http_scheme_is_kept(self):
        self._assert_base_url("http://www.example.com", "http://www.example.com/")

    def test_domain_entered_without_a_scheme(self):
        # Website._handle_domain prepends https:// on write, so this asserts the
        # end-to-end result rather than this module's own guard.
        self._assert_base_url("www.example.com", "https://www.example.com/")

    def test_scheme_is_added_for_an_unnormalised_domain(self):
        # Bypass Website._handle_domain to exercise the guard in this module,
        # for values that never went through it.
        self.env.cr.execute(
            "UPDATE website SET domain = %s WHERE id = %s",
            ("www.example.com", self.website.id),
        )
        self.website.invalidate_recordset(["domain"])
        self.assertEqual(
            self.website._get_sitemap_base_url(), "https://www.example.com/"
        )

    def test_no_domain_falls_back_to_odoo_default(self):
        # Falsy tells the controller to leave url_root alone.
        self._assert_base_url("", False)
        self._assert_base_url(False, False)
