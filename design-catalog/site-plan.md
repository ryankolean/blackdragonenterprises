# Site plan and feature parity: blackdragonenterprises.com

Black Dragon moves off Wix onto Summit's stack, and **the new site must do everything the current one does** (Jira SUMMIT-207). All Sisu content moves to thesisuway.com.

## The current site (reviewed 2026-09-23)

Reviewed from screenshots of the live site and the full Testimonials text, supplied by Ryan. The live site is a newer, simpler Wix build than the one search engines had indexed. Its navigation is **Home · Work With Angus · Media · Testimonials · Discovery Call**, on a navy (#003080-ish) background with white condensed headings. Footer: email, LinkedIn, "Proudly created with Wix.com". A Wix cookie-consent banner shows on first visit.

## Pages

| New page | File | Replaces on the current Wix site | Old URL (redirect from) |
|---|---|---|---|
| Home | `index.html` | Home: "SISU · Authentic Resilience" hero, bio, Book a Discovery Call | `/` |
| Work with Angus | `services.html` | Work With Angus: five offerings (page titled "About") | `/about` *(confirm slug)* |
| About | `about.html` | No current equivalent; older indexed pages | `/aboutme`, `/clients` |
| Testimonials | `testimonials.html` | Testimonials: all 17, carried over verbatim | `/blank-page` *(confirm slug)* |
| Media | `media.html` | Media: YouTube, Substack, Buy the Book (page titled "About Me") | `/about-copy` *(confirm slug)* |
| Discovery call | `contact.html` | Discovery Call: Wix Bookings "Discovery" service, free, 20 minutes | *(confirm slug)* |
| Brand system | `specimen.html` | — | — |

**Older indexed pages** (`/blog`, `/post/...`, `/blackdragonstore`, `/podcastsites`, `/clients`, `/aboutme`) are not in the current navigation. They may be left over from the previous design and still reachable, or already deleted. Confirm in the Wix dashboard. Either way they get redirects so old links keep working.

## Feature parity audit

| Feature | On current site? | Replacement on Summit's stack | Concept status |
|---|---|---|---|
| **Booking** | **Yes: Wix Bookings**, "Discovery", free 20-minute call, Book Now | Google Calendar appointment page Angus already uses in the SISU app (set to 20 minutes), or Cal.com | Built: every "Book" button links to it |
| Service descriptions | Yes, five offerings | Static page, Angus's copy | Built |
| Testimonials | Yes, 17 | Static page | Built, verbatim |
| Media links | YouTube (@bytheblackdragon), Substack (@sisublackdragon), book (Tactical 16 author page) | Media page | Built, real links |
| Contact | Email and LinkedIn in the footer; no form | Same; an optional form is shown in the concept | Form built, not connected, optional |
| Cookie consent | Yes, Wix banner | Only needed if analytics or embeds set cookies; cookieless analytics avoids it | Not needed yet |
| Blog | Old indexed pages only | Redirect old URLs, or carry posts over if Angus wants them | Not built |
| Store | Old indexed page only | Drop unless Angus wants it back | Not built |
| Email list / members area | None seen | — | — |
| Analytics | Wix built-in (assumed) | Plausible, Fathom or GA4 | Not built |
| Business email @blackdragonenterprises.com | **Yes** | Keep existing provider; copy MX records to Porkbun | SUMMIT-208 |

## Data to export before cutover

Wix Bookings history and any upcoming booked calls, contacts, and (if they still exist) blog posts and store orders.

## Cutover order

1. Parity table complete and every row tested end to end on the preview.
2. Angus signs off.
3. Domain moves to Porkbun (SUMMIT-208); DNS points at the new site; redirects above go live.
4. Wix plan stays active 2–4 weeks as a fallback, then is cancelled.

## Name collisions

blackdragonent.com (a sales and accounting consultancy) and Black Dragon Comics are unrelated businesses with similar names. Keep this in mind for SEO and the trademark check.
