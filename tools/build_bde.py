"""One-off generator for the Black Dragon Enterprises concept pages. Output is plain static HTML."""
import pathlib, textwrap, importlib.util

ROOT = pathlib.Path(__file__).resolve().parents[1]
import os
PROD = os.environ.get("SITE_ENV") == "production"   # SITE_ENV=production python3 tools/<this file> for the live build
BASE = "https://blackdragonenterprises.com/" if PROD else "https://ryankolean.github.io/blackdragonenterprises/"
SISU = "https://thesisuway.com/" if PROD else "https://ryankolean.github.io/thesisuway/"
EMAIL = "angus@blackdragonenterprises.com"
BOOK = "https://calendar.app.google/LoMbzd8xpjeCvdap7"
LINKEDIN = "https://www.linkedin.com/in/coachangus/"
BOOKSTORE = "https://tactical16.com/angus-peacock-author/"
NAAFI = "https://podcasts.apple.com/podcast/naafi-break/id1557206328"

SEAL = '<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect x="3" y="3" width="58" height="58" rx="4" fill="#A3262A"/><rect x="7.5" y="7.5" width="49" height="49" rx="2" fill="none" stroke="#F5F1E8" stroke-width="1.5"/><g fill="#F5F1E8"><path d="M14 49 C12 41 18 37 25 37 C32 37 36 34 36 29 C36 24 31 22 27 24 C29 18 38 17 42 22 C46 27 44 36 36 40 C30 43 22 42 20 46 C19 48 17 50 14 49 Z"/><path d="M22 37.4 L24 33.5 L26 37.2 Z M29 36.6 L32 32.8 L32.6 36 Z M35.2 33 L39.2 31 L36.4 30 Z"/><path d="M40 20 L49 15.5 L46 21.5 L50 23 L43.5 25 Z"/><path d="M41 19.5 L40 13 L43.5 18.2 Z"/></g><circle cx="44.2" cy="20.4" r="1.1" fill="#A3262A"/><path d="M48.5 23.5 C51 27 51 31 48 34" fill="none" stroke="#F5F1E8" stroke-width="1.3" stroke-linecap="round"/><circle cx="46" cy="44" r="5.2" fill="#C39A4B"/><circle cx="44.4" cy="42.4" r="1.4" fill="#F5F1E8" opacity=".55"/></svg>'
WORDMARK = f'{SEAL}<span class="wordmark__text"><span class="wordmark__name">Black Dragon</span><span class="wordmark__sub">Enterprises</span></span>'

NAV = [("services.html", "Work with Angus"), ("about.html", "About"), ("testimonials.html", "Testimonials"), ("media.html", "Media"), ("contact.html", "Discovery call")]
YOUTUBE = "https://www.youtube.com/@bytheblackdragon"
SUBSTACK = "https://substack.com/@sisublackdragon"
exec(open(pathlib.Path(__file__).with_name("testimonials_bde.py")).read())


ROBOTS = "" if PROD else '<meta name="robots" content="noindex, nofollow">'
CONCEPT = "" if PROD else """<aside class="concept-bar" aria-label="Concept preview notice">
  <div class="container">
    <p><strong>Concept preview</strong>A redesign by <a href="https://summitsoftwaresolutions.dev/">Summit Software Solutions</a>. Not the live site, which is <a href="https://www.blackdragonenterprises.com/">blackdragonenterprises.com</a>. Placeholder content is marked.</p>
  </div>
</aside>
"""

def page(slug, title, desc, body, extra_head=""):
    cur = ' aria-current="page"'
    nav = "\n".join(f'        <li><a href="{h}"{cur if h == slug else ""}>{l}</a></li>' for h, l in NAV)
    url = BASE + ("" if slug == "index.html" else slug)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{ROBOTS}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Black Dragon Enterprises">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#131315">
