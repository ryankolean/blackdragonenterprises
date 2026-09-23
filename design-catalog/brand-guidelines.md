# Brand Guidelines: Black Dragon Enterprises

**Version:** 0.1, 2026-09-23. Proposal by Summit Software Solutions, pending Angus Peacock's approval.
**Live version:** [`specimen.html`](../specimen.html) renders every token, pair and component below.

## Principle

The current Wix site could not be sampled for this concept (no account access yet, and the site was not reachable from the build environment), so this system is **proposed, not measured**. When we get into the Wix account, check the existing logo, colors and fonts against this document. Anything Angus is attached to wins, and the palette gets re-tested.

What the brand has to carry, from public sources:

| Fact | Source |
|---|---|
| Tagline "Coaching, Development, Education" | blackdragonenterprises.com page title |
| "Coaching, Leadership, Performance and Project Management … more than twenty years of international experience in Business, Sports & Military environments" | blackdragonenterprises.com |
| Royal Navy veteran; rugby coach on four continents; World Rugby Level 3 coach educator; life coach | Public coaching profiles |
| English, French and Mandarin Chinese | Public coaching profiles |
| Coaching philosophy framed as "SISU coaching … an investment in your own longevity" | blackdragonenterprises.com |

**The idea: lacquer, brass and a seal.** A dragon, a naval career and fluent Mandarin. Black lacquer and ivory paper, signed once with a cinnabar seal, with naval brass as the only metal. It should feel like an executive coach's study, not a martial-arts school.

**Relationship to The Sisu Way.** The two brands are deliberately distinct (warm black, red and brass vs. cool northern blues) because they sell different things to different people. They share one person, and each links to the other from About and the footer.

## Color

### Tokens

```css
:root {
  --ivory:         #F5F1E8;  /* page field */
  --stone:         #E6DFD1;  /* tint sections */
  --ink:           #1F1E1C;  /* body text, headings on light */
  --obsidian:      #131315;  /* hero, dark sections, footer, concept bar */
  --cinnabar:      #A3262A;  /* the seal: brand color, primary buttons on light, links */
  --cinnabar-deep: #7A1A1D;  /* hover / pressed */
  --brass:         #C39A4B;  /* accent on obsidian ONLY */
  --ash:           #5F5A52;  /* secondary text on ivory and stone */
}
```

### Roles

| Token | Use for | Never use for |
|---|---|---|
| `--ivory` | Page, cards, text on dark and on cinnabar | Text on brass |
| `--stone` | Alternate sections, muted text on dark | Text on ivory |
| `--ink` | All reading text on light, secondary buttons | Large fills (use obsidian) |
| `--obsidian` | Hero, dark bands, footer, text on brass | Body text on light (use ink) |
| `--cinnabar` | Primary buttons on light, links, labels, card top-rules, the seal | Text on obsidian |
| `--cinnabar-deep` | Hover and pressed states, error text | Fills larger than a button |
| `--brass` | On obsidian only: labels, italic emphasis, primary buttons, rules, the pearl | **Anything on ivory or stone** |
| `--ash` | Captions, hints, meta text on ivory and stone | Anything on dark |

**Proportion.** Roughly 55% ivory and stone, 35% obsidian and ink, 10% cinnabar and brass combined. Cinnabar appears once per view as a primary action; brass never leaves the dark sections.

### WCAG contrast, every pair in use

| Text | Background | Ratio | AA | AAA |
|---|---|---|---|---|
| `--ink` | `--ivory` | **14.78** | pass | pass |
| `--ink` | `--stone` | **12.56** | pass | pass |
| `--cinnabar` | `--ivory` | **6.50** | pass | — |
| `--cinnabar` | `--stone` | **5.52** | pass | — |
| `--ivory` | `--cinnabar` | **6.50** | pass | — |
| `--ivory` | `--cinnabar-deep` | **9.35** | pass | pass |
| `--cinnabar-deep` | `--ivory` | **9.35** | pass | pass |
| `--ivory` | `--obsidian` | **16.46** | pass | pass |
| `--stone` | `--obsidian` | **14.00** | pass | pass |
| `--brass` | `--obsidian` | **7.11** | pass | pass |
| `--obsidian` | `--brass` | **7.11** | pass | pass |
| `--ash` | `--ivory` | **6.07** | pass | — |
| `--ash` | `--stone` | **5.16** | pass | — |

### Forbidden pairs

| Text | Background | Ratio | Rule |
|---|---|---|---|
| `--brass` | `--ivory` | 2.32 | **Never.** Brass lives on obsidian only |
| `--brass` | `--stone` | 1.97 | **Never** |
| `--ivory` | `--brass` | 2.32 | **Never.** Brass buttons take obsidian text |
| `--cinnabar` | `--obsidian` | 2.53 | **Never as text.** The seal sits on obsidian as a filled shape only |
| `--ash` | `--obsidian` | 2.71 | **Never.** Muted text on dark uses `--stone` |

## Typography

```css
--font-display: "Cormorant Garamond", Garamond, "Times New Roman", serif;  /* headings, quotes, numerals */
--font-ui:      "Manrope", system-ui, -apple-system, "Segoe UI", sans-serif; /* body, labels, buttons, nav, forms */
```

**Why.** Cormorant is a high-contrast Garamond with a beautiful italic: considered and a little formal, the voice of an experienced advisor. Italic carries emphasis in headings ("Find what you *didn't know* you had"). Manrope is open and modern, reads well at small sizes, and keeps the site from feeling antique. Both are free on Google Fonts.

### Scale

