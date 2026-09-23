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
| Media | `media.html` | Podcast Sites | `/podcastsites` |
| Contact | `contact.html` | Contact form / booking (to verify) | to verify |
| Brand system | `specimen.html` | — | — |

Current pages were found from search-engine listings of the site. The full list, including any hidden or member-only pages, must be confirmed from inside the Wix account.

## Feature parity audit

Fill in from the Wix dashboard's **installed apps** list. Nothing is dropped without a decision.

| Feature | On current site? | Replacement on Summit's stack | Concept status |
|---|---|---|---|
| Contact form | To verify | Form service (Formspree, Basin or similar) emailing Angus | Form built, not connected |
| Booking / scheduling | To verify on Wix | Google Calendar booking page Angus already uses in the SISU app | Linked from Contact and every "Book" button |
| Payments / packages | To verify | Stripe payment links or checkout | Not built |
| Email list / newsletter | To verify | Buttondown, MailerLite or similar; import Wix contacts | Not built |
| Blog | To verify | Static posts or a headless CMS | Not built |
| Members area / client downloads | To verify | Decide case by case | Not built |
| Testimonials | Yes | Static page | Built, needs full content |
| History / clients | Yes | Section on About | Built, needs content |
| Podcast links | Yes | Media page | Built, needs links |
| Analytics | To verify | Plausible, Fathom or GA4 | Not built |
| Business email @blackdragonenterprises.com | To verify | Keep existing provider; copy MX records to Porkbun | SUMMIT-208 |

## Data to export before cutover

Contacts and subscribers, form submissions, bookings, any blog posts, any customer or payment history.

## Cutover order

1. Parity table complete and every row tested end to end on the preview.
2. Angus signs off.
3. Domain moves to Porkbun (SUMMIT-208); DNS points at the new site; redirects above go live.
4. Wix plan stays active 2–4 weeks as a fallback, then is cancelled.
