# Launch checklist: blackdragonenterprises.com

The preview on GitHub Pages is the concept. Launch builds the same pages without the concept bar or `noindex`, with production URLs, and serves them from Cloudflare Pages at blackdragonenterprises.com.

## Before launch (needs Angus)
- [ ] Angus signs off the copy, photos (full-resolution originals) and testimonials (permission from each person quoted).
- [ ] Wix dashboard: confirm page slugs (see `_redirects`), whether the old blog and store still exist, and export contacts and bookings.
- [ ] His Google Calendar booking page is set up as a free 20-minute "Discovery" call, with confirmation and reminder emails.
- [ ] Decide on the optional contact form. If kept, connect it to a form service (Formspree or Basin) and test it.
- [ ] Porkbun account in Angus's name; domain transfer started (60-day lock rule applies). **Copy every DNS record first, especially MX, SPF, DKIM and DMARC for angus@ email.**

## Build
```bash
git checkout -b launch origin/launch-prep
SITE_ENV=production python3 tools/build_bde.py
```
This removes the concept bar and `noindex`, points canonicals and share images at https://blackdragonenterprises.com/, rewrites the 404 page and manifest for the root path, and writes `robots.txt` (allow) and `sitemap.xml`. Decide whether `specimen.html` (the brand guide) stays public; it isn't in the sitemap.

## Deploy
- [ ] Cloudflare Pages project connected to this repo (production branch `launch`), no build command, output directory `/`.
- [ ] Add the custom domain in Cloudflare Pages, then point DNS at Porkbun to it (CNAME for `www`; apex via Cloudflare DNS or an ALIAS record). HTTPS on both `www` and apex; one redirects to the other.
- [ ] `_redirects` is live: spot-check `/aboutme`, `/blank-page`, `/about-copy`, one `/post/...` URL.
- [ ] Cookieless analytics (Plausible, Fathom or Cloudflare Web Analytics) added; no cookie banner needed.

## Cutover and after
- [ ] Test at 375, 768 and 1280 px: no horizontal scroll, no console errors, booking link works, email to angus@ still delivers.
- [ ] Submit the sitemap in Google Search Console.
- [ ] Keep the Wix plan for 2–4 weeks as a fallback, then cancel it.

**Note on `/about`:** on the live Wix site, the "Work With Angus" page may use the `/about` slug. The new site uses `/about` for About Angus and `/services` for Work with Angus. If Wix's `/about` has search traffic, consider renaming the new About page (for example `/angus`) and redirecting `/about` to `/services`.