| Element | Family | Size | Weight | Line height | Notes |
|---|---|---|---|---|---|
| Display | Cormorant Garamond | clamp(48px, 8vw, 96px) | 500 | 0.98 | Italic emphasis in brass (dark) or cinnabar (light) |
| H1 | Cormorant Garamond | clamp(42px, 6vw, 72px) | 500 | 1.05 | |
| H2 | Cormorant Garamond | clamp(32px, 4.2vw, 52px) | 500 | 1.05 | |
| H3 | Cormorant Garamond | clamp(23px, 2.6vw, 30px) | 600 | 1.15 | |
| Label | Manrope | 13px | 700 | 1.2 | Uppercase, **0.2em**, preceded by a 28px rule |
| Nav | Manrope | 14px | 600 | 1.2 | 0.06em |
| Button | Manrope | 14px | 700 | 1.2 | Uppercase, 0.12em |
| Lede | Manrope | clamp(17px, 2vw, 21px) | 400 | 1.6 | |
| Body | Manrope | 17px (16px < 640px) | 400 | 1.7 | |
| Quote | Cormorant Garamond italic | clamp(21px, 2.4vw, 26px) | 500 | 1.35 | |

### Rules

- Cormorant never goes below 21px: its small x-height needs size.
- Headings in sentence case. Uppercase is for labels, buttons and the "Enterprises" sub-line only.
- One italic emphasis per heading at most.
- Measure capped at 64ch.

## Mark

**The seal.** A cinnabar square with an ivory inner border, like the red chop that signs a Chinese painting, holding a dragon chasing a brass pearl. In Chinese art the dragon pursues the pearl of wisdom, which is a coach's job in one image. Files: `assets/img/seal.svg`, `favicon.svg`.

- **Placeholder quality.** Drawn for the concept; a designer should refine it. If Angus has an existing logo, it replaces this.
- **Option to discuss:** 黑龍 ("black dragon") inside the seal instead of the drawing, if Angus wants his Mandarin to carry the mark. Get it checked by a native reader before use.
- Lockup: seal + "Black Dragon" in Cormorant 600 over "ENTERPRISES" in Manrope 700 at 0.3em tracking.
- Minimum 24px for the seal, 150px wide for the lockup. Clear space equal to the inner-border inset.
- Always cinnabar with ivory line work and a brass pearl. Never outline it, recolor it, or place it on cinnabar.

## Motif

- **Scales.** A brass scale pattern at 7% opacity, anchored to the right edge of dark heroes only (`assets/img/scales.svg`).
- **Seal rule.** Section breaks: a brass hairline with a small cinnabar diamond at its centre. The same diamond marks timeline points and separates the Business ◆ Sport ◆ Military line.
- Card top rules are 3px cinnabar.

## Style guide

### Spacing

8-point scale: `4 8 12 16 24 32 48 64 96 128`. Sections are 96px padding on desktop, 64px on phones. Container 1160px, gutters 32px (16px under 640px).

### Radii, borders, shadows

- 2px radius everywhere. The brand is square-shouldered, like the seal.
- Hairlines are ink at 14% on light and brass at 35% on dark.
- **No drop shadows.**

### Buttons

| Variant | Fill | Text | Border | Hover |
|---|---|---|---|---|
| Primary (light) | cinnabar | ivory | none | cinnabar-deep |
| Secondary (light) | none | ink | 1px ink | ink fill, ivory text |
| Primary (dark) | brass | obsidian | none | `#D6AE5F` |
| Secondary (dark) | none | ivory | 1px ivory 60% | ivory fill, obsidian text |

48px minimum height (44px in the compact header), uppercase Manrope 700 at 14px, 0.12em tracking. One primary per view.

### Components on the concept

- **Service card**: ivory, 3px cinnabar top rule, Cormorant italic roman numeral, H3, 16px body.
- **Quote**: Cormorant italic, 3px cinnabar left rule (brass on dark), caption in small caps.
- **Timeline**: cinnabar hairline with diamond markers.
- **Form**: 48px inputs on ivory, small-caps labels, cinnabar focus ring.
- **Booking embed**: dashed stand-in box until the scheduling tool is chosen.
- **Placeholder marker**: dashed cinnabar box. Every unconfirmed item carries it.
- **Concept bar**: obsidian strip above the header, reading "CONCEPT PREVIEW — A redesign by Summit Software Solutions. Not the live site." Removed at launch.

### Motion

Hover transitions only, 150ms ease-out; disabled under `prefers-reduced-motion`.

## Voice and tone

Write like a senior officer who is also a good listener: plain words, short sentences, confidence without swagger. Lead with the client's outcome, then Angus's credentials.

| Say | Don't say |
|---|---|
| Find what you didn't know you had. | Unleash your inner dragon. |
| Start with a conversation. | Dominate your competition. |
| Twenty years in business, sport and the military. | Warrior mindset. Alpha leadership. |

## Photography direction

A proper portrait of Angus first: natural light, dark background, looking at the camera, no arms folded. Then coaching in action (pitch-side, workshop, one-to-one), and environments with texture: wood, paper, brass, water. Avoid stock handshakes and dragon imagery; the seal is the only dragon.

## Traceability

| Decision | Reason |
|---|---|
| Obsidian + ivory base | "Black Dragon", read as lacquer rather than heavy-metal black |
| Cinnabar seal | Chinese chop that signs a work; Angus speaks Mandarin |
| Brass accent on dark only | Royal Navy brass; fails contrast on light |
| Dragon chasing the pearl | Traditional image of pursuing wisdom: coaching |
| Cormorant Garamond | Senior-advisor register; expressive italic |
| Manrope | Legible body and UI; keeps the site current |
