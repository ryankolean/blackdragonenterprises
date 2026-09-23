# Black Dragon Enterprises

Concept rebuild of **blackdragonenterprises.com**, Angus Peacock's coaching, leadership and consulting site, by [Summit Software Solutions](https://summitsoftwaresolutions.dev/) as part of a proposal. It moves the site off Wix, focuses it on coaching and consulting, and keeps every feature the current site has.

**This is a preview, not the live site.** The live site is [blackdragonenterprises.com](https://www.blackdragonenterprises.com/). Every page here carries a concept banner, is marked `noindex, nofollow`, and `robots.txt` disallows crawling. Unconfirmed content is marked on the page with a dashed *Placeholder* box.

- **Concept site:** https://ryankolean.github.io/blackdragonenterprises/
- **Brand system:** https://ryankolean.github.io/blackdragonenterprises/specimen.html
- **Sister concept:** [`ryankolean/thesisuway`](https://github.com/ryankolean/thesisuway), where all Sisu content and the app now live
- **Tickets:** [SUMMIT-197](https://ryan-kolean.atlassian.net/browse/SUMMIT-197) (epic), [SUMMIT-207](https://ryan-kolean.atlassian.net/browse/SUMMIT-207) (this site), [SUMMIT-208](https://ryan-kolean.atlassian.net/browse/SUMMIT-208) (domain move)

## The site

Static HTML, no framework, no build step.

| Page | What | Replaces |
|---|---|---|
| `index.html` | Hero, four services, Angus, a testimonial, links to The Sisu Way and booking | Home |
| `about.html` | Background, credentials, History timeline | About, History |
| `services.html` | Coaching, leadership, performance, project management; how it works | — |
| `testimonials.html` | Client quotes | Testimonials |
| `media.html` | Book, podcasts, talks | Podcast Sites |
| `contact.html` | Booking embed and contact form | Contact |
| `specimen.html` | The brand system, rendered | — |

Page mapping, redirects and the feature parity audit are in [`design-catalog/site-plan.md`](design-catalog/site-plan.md).

## Brand system

Proposed, not measured: the Wix site was not accessible when the concept was built. Full rationale, contrast tables and rules in [`design-catalog/brand-guidelines.md`](design-catalog/brand-guidelines.md).

| Token | Value | Role |
|---|---|---|
| `--ivory` | `#F5F1E8` | Page field |
| `--stone` | `#E6DFD1` | Tint sections |
| `--ink` | `#1F1E1C` | Text |
| `--obsidian` | `#131315` | Hero, dark sections, footer, concept bar |
| `--cinnabar` | `#A3262A` | The seal: brand color, primary buttons, links |
| `--cinnabar-deep` | `#7A1A1D` | Hover and pressed |
| `--brass` | `#C39A4B` | Accent, **on obsidian only** |
| `--ash` | `#5F5A52` | Secondary text on light |

Type is **Cormorant Garamond** (headings, quotes) and **Manrope** (everything else). Every text and background pair in use passes WCAG AA; the forbidden pairs are listed in the guidelines.

## Research

| Path | What |
|---|---|
| [`design-catalog/brand-guidelines.md`](design-catalog/brand-guidelines.md) | Palette, contrast, type, seal, motif, components, voice |
| [`design-catalog/site-plan.md`](design-catalog/site-plan.md) | Page map, redirects from Wix URLs, feature parity audit, cutover order |
| [`design-catalog/assets-needed.md`](design-catalog/assets-needed.md) | Everything we need from Angus, in one list |

## Known placeholders

- **Testimonials, history and podcast links** wait on Wix access; two testimonial lines are as indexed by search engines and need checking.
- **Services** are proposed from the current site's four headline services.
- **The contact form** is not connected. **Booking** uses the Google Calendar booking page Angus already uses in the SISU app.
- **The seal** is drawn for the concept.
- **No photography** yet.

## Local preview

```bash
python3 -m http.server 4332
```

Then `http://localhost:4332/`.

## Deploy

GitHub Pages from Actions (`.github/workflows/pages.yml`). One-time setup: **Settings → Pages → Source: GitHub Actions**.

## Precedent

Mirrors [`ryankolean/roses`](https://github.com/ryankolean/roses) and [`ryankolean/meantime`](https://github.com/ryankolean/meantime): static multi-page HTML on GitHub Pages with a concept banner and a documented brand system.