<meta property="og:image" content="{BASE}assets/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/style.css">{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

{CONCEPT}
<header class="site-header">
  <div class="container site-header__inner">
    <a class="wordmark" href="index.html" aria-label="Black Dragon Enterprises, home">{WORDMARK}</a>
    <nav class="site-nav" aria-label="Main">
      <ul>
{nav}
        <li><a class="btn btn--primary" href="contact.html#book">Book a call</a></li>
      </ul>
    </nav>
  </div>
</header>

<main id="main">
{textwrap.dedent(body).strip()}
</main>

<footer class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <div>
        <a class="wordmark" href="index.html" aria-label="Black Dragon Enterprises, home">{WORDMARK}</a>
        <p style="margin-top:var(--s-4);max-width:36ch">Authentic resilience. Coaching, leadership and expedition learning with Angus Peacock.</p>
      </div>
      <div>
        <h2>Pages</h2>
        <ul>
          <li><a href="services.html">Work with Angus</a></li>
          <li><a href="about.html">About Angus</a></li>
          <li><a href="testimonials.html">Testimonials</a></li>
          <li><a href="media.html">Media</a></li>
          <li><a href="contact.html">Discovery call</a></li>
        </ul>
      </div>
      <div>
        <h2>Get in touch</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="contact.html#book">Book a discovery call</a></li>
          <li><a href="{LINKEDIN}">LinkedIn</a></li>
          <li><a href="{SISU}">The Sisu Way</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__base">
      <span>&copy; 2026 Black Dragon Enterprises. All rights reserved.</span>
      <span>Concept by <a href="https://summitsoftwaresolutions.dev/">Summit Software Solutions</a> &middot; <a href="specimen.html">Brand system</a></span>
    </div>
  </div>
</footer>
</body>
</html>
"""


P = {}

OFFERS = [
 ("The SISU Way&trade;: 1:1 coaching programme", "For leaders, founders, and people in transition: stepping into leadership, managing teams, or moving from military or service into business. Be steady under pressure, be a consistent performer and build resilience you can rely on."),
 ("Group &amp; team coaching", "Focused sessions for teams or cohorts who want shared language, accountability, and practical coaching support founded in lived experience."),
 ("The ABC Movement Programme", "Interactive training built around regulation, relationship, movement, and meaning, designed for real-world application before, during, and after high-pressure seasons."),
 ("Speaking &amp; keynotes", "Keynotes and talks on resilience, leadership under pressure, endurance, curiosity, and meaning, grounded in lived experience and practical takeaways."),
 ("Curriculum design &amp; expedition learning", "Design and facilitation for learning and development, from building your curriculum to creating meaningful competition."),
]
ROMAN = ["i.", "ii.", "iii.", "iv.", "v."]
def offer_cards(detail=False):
    return "\n".join(f'      <article class="service"><span class="service__num">{ROMAN[i]}</span><h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(OFFERS))

def esc(x):
    import html as _h
    return _h.escape(x, quote=False)
def quote_html(name, role, paras):
    body = "".join(f"<p>{esc(p)}</p>" for p in paras)
    return f'      <figure class="quote quote--long">{body}<footer>{esc(name)} &middot; {esc(role)}</footer></figure>'

P["index.html"] = page("index.html",
 "Black Dragon Enterprises - coaching, leadership and resilience with Angus Peacock",
 "Angus Peacock is a coach, author and adventurer. Twenty years, four continents: a grounded, practical approach to resilience and leadership.",
 f"""
<section class="hero dark">
  <div class="container hero__grid">
    <div>
      <span class="label">Sisu &middot; Authentic resilience</span>
      <h1 class="display">Twenty years. Four continents. <em>Environments most coaches have only seen in films.</em></h1>
      <p class="lede">Angus Peacock is a coach, author and adventurer. His expeditions across deserts, mountains and oceans inform a grounded, practical approach to resilience and leadership, refined over nearly two decades of coaching individuals and organisations.</p>
      <div class="btnrow">
        <a class="btn btn--primary" href="contact.html#book">Book a discovery call</a>
        <a class="btn btn--secondary" href="services.html">Work with Angus</a>
      </div>
    </div>
    <figure class="hero__photo"><img src="assets/img/photos/pine.jpg" alt="Frost-covered pine branches with the winter sun behind them" width="565" height="984" loading="eager"></figure>
  </div>
</section>

<section>
  <div class="container">
    <span class="label">Work with Angus</span>
    <h2>Bold transformations for people who are ready for them</h2>
    <p class="lede">Quality over volume is not a tagline. It is an operating principle.</p>
    <div class="grid grid--3" style="margin-top:var(--s-6)">
{offer_cards()}
    </div>
    <div class="btnrow"><a class="btn btn--secondary" href="services.html">How each one works</a></div>
  </div>
</section>

<section class="tint">
  <div class="container split split--wide">
    <div>
      <span class="label">About</span>
      <h2>Angus Peacock</h2>
      <p class="lede">Coach, author and adventurer. Royal Navy veteran and rugby coach educator on four continents.</p>
      <p>His coaching starts from <em>sisu</em>: the Finnish idea of resolve under pressure. It is the thread through his expeditions, his book, and two decades of coaching individuals, teams and organisations.</p>
      <div class="btnrow"><a class="btn btn--secondary" href="about.html">Read his story</a></div>
    </div>
    <ul class="facts">
      <li><b>~20 years</b>Coaching individuals and organisations</li>
      <li><b>Four continents</b>Deserts, mountains and oceans</li>
      <li><b>World Rugby Level 3</b>Coach and accredited coach educator</li>
      <li><b>Author</b><em>SISU: A Series of Epic Adventures</em></li>
    </ul>
  </div>
</section>

<section>
  <div class="container">
    <span class="label">The magic of Sisu coaching</span>
    <figure class="quote" style="max-width:900px">
      <p>&ldquo;He is capable of seeing deep into a person's potential and extracting abilities they never knew existed.&rdquo;</p>
      <footer>Jason B. &middot; Software Architect</footer>
    </figure>
    <div class="btnrow"><a class="btn btn--secondary" href="testimonials.html">Read all {len(T)} testimonials</a></div>
  </div>
</section>

<section class="dark">
  <div class="container split">
    <div>
      <span class="label">Also from Angus</span>
      <h2>The Sisu Way</h2>
      <p>Move. Endure. Thrive. The app and daily practice behind the coaching now has its own home.</p>
      <div class="btnrow"><a class="btn btn--secondary" href="{SISU}">Visit The Sisu Way</a></div>
    </div>
    <div>
      <span class="label">Start here</span>
      <h2>A 20-minute discovery call</h2>
      <p>No pitch, no pressure. Just an honest assessment of whether there's a fit.</p>
      <div class="btnrow"><a class="btn btn--primary" href="contact.html#book">Book a discovery call</a></div>
    </div>
  </div>
</section>
""")

P["about.html"] = page("about.html",
 "About Angus Peacock - Black Dragon Enterprises",
 "Angus Peacock: coach, author and adventurer, with nearly two decades of coaching individuals and organisations across four continents.",
 f"""
<section class="hero dark">
  <div class="container">
    <span class="label">About</span>
    <h1 class="display">Angus <em>Peacock</em></h1>
    <p class="lede">Coach, author and adventurer. His expeditions across deserts, mountains and oceans inform a grounded, practical approach to resilience and leadership.</p>
  </div>
</section>

<section>
  <div class="container split split--wide">
    <div>
      <span class="label">Background</span>
      <h2>Where the experience comes from</h2>
      <p>Angus grew up in Croydon, in south London, and served as an officer in the Royal Navy before building a second career in coaching that has taken him through China and on to the United States. He has coached rugby for more than two decades across North America, South America, Europe and Asia, holds World Rugby Level 3 and USA Rugby Level 400 credentials, and is an accredited coach educator.</p>
      <p>Alongside sport he coaches leaders, founders and people in transition, runs team programmes and speaks on resilience and leadership under pressure. He has also led complex projects in industry.</p>
      <p>His book, <em>SISU: A Series of Epic Adventures</em> (Tactical 16), tells the true story of turning personal trauma into a journey across Europe and Asia. The same resolve sits at the centre of his coaching.</p>
      <p class="placeholder"><b>To confirm</b>The first line of the hero is Angus's own copy from the current site. The background is assembled from public profiles and a 2023 podcast interview; Angus's own bio and a portrait will replace it.</p>
    </div>
    <ul class="facts">
      <li><b>Service</b>Royal Navy, officer</li>
      <li><b>Coaching</b>World Rugby Level 3 &middot; USA Rugby Level 400 &middot; coach educator</li>
      <li><b>Reach</b>North America, South America, Europe, Asia</li>
      <li><b>Languages</b>English, French, Mandarin Chinese</li>
      <li><b>Writing</b><em>SISU: A Series of Epic Adventures</em> &middot; <a href="{SUBSTACK}">Substack</a></li>
    </ul>
  </div>
</section>

<section class="tint" id="history">
  <div class="container split">
    <div>
      <span class="label">History</span>
      <h2>Milestones</h2>
      <p class="placeholder"><b>Placeholder</b>The current site no longer has a History page. Angus to confirm whether he wants a timeline; if so, dates and roles come from him.</p>
    </div>
    <ol class="timeline">
      <li><b>Royal Navy</b><span class="mute">Officer. Dates to confirm.</span></li>
      <li><b>International rugby coaching</b><span class="mute">Four continents over two decades.</span></li>
      <li><b>Colorado rugby</b><span class="mute">Head of Rugby Colorado; youth rugby growth.</span></li>
      <li><b>Black Dragon Enterprises</b><span class="mute">Coaching, team programmes, speaking and expedition learning.</span></li>
      <li><b><em>SISU</em>, published</b><span class="mute">Tactical 16.</span></li>
    </ol>
  </div>
</section>

<section class="dark">
  <div class="container split">
    <div>
      <span class="label">The Sisu Way</span>
      <h2>Move. Endure. Thrive.</h2>
      <p>The ideas behind the book and the coaching, as an app and a daily practice.</p>
      <div class="btnrow"><a class="btn btn--secondary" href="{SISU}">Visit The Sisu Way</a></div>
    </div>
    <div>
      <span class="label">Work with Angus</span>
      <h2>Start with a conversation</h2>
      <p>Twenty minutes, free. See whether there's a fit.</p>
      <div class="btnrow"><a class="btn btn--primary" href="contact.html#book">Book a discovery call</a></div>
    </div>
  </div>
</section>
""")

P["services.html"] = page("services.html",
 "Work with Angus - Black Dragon Enterprises",
 "The SISU Way 1:1 coaching programme, group and team coaching, the ABC Movement Programme, speaking and keynotes, and curriculum design and expedition learning.",
 f"""
<section class="hero dark">
  <div class="container">
    <span class="label">Work with Angus</span>
    <h1 class="display">Bold transformations for people who are <em>ready for them.</em></h1>
    <p class="lede">Quality over volume is not a tagline. It is an operating principle.</p>
    <div class="btnrow"><a class="btn btn--primary" href="contact.html#book">Book a discovery call</a></div>
  </div>
</section>

<section class="photos-band">
  <div class="container">
    <div class="photos">
      <img src="assets/img/photos/desert1.jpg" alt="A lone walker descending a steep desert ravine" width="346" height="251" loading="lazy">
      <img src="assets/img/photos/desert2.jpg" alt="A desert ridge under a blue sky, with a figure resting near the top" width="346" height="251" loading="lazy">
    </div>
    <p class="placeholder" style="margin-top:var(--s-4)"><b>Photos</b>Angus's own expedition photos from the current site, taken from screenshots. Full-resolution originals will replace them.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="label">Five ways to work together</h2>
    <div class="grid grid--2" style="margin-top:var(--s-6)">
{offer_cards()}
    </div>
    <p class="placeholder" style="margin-top:var(--s-6)"><b>To confirm</b>Descriptions are Angus's own, from the current site. Formats, lengths and whether prices are published are for Angus to decide.</p>
  </div>
</section>

<section class="tint">
  <div class="container">
    <span class="label">How it starts</span>
    <h2>Three steps</h2>
    <div class="grid grid--3" style="margin-top:var(--s-6)">
      <article class="service"><span class="service__num">1.</span><h3>Discovery call</h3><p>Twenty minutes, free. Angus asks questions; you are heard, not sold to.</p></article>
      <article class="service"><span class="service__num">2.</span><h3>Decide</h3><p>At the end of the call you choose how to move forward.</p></article>
      <article class="service"><span class="service__num">3.</span><h3>Work</h3><p>A programme shaped to you or your team, with accountability between sessions.</p></article>
    </div>
    <div class="btnrow"><a class="btn btn--primary" href="contact.html#book">Book a discovery call</a></div>
  </div>
</section>
""")

QUOTES = "\n".join(quote_html(*t) for t in T)
P["testimonials.html"] = page("testimonials.html",
 "Testimonials - Black Dragon Enterprises",
 "The magic of Sisu coaching: what clients, players and colleagues say about working with Angus Peacock.",
 f"""
<section class="hero dark">
  <div class="container">
    <span class="label">Testimonials</span>
    <h1 class="display">The magic of <em>Sisu coaching</em></h1>
    <p class="lede">From clients, players and colleagues across sport, business and service.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="quotes">
{QUOTES}
    </div>
  </div>
</section>

<section class="dark">
  <div class="container">
    <h2>Ready to start?</h2>
    <div class="btnrow"><a class="btn btn--primary" href="contact.html#book">Book a discovery call</a></div>
  </div>
</section>
""")

P["media.html"] = page("media.html",
 "Media - Black Dragon Enterprises",
 "Books, videos and writing on resilience, adventure and the SISU mindset by Angus Peacock.",
 f"""
<section class="hero dark">
  <div class="container">
    <span class="label">Media</span>
    <h1 class="display">Books, videos <em>&amp; writing</em></h1>
    <p class="lede">On resilience, adventure, and the SISU mindset.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="label">Where to find Angus</h2>
    <ul class="media" style="margin-top:var(--s-5)">
      <li><span class="kind">Book</span><h3><em>SISU: A Series of Epic Adventures</em></h3><a href="{BOOKSTORE}">Buy the book</a></li>
      <li><span class="kind">Video</span><h3>YouTube &middot; By the Black Dragon</h3><a href="{YOUTUBE}">Watch</a></li>
      <li><span class="kind">Writing</span><h3>Substack</h3><a href="{SUBSTACK}">Read</a></li>
      <li><span class="kind">Podcast</span><h3>Interviews with Interesting People</h3><a href="https://theblackdragon.podbean.com/">Listen</a></li>
      <li><span class="kind">Podcast</span><h3>NAAFI Break &middot; &ldquo;A boy from Croydon&rdquo;</h3><a href="{NAAFI}">Listen</a></li>
    </ul>
    <p class="placeholder" style="margin-top:var(--s-6)"><b>To confirm</b>The book, YouTube and Substack match the current site. The two podcasts come from older pages and public listings: keep them or drop them.</p>
  </div>
</section>

<section class="tint">
  <div class="container split">
    <div>
      <span class="label">Speaking</span>
      <h2>Have Angus on your stage or show</h2>
      <p>Resilience, leadership under pressure, endurance, curiosity and meaning, and the story behind <em>SISU</em>.</p>
    </div>
    <div class="btnrow" style="margin-top:0"><a class="btn btn--primary" href="contact.html">Get in touch</a></div>
  </div>
</section>
""")

P["contact.html"] = page("contact.html",
 "Book a discovery call - Black Dragon Enterprises",
 "A free 20-minute discovery call with Angus Peacock. No pitch, no pressure.",
 f"""
<section class="hero dark">
  <div class="container">
    <span class="label">Discovery call</span>
    <h1 class="display">Book your <em>discovery call</em></h1>
    <p class="lede">Angus doesn't take every client. He works with people he can genuinely help. This is a 20-minute conversation: no pitch, no pressure, just an honest assessment of whether there's a fit.</p>
  </div>
</section>

<section id="book">
  <div class="container split">
    <div>
      <span class="label">What happens in the call</span>
      <h2>Discovery &middot; free, 20 minutes</h2>
      <ul>
        <li>Angus will ask questions.</li>
        <li>You'll be heard, not sold to.</li>
        <li>At the end you choose how to move forward.</li>
      </ul>
      <div class="bookcard">
        <img src="assets/img/photos/pine.jpg" alt="" width="565" height="984" loading="lazy">
        <div>
          <h3>Discovery</h3>
          <p class="mute">Free 20-minute discovery call</p>
          <a class="btn btn--primary" href="{BOOK}">Book now</a>
        </div>
      </div>
      <p class="mute" style="font-size:14px;margin-top:var(--s-3)">Replaces the Wix Bookings "Discovery" service with the Google Calendar booking page Angus already uses in the SISU app.</p>
    </div>
    <div>
      <span class="label">Message</span>
      <h2>Or send a note</h2>
      <form class="form" action="#" method="post" onsubmit="return false">
        <div class="field"><label for="name">Name</label><input id="name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="topic">I'm interested in</label>
          <select id="topic" name="topic"><option>The SISU Way 1:1 coaching</option><option>Group &amp; team coaching</option><option>The ABC Movement Programme</option><option>Speaking &amp; keynotes</option><option>Curriculum design &amp; expedition learning</option><option>Something else</option></select></div>
        <div class="field"><label for="msg">Message</label><textarea id="msg" name="message" required></textarea><p class="hint">Where you are, where you want to be.</p></div>
        <div><button class="btn btn--primary" type="submit">Send message</button></div>
      </form>
      <p class="placeholder" style="margin-top:var(--s-5)"><b>New</b>The current site has no contact form, only email and LinkedIn. This one is optional and not connected; at build it would email Angus through a form service.</p>
      <p style="margin-top:var(--s-5)">Or email <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="{LINKEDIN}">LinkedIn</a></p>
    </div>
  </div>
</section>
""")

for name, html in P.items():
    (ROOT / name).write_text(html)
    print("wrote", name, len(html))

# ---------------------------------------------------------------- specimen
spec_ = importlib.util.spec_from_file_location("c", str(pathlib.Path(__file__).with_name("contrast_lib.py")))
C = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(C)
TOK = {
 "ivory":("#F5F1E8","Page field."),
 "stone":("#E6DFD1","Tint sections. Cards sit on ivory inside it."),
 "ink":("#1F1E1C","Body text and headings on light."),
 "obsidian":("#131315","The black of Black Dragon. Hero, dark sections, footer, concept bar."),
 "cinnabar":("#A3262A","The seal. Brand color, primary buttons on light, links, rules."),
 "cinnabar-deep":("#7A1A1D","Hover and pressed state for cinnabar."),
 "brass":("#C39A4B","Accent on obsidian only: labels, italics, primary buttons on dark, the pearl."),
 "ash":("#5F5A52","Secondary text on ivory and stone only."),
}
OK=[("ink","ivory"),("ink","stone"),("cinnabar","ivory"),("cinnabar","stone"),("ivory","cinnabar"),("ivory","cinnabar-deep"),("cinnabar-deep","ivory"),("ivory","obsidian"),("stone","obsidian"),("brass","obsidian"),("obsidian","brass"),("ash","ivory"),("ash","stone")]
BAD=[("brass","ivory","Never. Brass lives on obsidian only."),("brass","stone","Never."),("ivory","brass","Never. Brass buttons take obsidian text."),("cinnabar","obsidian","Never as text. The seal sits on obsidian as a filled shape only."),("ash","obsidian","Never. Muted text on dark uses stone.")]
def row(fg,bg,note=None):
    r=C.cr(TOK[fg][0],TOK[bg][0])
    s=f'<span class="pairbox" style="color:{TOK[fg][0]};background:{TOK[bg][0]}">Dragon</span>'
    if note: return f"<tr><td>{s}</td><td><code>--{fg}</code></td><td><code>--{bg}</code></td><td class='ratio fail'>{r:.2f}</td><td>{note}</td></tr>"
    aa="pass" if r>=4.5 else "large only"; aaa="pass" if r>=7 else "&mdash;"
    return f"<tr><td>{s}</td><td><code>--{fg}</code></td><td><code>--{bg}</code></td><td class='ratio'>{r:.2f}</td><td class='pass'>{aa}</td><td>{aaa}</td></tr>"
sw="".join(f'<div class="sw"><div class="chip" style="background:{v[0]}"></div><div class="meta"><code>--{k}</code> {v[0]}<span class="src">{v[1]}</span></div></div>' for k,v in TOK.items())

STYLE="""
<style>
.swatches{display:grid;gap:var(--s-4);grid-template-columns:repeat(auto-fill,minmax(200px,1fr));margin-top:var(--s-6)}
.sw{border:var(--hair);background:var(--ivory)}
.sw .chip{height:96px;border-bottom:var(--hair)}
.sw .meta{padding:var(--s-3) var(--s-4) var(--s-4);font-size:14px;line-height:1.5}
.sw code{font-weight:800}
.sw .src{display:block;margin-top:var(--s-1);color:var(--ash);font-size:13px}
.table-wrap{overflow-x:auto;margin-top:var(--s-5)}
table{width:100%;border-collapse:collapse;font-size:15px;min-width:560px}
th,td{text-align:left;padding:var(--s-3) var(--s-3) var(--s-3) 0;border-bottom:var(--hair);vertical-align:middle}
th{font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.ratio{font-variant-numeric:tabular-nums}.pass{font-weight:700}.fail{font-weight:800;color:var(--cinnabar-deep)}
.pairbox{display:inline-block;padding:2px var(--s-3);font-family:var(--font-display);font-size:18px;font-weight:600;border:1px solid rgba(0,0,0,.08)}
.spec{border-bottom:var(--hair);padding:var(--s-5) 0;display:grid;gap:var(--s-2) var(--s-5);grid-template-columns:1fr}
@media (min-width:720px){.spec{grid-template-columns:210px 1fr;align-items:baseline}}
.spec__meta{font-size:13px;color:var(--ash)}
.spec__sample{min-width:0;overflow-wrap:break-word}
.logo-row{display:flex;flex-wrap:wrap;gap:var(--s-5);align-items:center;margin-top:var(--s-5)}
.logo-tile{padding:var(--s-6);display:flex;align-items:center;justify-content:center;min-width:180px}
</style>"""

BODY=f"""
<section class="hero dark">
  <div class="container">
    <span class="label">Brand system &middot; v0.1 proposal</span>
    <h1 class="display">Black Dragon <em>style guide</em></h1>
    <p class="lede">Palette, type, seal, motif and components for blackdragonenterprises.com. Proposed by Summit Software Solutions; nothing here is final until Angus signs it off.</p>
  </div>
</section>

<section>
  <div class="container">
    <span class="label">Idea</span>
    <h2>Lacquer, brass and a seal</h2>
    <p class="lede">A dragon, a Royal Navy career and fluent Mandarin. The palette is black lacquer and ivory paper, signed once with a cinnabar seal, with naval brass as the only metal. It should feel like an executive coach's study, not a martial-arts school.</p>
  </div>
</section>

<section class="tint">
  <div class="container">
    <span class="label">Color</span>
    <h2>Palette</h2>
    <div class="swatches">{sw}</div>
  </div>
</section>

<section>
  <div class="container">
    <span class="label">Accessibility</span>
    <h2>Every pair in use passes WCAG AA</h2>
    <p>Ratios computed from WCAG 2.1 relative luminance. AA needs 4.5:1 for body text, 3:1 for large text.</p>
    <div class="table-wrap"><table><thead><tr><th>Sample</th><th>Text</th><th>Background</th><th>Ratio</th><th>AA</th><th>AAA</th></tr></thead><tbody>{"".join(row(a,b) for a,b in OK)}</tbody></table></div>
    <h3 style="margin-top:var(--s-8)">Forbidden pairs</h3>
    <div class="table-wrap"><table><thead><tr><th>Sample</th><th>Text</th><th>Background</th><th>Ratio</th><th>Rule</th></tr></thead><tbody>{"".join(row(a,b,n) for a,b,n in BAD)}</tbody></table></div>
  </div>
</section>

<section class="tint">
  <div class="container">
    <span class="label">Type</span>
    <h2>Cormorant Garamond &amp; Manrope</h2>
    <p>A high-contrast Garamond for headings: considered, a little formal, with an italic that carries emphasis. A clean, open sans for everything you read and click.</p>
    <div class="spec"><div class="spec__meta">Display &middot; Cormorant Garamond 500 &middot; clamp(48&ndash;96px)</div><div class="spec__sample display" style="margin:0">Find what you <em style="color:var(--cinnabar)">didn't know</em> you had.</div></div>
    <div class="spec"><div class="spec__meta">H1 &middot; Cormorant 500 &middot; clamp(42&ndash;72px)</div><div class="spec__sample"><h1 style="margin:0">Coaching and consulting</h1></div></div>
    <div class="spec"><div class="spec__meta">H2 &middot; Cormorant 500 &middot; clamp(32&ndash;52px)</div><div class="spec__sample"><h2 style="margin:0">Four ways to work together</h2></div></div>
    <div class="spec"><div class="spec__meta">H3 &middot; Cormorant 600 &middot; clamp(23&ndash;30px)</div><div class="spec__sample"><h3 style="margin:0">Leadership development</h3></div></div>
    <div class="spec"><div class="spec__meta">Label &middot; Manrope 700 &middot; 13px &middot; 0.2em &middot; with rule</div><div class="spec__sample"><span class="label" style="margin:0">Services</span></div></div>
    <div class="spec"><div class="spec__meta">Lede &middot; Manrope 400 &middot; clamp(17&ndash;21px) / 1.6</div><div class="spec__sample"><p class="lede" style="margin:0">For individuals, teams and organizations that want a higher standard and the habits to hold it.</p></div></div>
    <div class="spec"><div class="spec__meta">Body &middot; Manrope 400 &middot; 17px (16px mobile) / 1.7</div><div class="spec__sample"><p style="margin:0">Regular sessions, honest feedback, and accountability between them.</p></div></div>
    <div class="spec"><div class="spec__meta">Quote &middot; Cormorant italic 500</div><div class="spec__sample"><figure class="quote" style="margin:0"><p style="margin:0">&ldquo;Seeing deep into a person's potential.&rdquo;</p></figure></div></div>
  </div>
</section>

<section>
  <div class="container">
    <span class="label">Mark</span>
    <h2>The seal</h2>
    <p>A cinnabar seal, like the red chop that signs a Chinese painting, holding a dragon reaching for the brass pearl. In Chinese art the dragon pursues the pearl of wisdom: a coach's job in one image. Drawn for the concept; a designer should refine it.</p>
    <div class="logo-row">
      <div class="logo-tile" style="background:var(--ivory);border:var(--hair)"><img src="assets/img/seal.svg" alt="Black Dragon seal on ivory" width="120" height="120"></div>
      <div class="logo-tile" style="background:var(--obsidian)"><span class="wordmark" style="color:var(--ivory)">{WORDMARK}</span></div>
      <div class="logo-tile" style="background:var(--ivory);border:var(--hair)"><span class="wordmark">{WORDMARK}</span></div>
    </div>
    <ul style="margin-top:var(--s-5);max-width:64ch">
      <li>Minimum 24px for the seal, 150px wide for the lockup.</li>
      <li>Clear space equal to the seal's inner border inset on every side.</li>
      <li>The seal is always cinnabar with ivory line work and a brass pearl. Never outline it, never place it on cinnabar.</li>
      <li>Option to discuss with Angus: 黑龍 ("black dragon") inside the seal in place of the drawing, if he wants the Chinese name to carry the mark.</li>
    </ul>
  </div>
</section>

<section class="dark">
  <div class="container">
    <span class="label">Motif</span>
    <h2>Scales and the seal rule</h2>
    <p class="lede">A faint brass scale pattern (7% opacity) sits at the edge of dark heroes. Section breaks use a brass hairline with a cinnabar diamond at its centre.</p>
    <div class="rule" role="presentation"><span></span></div>
  </div>
</section>

<section>
  <div class="container">
    <span class="label">Components</span>
    <h2>Buttons</h2>
    <div class="btnrow"><a class="btn btn--primary" href="#">Book a discovery call</a><a class="btn btn--secondary" href="#">Work with Angus</a></div>
    <div class="dark" style="padding:var(--s-6);margin-top:var(--s-5)"><div class="btnrow" style="margin:0"><a class="btn btn--primary" href="#">Primary on dark</a><a class="btn btn--secondary" href="#">Secondary on dark</a></div></div>
    <p class="mute" style="margin-top:var(--s-4)">Primary is cinnabar with ivory text on light, brass with obsidian text on dark. 2px radius, 48px minimum height, uppercase Manrope 700 at 14px with 0.12em tracking.</p>
    <h2 style="margin-top:var(--s-8)">Service card</h2>
    <div class="grid grid--3"><article class="service"><span class="service__num">i.</span><h3>Coaching</h3><p>Cinnabar top rule, Cormorant italic numeral, no shadow.</p></article><article class="service"><span class="service__num">ii.</span><h3>Leadership</h3><p>Ivory card; on stone sections it stays ivory.</p></article><article class="service"><span class="service__num">iii.</span><h3>Performance</h3><p>Body text in Manrope 16px.</p></article></div>
    <h2 style="margin-top:var(--s-8)">Form field</h2>
    <div class="form"><div class="field"><label for="demo">Email</label><input id="demo" type="email" placeholder="you@example.com"><p class="hint">Labels are small caps in Manrope 800; inputs are 48px tall.</p></div></div>
    <h2 style="margin-top:var(--s-8)">Placeholder marker</h2>
    <p class="placeholder"><b>Placeholder</b>Every piece of unconfirmed content on the concept carries this marker.</p>
  </div>
</section>

<section class="tint">
  <div class="container split">
    <div>
      <span class="label">Voice</span>
      <h2>Direct, warm, earned</h2>
      <p>Write like a senior officer who is also a good listener: plain words, short sentences, confidence without swagger. Talk about the client's outcome before Angus's credentials.</p>
    </div>
    <ul class="facts">
      <li><b>Say</b>Find what you didn't know you had. Start with a conversation.</li>
      <li><b>Don't say</b>Unleash your inner dragon. Dominate. Warrior mindset.</li>
      <li><b>Always</b>Lead with the person being coached, not the coach.</li>
    </ul>
  </div>
</section>
"""
(ROOT/"specimen.html").write_text(page("specimen.html","Brand system - Black Dragon Enterprises","Palette, typography, seal, motif and components for Black Dragon Enterprises.",BODY,STYLE))
print("wrote specimen.html")

(ROOT / "404.html").write_text(page("404.html","Page not found - Black Dragon Enterprises","This page does not exist.","""
<section class="hero dark">
  <div class="container">
    <span class="label">404</span>
    <h1 class="display">This page has <em>moved on</em>.</h1>
    <p class="lede">If you followed a link from the old site, the page you want is probably under About, Testimonials or Media now.</p>
    <div class="btnrow"><a class="btn btn--primary" href="index.html">Back to home</a><a class="btn btn--secondary" href="contact.html">Contact Angus</a></div>
  </div>
</section>
""").replace('href="','href="__').replace('href="__http','href="http').replace('href="__mailto','href="mailto').replace('href="__#','href="#').replace('href="__','href="/blackdragonenterprises/').replace('src="assets/','src="/blackdragonenterprises/assets/'))
print("wrote 404.html")


# ---------------------------------------------------------------- launch files
PAGES = ['index.html', 'services.html', 'about.html', 'testimonials.html', 'media.html', 'contact.html']
if PROD:
    _p = ROOT / "404.html"; _p.write_text(_p.read_text().replace('"/blackdragonenterprises/', '"/'))
    _m = ROOT / "site.webmanifest"; _m.write_text(_m.read_text().replace('"/blackdragonenterprises/', '"/'))
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{BASE}{'' if p == 'index.html' else p.replace('.html', '')}</loc></url>\n" for p in PAGES) + "</urlset>\n")
    print("wrote production robots.txt and sitemap.xml")
else:
    (ROOT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
