Builds sitemap URLs from the website's own domain instead of the host that
happened to request the sitemap.

Odoo renders every `<loc>` in `/sitemap.xml` from
`request.httprequest.url_root` and caches the result for 12 hours in an
`ir.attachment` keyed only by website id — the requesting host is not part of
the cache key. One request arriving on a non-canonical host (a server's bare IP
address, an ops hostname, an unmatched SNI landing on the default vhost) is
therefore enough to rewrite the sitemap that every other host, search engine
crawlers included, then serves for the next 12 hours.

Odoo already honours the **Website Domain** setting for `robots.txt`, the
`noindex` meta tag and canonical URLs, but not for the sitemap. This module
closes that gap: when Website Domain is set, sitemap URLs always use it. When it
is empty, Odoo's default behaviour is left untouched.

The symptom, if you are looking for it in Google Search Console, is a sitemap
whose URLs all point at an unexpected host — typically reported as *Page with
redirect* or as URLs outside the property, with no obvious change on the site
itself to explain it.
