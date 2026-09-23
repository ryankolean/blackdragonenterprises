# Site plan and feature parity: blackdragonenterprises.com

Black Dragon moves off Wix onto Summit's stack, and **the new site must do everything the current one does** (Jira SUMMIT-207). All Sisu content moves to thesisuway.com.

## Pages

| New page | File | Replaces on the current Wix site | Old URL (redirect from) |
|---|---|---|---|
| Home | `index.html` | Home | `/` |
| About | `about.html` | About | `/aboutme` |
| About › History | `about.html#history` | History | `/clients` |
| Services | `services.html` | Service copy on Home | — |
| Testimonials | `testimonials.html` | Testimonials | `/blank-page` |
| About (duplicate) | `about.html` | About Me (a duplicate About page) | `/about-copy` |
| Media | `media.html` | Podcast Sites (show hosted on Podbean) | `/podcastsites` |
| Blog | not built yet | Blog (Wix Blog app) | `/blog`, `/post/...` (one redirect per post) |
| Store | not built yet; keep or drop is Angus's call | Store (Wix Stores app): rugby, performance and sports fashion wear | `/blackdragonstore` |
| Contact | `contact.html` | Contact text (LinkedIn DM or email) | none |
| Brand system | `specimen.html` | — | — |

Current pages were found from search-engine listings of the site (public review, 2026-09-23; the live site could not be loaded directly). The full list, including any hidden or member-only pages, the blog post count and the store's products, must be confirmed from inside the Wix account.

## Feature parity audit

Fill in from the Wix dashboard's **installed apps** list. Nothing is dropped without a decision.

| Feature | On current site? | Replacement on Summit's stack | Concept status |
|---|---|---|---|
| Contact form | No form found; contact is by LinkedIn DM or email | Form service (Formspree, Basin or similar) emailing Angus | Form built, not connected |
| Booking / scheduling | None found publicly; confirm in the dashboard | Google Calendar booking page Angus already uses in the SISU app | Linked from Contact and every "Book" button |
| Payments / store | **Yes: Wix Stores** at `/blackdragonstore` (merchandise). Sales activity unknown | Shopify Starter buy buttons or Stripe payment links, or drop the store if it has no sales | Not built |
| Email list / newsletter | None found publicly; confirm in the dashboard | Buttondown, MailerLite or similar; import Wix contacts | Not built |
| Blog | **Yes: Wix Blog** at `/blog`, posts at `/post/...` (rugby and project management) | Static posts (or a headless CMS if Angus wants to self-edit); redirect every post URL | Not built |
| Members area / client downloads | None found publicly; confirm in the dashboard | Decide case by case | Not built |
| Testimonials | Yes | Static page | Built, needs full content |
| History / clients | Yes | Section on About | Built, needs content |
| Podcast links | Yes; the show is hosted on Podbean (theblackdragon.podbean.com) | Media page links to Podbean; hosting unchanged | Built, needs links |
| Analytics | To verify | Plausible, Fathom or GA4 | Not built |
| Business email @blackdragonenterprises.com | **Yes**: angus@ is published on the site | Keep existing provider; copy MX records to Porkbun | SUMMIT-208 |

## Data to export before cutover

Blog posts and their images, store products and order history, contacts and subscribers, form submissions, any bookings.

## Cutover order

1. Parity table complete and every row tested end to end on the preview.
2. Angus signs off.
3. Domain moves to Porkbun (SUMMIT-208); DNS points at the new site; redirects above go live.
4. Wix plan stays active 2–4 weeks as a fallback, then is cancelled.

## Name collisions

blackdragonent.com (a sales and accounting consultancy) and Black Dragon Comics are unrelated businesses with similar names. Keep this in mind for SEO and the trademark check.
