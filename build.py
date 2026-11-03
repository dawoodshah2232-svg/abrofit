#!/usr/bin/env python3
"""Build ABROFIT site on the LARGAMS FITNESS theme (copied CSS/JS, green accent).
Run: python3 build2.py — writes the 11 HTML pages. CSS/JS live in assets/ and are
NOT generated here: style.css is the Largams stylesheet with gold->green, app.js
is the Largams script with the enquiry greeting changed to ABROFIT."""
import pathlib

WA = "https://wa.me/918137008663"
WA_JOIN = WA + "?text=Hi%20ABROFIT%2C%20I%20would%20like%20a%20free%20consultation.%20Please%20share%20the%20details."
WA_TRIAL = WA + "?text=Hi%20ABROFIT%2C%20I%20would%20like%20to%20try%20the%20one-day%20free%20trial."
WA_ABRO = WA + "?text=Hi%20ABROFIT%2C%20I%20am%20interested%20in%20your%20online%20fitness%20coaching%20programs.%20Please%20share%20the%20details."
WA_30 = WA + "?text=Hi%20ABROFIT%2C%20I%20would%20like%20to%20know%20more%20about%20your%2030-Day%20Online%20Fitness%20Program."
WA_90 = WA + "?text=Hi%20ABROFIT%2C%20I%20would%20like%20to%20know%20more%20about%20your%2090-Day%20Transformation%20Challenge."
IG_ABRO = "https://www.instagram.com/abrofitbylf"
IG_LARG = "https://www.instagram.com/largamsfitness"
WA_MSG = "https://wa.me/message/2R23YX4M53E4C1"
LARG_SITE = "https://dawoodshah2232-svg.github.io/largams-fitness/"
PAGES = "https://dawoodshah2232-svg.github.io/abrofit/"

NAV = [
    ("index.html", "Home", None),
    ("about.html", "About", None),
    ("how-it-works.html", "Coaching", [("how-it-works.html", "How It Works"), ("programs.html", "Programs"), ("a-day.html", "A Day With ABROFIT")]),
    ("why-it-matters.html", "Why ABROFIT", [("why-it-matters.html", "Why It Matters"), ("comparison.html", "Comparison"), ("value.html", "Value")]),
    ("faq.html", "FAQ", None),
    ("calculator.html", "BMI Calculator", None),
    ("contact.html", "Contact", None),
]

def nav_html(active):
    out = []
    for href, label, drop in NAV:
        if drop:
            items = "".join(f'<a href="{h}"{" class=\"active\" aria-current=\"page\"" if h == active else ""}>{l}</a>' for h, l in drop)
            cur = " active" if any(h == active for h, _ in drop) else ""
            out.append(f'<div class="drop"><a aria-haspopup="true" href="{href}" class="{cur.strip()}">{label} <span class="caret" aria-hidden="true">\u25be</span></a><button class="drop-toggle" type="button" aria-expanded="false" aria-label="Show {label} submenu">\u25be</button><div class="drop-menu">{items}</div></div>')
        else:
            out.append(f'<a href="{href}"{" class=\"active\" aria-current=\"page\"" if href == active else ""}>{label}</a>')
    out.append(f'<a class="btn small" href="{WA_JOIN}">Free Consultation</a>')
    return "".join(out)

def head(title, desc, fname, ogimg="assets/images/hero.webp"):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | ABROFIT by LARGAMS FITNESS</title><meta name="description" content="{desc}">
<link rel="canonical" href="{PAGES}{fname}"><meta property="og:title" content="{title} — ABROFIT"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{PAGES}{fname}"><meta property="og:image" content="{PAGES}{ogimg}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&display=swap" rel="stylesheet"><link rel="icon" type="image/png" href="assets/logo-abrofit.png"><link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"ABROFIT","url":"{PAGES}","parentOrganization":{{"@type":"Organization","name":"LARGAMS FITNESS","url":"{LARG_SITE}"}},"sameAs":["{IG_ABRO}","{IG_LARG}"],"description":"ABROFIT is the online fitness division of LARGAMS FITNESS: personalized online coaching, workout plans and diet plans for people worldwide."}}</script></head>"""

def header(active):
    return f"""<body><a class="skip" href="#main">Skip to content</a><div class="spotlight" aria-hidden="true"></div>
<header class="site-header"><div class="parent-strip"><div class="wrap">ABROFIT &mdash; by LARGAMS FITNESS</div></div><div class="wrap nav-inner"><a class="logo" href="index.html"><img class="site-logo" src="assets/logo-abrofit.png" alt="ABROFIT — by LARGAMS FITNESS"></a><button class="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button><nav class="main-nav">{nav_html(active)}</nav></div></header>"""

FOOTER = f"""<footer><div class="wrap"><div class="foot-grid"><div><img class="footer-logo" src="assets/logo-abrofit.png" alt="ABROFIT logo"><h4>ABROFIT</h4><ul><li><a href="about.html">About ABROFIT</a></li><li><a href="programs.html">Online Coaching</a></li><li><a href="programs.html">30-Day Program</a></li><li><a href="programs.html">90-Day Challenge</a></li></ul></div><div><h4>LARGAMS FITNESS</h4><ul><li><a href="{LARG_SITE}">Parent Company</a></li><li><a href="{LARG_SITE}gym.html">The Gym</a></li><li><a href="{LARG_SITE}about.html">About LARGAMS</a></li><li><a href="{LARG_SITE}">Visit LARGAMS Site</a></li></ul></div><div><h4>Quick Links</h4><ul><li><a href="index.html">Home</a></li><li><a href="programs.html">Programs</a></li><li><a href="how-it-works.html">How It Works</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact</a></li></ul></div><div><h4>More</h4><ul><li><a href="calculator.html">BMI Calculator</a></li><li><a href="a-day.html">A Day With ABROFIT</a></li><li><a href="comparison.html">Comparison</a></li><li><a href="value.html">Value</a></li></ul></div><div><h4>Social Media</h4><ul><li><a href="{IG_ABRO}">ABROFIT Instagram</a></li><li><a href="{IG_LARG}">LARGAMS FITNESS Instagram</a></li><li><a href="{WA_MSG}">WhatsApp Message Link</a></li></ul></div></div><div class="foot-bottom"><p>&copy; <span id="year">2026</span> ABROFIT. ALL RIGHTS RESERVED.<br>ABROFIT &mdash; The Online Fitness Division of LARGAMS FITNESS. Prices on enquiry unless stated as free. Results vary by person and consistency.</p></div></div></footer>
<a class="wa-float" href="{WA_JOIN}"><span>WhatsApp Us</span></a>
<script src="assets/config.js"></script><script src="assets/app.js"></script></body></html>"""

def page(fname, title, desc, hero, body, ogimg="assets/images/hero.webp"):
    html = head(title, desc, fname, ogimg) + header(fname) + "<main id=\"main\">" + hero + body + "</main>" + FOOTER
    pathlib.Path(fname).write_text(html)
    print("wrote", fname, len(html))

def hero_index():
    return f"""<section class="hero"><img class="bg" src="assets/images/hero.webp" alt="Illustrative concept image: training at home abroad in the evening"><div class="wrap hero-inner"><p class="kicker">ABROFIT &mdash; by LARGAMS FITNESS</p><h1 class="hero-title">Fit Abroad. <span class="green-word">30 Minutes</span> A Day.</h1><p class="lead">Abroad? No gym? No time? No problem. A personal coach, a personalized plan, and a diet built for you &mdash; online, wherever you live.</p><div class="btns"><a class="btn" href="{WA_JOIN}">Book A Free Consultation</a><a class="btn ghost" href="programs.html">See Programs &rarr;</a></div></div></section>"""

def page_hero(kicker, title, lead, img, cta=True):
    btns = f'<div class="btns"><a class="btn" href="{WA_JOIN}">Book A Free Consultation</a><a class="btn ghost" href="programs.html">See Programs &rarr;</a></div>' if cta else ""
    return f"""<section class="page-hero"><img class="bg" src="{img}" alt="Illustrative concept image"><div class="wrap hero-inner"><p class="kicker">{kicker}</p><h1 class="hero-title">{title}</h1><p class="lead">{lead}</p>{btns}</div></section>"""

def section(kicker, h2, lead, inner="", tight=False):
    cls = "section tight" if tight else "section"
    return f'<section class="{cls}"><div class="wrap"><p class="kicker reveal">{kicker}</p><h2 class="reveal">{h2}</h2><p class="lead reveal">{lead}</p>{inner}</div></section>'

BARBELL = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6.5 6.5v11M17.5 6.5v11M3 9v6M21 9v6M6.5 12h11"/></svg>'
CHECK = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l4 4L19 6"/></svg>'

def cards(items, icon=BARBELL):
    inner = "".join(f'<div class="card reveal" style="--d:.08s"><div class="card-body"><h3>{icon} {h}</h3><p>{p}</p></div></div>' for h, p in items)
    return f'<div class="grid three" style="margin-top:28px">{inner}</div>'

def split(img, alt, h3, text, cta_text, cta_href):
    return f'<div class="split reveal"><div class="media"><img loading="lazy" src="{img}" alt="{alt}"></div><div class="split-body"><h3>{h3}</h3><p>{text}</p><p><a class="btn" href="{cta_href}">{cta_text}</a></p></div></div>'

def insta():
    return f"""<div class="insta-grid"><a class="insta-card reveal" href="{IG_ABRO}"><img class="insta-brand-abro" src="assets/logo-abrofit.png" alt="ABROFIT logo"><div class="insta-text"><span class="insta-tag">Official account &middot; Online coaching</span><span class="insta-name">ABROFIT</span><span class="insta-handle">@abrofitbylf</span></div><span class="insta-cta">Follow <span class="insta-arrow">&nearr;</span></span><span class="insta-watermark" aria-hidden="true">@</span></a>
<a class="insta-card insta-silver reveal" style="--d:.08s" href="{IG_LARG}"><img class="insta-brand" src="assets/logo-largams-dark.png" alt="LARGAMS FITNESS logo"><div class="insta-text"><span class="insta-tag">Official account &middot; Gym</span><span class="insta-name">LARGAMS FITNESS</span><span class="insta-handle">@largamsfitness</span></div><span class="insta-cta">Follow <span class="insta-arrow">&nearr;</span></span><span class="insta-watermark" aria-hidden="true">@</span></a></div>"""

NOTE = '<p class="small reveal" style="margin-top:16px">General fitness information only &mdash; not medical advice. If you have a health condition, speak to a qualified professional before starting a new training or diet plan. Results vary by person and consistency.</p>'
CTA = f'<p class="reveal" style="margin-top:28px"><a class="btn" href="{WA_JOIN}">Book A Free Consultation</a> <a class="btn ghost" href="programs.html">See Programs</a></p>'

STAT_SVGS = [
    '<svg class="ic-badge-svg" viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path stroke="#8DE32C" d="M12 3l7 2.5v5c0 4.2-3 7.2-7 9.5-4-2.3-7-5.3-7-9.5v-5z"/><path stroke="#FFFFFF" d="M12 8l3.2 1.2v2.6c0 2-1.4 3.4-3.2 4.4-1.8-1-3.2-2.4-3.2-4.4V9.2z"/></svg>',
    '<svg class="ic-badge-svg" viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path stroke="#8DE32C" d="M4 20v-5h5v-3h5V8h6v12H4z"/><path stroke="#FFFFFF" d="M4 20h16"/></svg>',
    '<svg class="ic-badge-svg" viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect stroke="#8DE32C" x="4" y="4" width="7" height="7" rx="1"/><rect stroke="#FFFFFF" x="13" y="4" width="7" height="7" rx="1"/><rect stroke="#FFFFFF" x="4" y="13" width="7" height="7" rx="1"/><rect stroke="#8DE32C" x="13" y="13" width="7" height="7" rx="1"/></svg>',
    '<svg class="ic-badge-svg" viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle stroke="#8DE32C" cx="12" cy="12" r="9" fill="none"/><path stroke="#FFFFFF" d="M3 12h18"/><path stroke="#FFFFFF" d="M12 3c2.5 2.5 2.5 15.5 0 18-2.5-2.5-2.5-15.5 0-18z"/></svg>',
]
def stats():
    items = [(30, "Minutes A Day"), (6, "How It Works Steps"), (3, "Core Programs"), (2, "Free Ways To Start")]
    inner = "".join(f'<div class="stat"><div class="stat-icon" aria-hidden="true">{STAT_SVGS[i]}</div><b><span data-count="{n}">00</span></b><span class="stat-rule" aria-hidden="true"></span><span>{label}</span></div>' for i, (n, label) in enumerate(items))
    return f'<div class="stats" style="margin-top:32px">{inner}</div>'

# ---------------- INDEX (Largams homepage order) ----------------
body = section("The Brand", "ABROFIT &mdash; More Than Just A Workout.",
    "You live abroad, or your days are full, and the gym never fits. ABROFIT brings the coach, the plan, and the diet to your home &mdash; in 30 minutes a day, guided daily by a professional coach.",
    stats())
body += section("Two Brands, One Standard", "Online Coaching. Parent Company.",
    "ABROFIT is the online division. LARGAMS FITNESS is the main company behind it &mdash; the physical gym brand that ABROFIT grows out of.",
    f'<div class="grid two" style="margin-top:28px"><div class="card reveal"><div class="card-body"><h3>{BARBELL} A &mdash; ABROFIT Online Coaching</h3><p>Professional fitness coaching, personalized workout programs and customized diet plans &mdash; wherever you are in the world. 30 minutes a day, a coach who checks in daily, and a plan built for your life abroad.</p><p><a class="btn" href="{WA_ABRO}">Enquire About ABROFIT</a></p></div></div><div class="card reveal" style="--d:.08s"><div class="card-body"><h3>{CHECK} B &mdash; LARGAMS FITNESS, Parent Company</h3><p>The physical fitness centre behind ABROFIT &mdash; in-person training, strength, weight and cardio work, and personal training. ABROFIT is its official online division.</p><p><a class="btn ghost" href="{LARG_SITE}">Visit LARGAMS FITNESS &rarr;</a></p></div></div></div>')
body += section("Pick Your Program.", "Start Where You Are.",
    "A 30-day program to build the habit, a 90-day challenge to go further, and one-to-one coaching for the closest guidance. Every paid program is priced on enquiry.",
    cards([("30-Day Program", "Thirty days of guided training, diet, and daily check-ins. Price: On enquiry."),
           ("90-Day Transformation Challenge", "Ninety days with your coach, designed to build lasting change. Price: On enquiry. Results vary by person and consistency."),
           ("One-to-One Online Coaching", "Your own coach, your own plan, daily guidance. Price: On enquiry."),
           ("Free Consultation", "A free conversation about your life, your time, and your goal. Free."),
           ("One-Day Free Trial", "One free day to feel how ABROFIT works before you commit. Free."),
           ("Custom Diet Plans", "Eating habits are part of the plan &mdash; built around your routine and the food around you.")])
    + f'<p class="reveal" style="margin-top:24px"><a class="btn" href="programs.html">All Programs</a></p>')
body += section("Training At Your Home, Abroad.", "No Gym Needed.",
    "Train at home, in your room, or wherever you are &mdash; your plan is built for your space, your schedule, and your life abroad.",
    split("assets/images/coach-call.webp", "Illustrative concept image: online coach on a video call with a client training at home", "Your Coach, On Screen, Every Day.", "Your coach guides the session, reviews your day, and keeps the plan moving with you &mdash; no commute, no waiting for equipment, no lost hour around the workout.", "Start With A Free Consultation", WA_JOIN))
body += section("Follow Us", "On Instagram",
    "Follow the official accounts for training, updates and announcements. We do not show a live embedded feed &mdash; Instagram embedding requires official authorisation &mdash; so these links take you directly to the profiles.",
    insta(), tight=True)
page("index.html", "ABROFIT — Online Fitness Coaching", "ABROFIT by LARGAMS FITNESS: online fitness coaching for people abroad and people with no time for a gym. 30 minutes a day, a personal coach, a diet plan built for you.", hero_index(), body)

# ---------------- HOW IT WORKS ----------------
steps = [("01", "Contact", "Message ABROFIT on WhatsApp and say you want to start."),
         ("02", "Free Consultation", "A free conversation about your life, your time, and your goal."),
         ("03", "Goal Assessment", "Your coach assesses your goal and your starting point."),
         ("04", "Personalized Plan", "A workout and diet plan built for you &mdash; not a generic program."),
         ("05", "Begin Training", "Start with 30 minutes a day, guided by your coach."),
         ("06", "Track Progress", "Daily check-ins and reviews keep the plan moving with you.")]
steps_html = "".join(f'<div class="step reveal"><b class="num">{n}</b><h3>{h}</h3><p>{p}</p></div>' for n, h, p in steps)
body = section("How It Works", "Six Steps. One Coach.", "From first message to daily progress &mdash; the same six steps for every client.", f'<div class="steps" style="margin-top:28px">{steps_html}</div>')
body += section("Start Today", "Start Your Fitness Journey Today.", "A free consultation, and a one-day free trial to feel how ABROFIT works before you commit to anything.", f'<p class="reveal" style="margin-top:24px"><a class="btn" href="{WA_JOIN}">Book A Free Consultation</a> <a class="btn ghost" href="{WA_TRIAL}">Try One Day Free</a></p>' + NOTE)
page("how-it-works.html", "How It Works — ABROFIT", "ABROFIT in six steps: contact, free consultation, goal assessment, personalized plan, begin training, track progress.", page_hero("How It Works", "Six Steps. One Coach.", "From first message to daily progress.", "assets/images/coach-call.webp"), body, "assets/images/coach-call.webp")

# ---------------- PROGRAMS ----------------
def program_card(title, dur, ben, inc, aud, price, wa, wa_label="Enquire"):
    return f'<div class="card price-card reveal"><div class="card-body"><h3>{title}</h3><p class="price">Price: {price}</p><p><strong>Duration:</strong> {dur}</p><p><strong>Benefits:</strong> {ben}</p><p><strong>What&rsquo;s included:</strong> {inc}</p><p><strong>Suitable for:</strong> {aud}</p><p><a class="btn" href="{wa}">{wa_label}</a></p></div></div>'
body = section("ABROFIT Programs", "Choose Your Program.", "Every paid program is priced on enquiry &mdash; nothing is invented. Free consultation and one-day trial are the only free items.",
    f'<div class="grid three" style="margin-top:28px">'
    + program_card("30-Day Online Fitness Program", "30 days", "Build the daily habit with guided training and nutrition.", "Daily check-ins, personalized workouts, customized diet plan.", "Anyone starting or restarting fitness, abroad or short on time.", "On enquiry", WA_30)
    + program_card("90-Day Transformation Challenge", "90 days", "A full 90 days with your coach, designed to build lasting change.", "Daily guidance, personalized workouts, customized diet plan, progress reviews.", "People ready for a longer, structured commitment.", "On enquiry", WA_90)
    + program_card("One-to-One Online Coaching", "Ongoing, on enquiry", "The closest guidance &mdash; your own coach and your own plan.", "Personal coach, personalized plan, diet plan, daily check-ins.", "Anyone who wants individual attention.", "On enquiry", WA_ABRO)
    + program_card("Free Consultation", "One conversation", "Understand your goal, time and starting point &mdash; free.", "A free conversation with ABROFIT about your goal.", "Everyone, before starting.", "Free", WA_JOIN)
    + program_card("One-Day Free Trial", "One day", "Feel how ABROFIT works before you commit.", "One day of guided training under the program.", "Everyone, before starting.", "Free", WA_TRIAL)
    + program_card("Custom Diet Plans", "With any program", "Eating habits become part of the plan, not an afterthought.", "A diet plan built around your routine and the food around you.", "Anyone whose eating habits need structure.", "On enquiry", WA_ABRO)
    + '</div>')
body += section("All ABROFIT Services", "Everything Included.",
    "The services below are the real ABROFIT offering from the brief. Prices, where applicable, are on enquiry &mdash; none are invented.",
    cards([("Worldwide Online Personal Training", "Professional coaching wherever you live, with no physical gym needed."),
           ("One-to-One Online Coaching", "Your own coach, your own plan, daily guidance."),
           ("Customized Diet Plans", "Built around your routine and the food around you."),
           ("Personalized Workout Programs", "Workouts built for your goal, space and schedule."),
           ("Weight Loss Programs", "Training and nutrition structured around your goal."),
           ("Muscle Building Programs", "Progressive training built for your goal."),
           ("Body Transformation Programs", "Longer programs with daily accountability. Results vary by person and consistency."),
           ("Guidance &amp; Accountability", "Daily check-ins so the plan holds when motivation alone does not.")], icon=CHECK))
page("programs.html", "Programs — ABROFIT", "ABROFIT programs: 30-day, 90-day, one-to-one coaching, free consultation and one-day free trial. Prices on enquiry.", page_hero("Programs", "Choose Your Program.", "Online coaching, built around 30 minutes a day.", "assets/images/morning-routine.webp"), body, "assets/images/morning-routine.webp")

# ---------------- WHY IT MATTERS ----------------
body = section("Why It Matters", "Without A System, Fitness Slips.",
    "Abroad, without a gym nearby and with long work hours, fitness quietly drops off the list. ABROFIT exists so the system holds when willpower alone does not.",
    cards([("No Time", "Long work hours leave no room for a gym trip &mdash; so training never happens."),
           ("No Gym Nearby", "A new city, an unfamiliar area, no gym you trust &mdash; the barrier stays up."),
           ("Unfamiliar Food", "New food, new routines, eating habits drift &mdash; and no plan corrects them."),
           ("Routine Lost After Moving", "The routine you had at home does not survive the move abroad."),
           ("No One Watching", "With no coach and no check-ins, skipping a day becomes skipping a month.")], icon=CHECK))
body += section("The Cost Of Doing Nothing", "Small Slips, Over Time.",
    "In general wellness terms: energy dips, weight creeps up, strength and stamina slip, sleep and stress get harder &mdash; and restarting feels harder every month. This is general information, not a medical claim about any person.",
    split("assets/images/hero.webp", "Illustrative concept image: training at home abroad", "A System Holds When Willpower Does Not.", "Thirty minutes a day, a coach who checks in, and a plan that fits your life &mdash; that is the system ABROFIT gives you, so fitness does not depend on motivation alone.", "Book A Free Consultation", WA_JOIN) + NOTE)
page("why-it-matters.html", "Why It Matters — ABROFIT", "Why fitness fails abroad without a system, and what ABROFIT changes: 30 minutes a day, a coach, a plan, a diet.", page_hero("Why It Matters", "Without A System, Fitness Slips.", "Abroad, with no time and no gym nearby, fitness needs a system.", "assets/images/hero.webp"), body)

# ---------------- COMPARISON ----------------
rows = [("Personalized plan", "Yes", "No — you plan it yourself", "No", "No — generic videos"),
        ("Professional coach guiding you", "Yes — daily guidance", "Only if you hire one", "No", "No"),
        ("Diet plan built for you", "Yes", "No", "No", "No — general advice only"),
        ("Daily accountability", "Yes — daily check-ins", "No", "No", "No"),
        ("30 minutes a day", "Yes — built around 30 minutes", "Depends on you", "No training", "Varies — no structure"),
        ("Train from anywhere", "Yes — at home, abroad, anywhere", "No — you must go to the gym", "—", "Yes — but unguided"),
        ("Works around your schedule", "Yes — plan fits your day", "Only if the gym hours fit", "—", "Only if you stay consistent alone")]
trs = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in rows)
body = section("Comparison", "Compare Honestly.",
    "Features only &mdash; no invented competitor prices or claims. Other services vary; this table compares what each option typically includes as described here.",
    f'<div class="table-wrap reveal" style="margin-top:28px"><table><thead><tr><th>Feature</th><th>ABROFIT</th><th>Gym Alone</th><th>No Plan</th><th>Random Online Videos</th></tr></thead><tbody>{trs}</tbody></table></div>' + CTA + NOTE)
page("comparison.html", "Comparison — ABROFIT", "ABROFIT vs gym alone vs no plan vs random online videos: features only, no invented prices.", page_hero("Comparison", "Compare Honestly.", "What each option actually includes &mdash; features only.", "assets/images/morning-routine.webp"), body, "assets/images/morning-routine.webp")

# ---------------- VALUE ----------------
body = section("Value", "What You Get, In One Place.",
    "Coach, plan, diet and daily check-ins &mdash; together, instead of pieced together from videos, apps and guesswork.",
    cards([("A Personal Coach", "A professional coach guides you and reviews your day."),
           ("A Personalized Plan", "Workouts built for your goal, space and schedule."),
           ("A Custom Diet Plan", "Eating habits built into the plan, not left to chance."),
           ("Daily Check-Ins", "Accountability every day, so the plan keeps moving.")], icon=CHECK))
body += section("Time Saved", "No Commute. No Waiting.",
    "No travel to a gym, no waiting for equipment, no lost hour around the workout. Thirty minutes, at home, done.",
    split("assets/images/healthy-meal.webp", "Illustrative concept image: healthy meal prep", "Your Meals, Planned Too.", "A diet plan built around your routine and the food around you &mdash; so eating supports training instead of undoing it.", "See Programs", "programs.html") + CTA + NOTE)
page("value.html", "Value — ABROFIT", "ABROFIT value: coach, plan, diet and daily check-ins in one place, 30 minutes a day, no commute.", page_hero("Value", "What You Get, In One Place.", "Coach, plan, diet and daily check-ins &mdash; together.", "assets/images/healthy-meal.webp"), body, "assets/images/healthy-meal.webp")

# ---------------- A DAY ----------------
day = [("01", "Morning Check-In", "Your coach checks in. The day's plan is clear before work starts."),
       ("02", "30-Minute Workout", "One focused session, at home, guided by your coach."),
       ("03", "Meals Per Plan", "Eat from your diet plan &mdash; built around your routine and the food around you."),
       ("04", "Evening Coach Review", "Your coach reviews the day and adjusts what needs adjusting."),
       ("05", "Ready For Tomorrow", "The habit builds day by day &mdash; not on motivation alone.")]
day_html = "".join(f'<div class="step reveal"><b class="num">{n}</b><h3>{h}</h3><p>{p}</p></div>' for n, h, p in day)
body = section("A Day With ABROFIT", "An Example Day.",
    "Morning check-in, a 30-minute workout, meals from your plan, and an evening coach review. This is an example &mdash; your plan is personalized.",
    f'<div class="steps" style="margin-top:28px">{day_html}</div>')
body += section("Your Morning", "Start The Day Right.",
    "A morning routine that fits your life abroad &mdash; stretch, check in, train, and get on with the day.",
    split("assets/images/morning-routine.webp", "Illustrative concept image: morning stretch at home", "Thirty Minutes, Then On With Your Day.", "The workout is short on purpose: it is the part most people can actually keep, every day.", "Book A Free Consultation", WA_JOIN))
page("a-day.html", "A Day With ABROFIT", "An example day with ABROFIT: morning check-in, 30-minute workout, meals per plan, evening coach review.", page_hero("A Day With ABROFIT", "An Example Day.", "Morning check-in to evening review &mdash; your plan, personalized.", "assets/images/morning-routine.webp"), body, "assets/images/morning-routine.webp")

# ---------------- FAQ ----------------
FAQS = [("Can I join ABROFIT from abroad?", "Yes &mdash; ABROFIT is designed for people worldwide, whether in India or anywhere across the globe, with no need for a physical gym."),
        ("I have no gym. Can I still train?", "Yes. Your plan is built for your space &mdash; train at home, in your room, or wherever you are."),
        ("Is 30 minutes a day enough?", "Thirty minutes is the promise because it is the part most people can actually keep. A short session done every day beats a long plan abandoned in week two. Your coach builds the session around your goal."),
        ("Who guides me?", "A professional coach &mdash; your personal coach guides you, reviews your day, and keeps you on track with daily check-ins."),
        ("What about my food and eating habits?", "Eating habits are part of the plan. You get a customized diet plan built around your routine and the food around you."),
        ("Do I need equipment?", "Bodyweight first. Anything else is discussed in consultation and confirmed in your plan &mdash; nothing is required to buy to start."),
        ("How do I start?", "Message ABROFIT on WhatsApp, have a free consultation, get your goal assessed, receive your plan, then begin training."),
        ("How much does it cost?", "Price: On enquiry. Please ask on WhatsApp &mdash; details to be confirmed. Free consultation and one-day free trial are free."),
        ("Will I transform in 30 days?", "The 30-day program is designed to help you build the habit and follow a plan for 30 days. Results vary by person and consistency &mdash; no transformation is guaranteed.")]
faqs_html = "".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS)
body = section("FAQ", "Questions, Answered.",
    "Where a detail is not yet confirmed, the answer says so and points to WhatsApp &mdash; nothing is invented. Questions about the physical gym are answered on the LARGAMS FITNESS site.",
    faqs_html + CTA + NOTE)
page("faq.html", "FAQ — ABROFIT", "ABROFIT FAQ: abroad, no gym, 30 minutes, coach, diet, equipment, cost, 30-day program.", page_hero("FAQ", "Questions, Answered.", "Abroad, no gym, 30 minutes &mdash; answered honestly.", "assets/images/coach-call.webp"), body, "assets/images/coach-call.webp")

# ---------------- CALCULATOR ----------------
body = section("Tools — BMI Calculator", "Know Your Starting Point.",
    "One number, honestly explained &mdash; then a plan built around you, not just the number.",
    """<div class="card reveal" style="margin-top:28px"><div class="card-body"><form id="bmi-form">
<label for="bmi-height">Height (cm) *</label><input id="bmi-height" type="number" min="50" max="250" step="1" required placeholder="e.g. 175">
<label for="bmi-weight">Weight (kg) *</label><input id="bmi-weight" type="number" min="20" max="400" step="0.1" required placeholder="e.g. 78">
<p><button class="btn" type="submit">Calculate My BMI</button></p>
</form><div id="bmi-result" class="calc-result" aria-live="polite"><p>Your result will appear here.</p></div></div></div>""")
body += section("What BMI Does — And Doesn't — Tell You", "A Starting Point, Not A Verdict.",
    "BMI is a simple screening number. It does not measure muscle, body fat, fitness or health on its own &mdash; a muscular athlete and a sedentary person can share the same BMI. Use it as a starting point, then talk to a coach about training, nutrition, sleep and habits. That is what the free ABROFIT consultation is for.",
    CTA + '<p class="small reveal" style="margin-top:16px">Disclaimer: this calculator gives general information only and is not medical advice. If you have a health condition, speak to a qualified professional before starting a new training or diet plan.</p>')
page("calculator.html", "BMI Calculator — ABROFIT", "ABROFIT BMI calculator: know your starting point, honestly explained, then a plan built around you.", page_hero("Tools — BMI Calculator", "Know Your Starting Point.", "One number, honestly explained.", "assets/images/hero.webp", cta=False), body)

# ---------------- ABOUT ----------------
body = section("Brand Story", "ABROFIT — Fitness Without Boundaries.",
    "ABROFIT is the online fitness division of LARGAMS FITNESS, created to make professional fitness coaching accessible to people worldwide. Whether you live in India or anywhere across the globe, ABROFIT brings personalized workout programs, customized diet plans and professional online fitness coaching directly to you. Our goal is to make fitness accessible to everyone, regardless of their location, lifestyle or access to a physical gym.")
body += section("Vision & Mission", "Fitness For Everyone, Everywhere.",
    "Vision: a world where living abroad or having no time for a gym never means giving up on fitness. Mission: give every client a coach, a plan and a diet that fit their real life &mdash; in 30 minutes a day.")
body += section("Philosophy & Approach", "Consistency Over Intensity.",
    "Fitness is a lifestyle built through consistency, professional guidance and dedication &mdash; not through one extreme week. ABROFIT builds the habit day by day: a short session done every day, meals planned, and a coach who checks in.")
body += section("Commitment", "We Do Not Invent Results.",
    "No trainer, testimonial, transformation photo or success rate is invented on this site. Prices are on enquiry until supplied, and results are always described as varying by person and consistency.")
body += section("Parent Company", "A Product Of LARGAMS FITNESS.",
    "LARGAMS FITNESS is the main company behind ABROFIT &mdash; the physical fitness centre whose training standard ABROFIT carries online.",
    f'<div class="card reveal" style="margin-top:28px"><div class="card-body"><img class="parent-logo" src="assets/logo-largams-dark.png" alt="LARGAMS FITNESS logo"><p>LARGAMS FITNESS &mdash; the main company. ABROFIT is its official online fitness division. <a href="{LARG_SITE}">Visit the LARGAMS FITNESS website &rarr;</a></p></div></div>')
body += section("Future Goals", "Growing, Step By Step.",
    "Future goals &mdash; including additional programs and online services &mdash; are editable placeholders to be confirmed by the brand. Future features (payments, logins, dashboards, booking, store) are Phase 2 and are not presented as live anywhere on this site.")
page("about.html", "About — ABROFIT", "About ABROFIT: the online fitness division of LARGAMS FITNESS, its story, vision, mission and parent company.", page_hero("About ABROFIT", "Fitness Without Boundaries.", "Professional coaching, personalized plans, customized nutrition &mdash; wherever you are.", "assets/images/coach-call.webp"), body, "assets/images/coach-call.webp")

# ---------------- CONTACT ----------------
body = section("Contact", "Start The Conversation.",
    "Tell us your goal and your situation &mdash; abroad, no time, no gym &mdash; and ABROFIT will reply on WhatsApp. This form opens WhatsApp with your message; nothing is stored on this site.",
    f"""<div class="grid two" style="margin-top:28px"><div class="card reveal"><div class="card-body"><form id="enquiry-form">
<label for="f-name">Full name *</label><input id="f-name" required autocomplete="name">
<label for="f-phone">Phone number *</label><input id="f-phone" required type="tel" autocomplete="tel">
<label for="f-email">Email address *</label><input id="f-email" required type="email" autocomplete="email">
<label for="f-country">Country *</label><input id="f-country" required autocomplete="country-name">
<label for="f-service">Service interested in *</label><select id="f-service" required><option value="">Choose a service…</option><option>ABROFIT Online Coaching</option><option>30-Day Program</option><option>90-Day Challenge</option><option>One-to-One Coaching</option><option>Free Consultation</option><option>One-Day Free Trial</option><option>General Enquiry</option></select>
<label for="f-message">Message *</label><textarea id="f-message" rows="5" required></textarea>
<p><button class="btn" type="submit">Submit Enquiry via WhatsApp</button></p>
</form></div></div><div class="reveal" style="--d:.1s"><h2>Direct Contact</h2>
<p><strong>WhatsApp:</strong> <a href="{WA_JOIN}">Free Consultation on WhatsApp</a></p>
<p><strong>WhatsApp message link:</strong> <a href="{WA_MSG}">wa.me/message</a></p>
<p><strong>Instagram:</strong> <a href="{IG_ABRO}">ABROFIT @abrofitbylf</a> &middot; <a href="{IG_LARG}">LARGAMS FITNESS @largamsfitness</a></p>
<p><strong>Location:</strong> Online, worldwide &mdash; no physical gym visit needed for ABROFIT coaching. For the physical gym, see <a href="{LARG_SITE}">LARGAMS FITNESS</a>.</p>
<p><strong>Hours / email:</strong> To be confirmed &mdash; please ask on WhatsApp.</p>
<p><a class="btn" href="{WA_TRIAL}">Try One Day Free</a></p></div></div>""")
page("contact.html", "Contact — ABROFIT", "Contact ABROFIT: enquiry form via WhatsApp, Instagram, and free consultation for online fitness coaching.", page_hero("Contact", "Start The Conversation.", "Abroad, no time, no gym &mdash; tell us where you are, and we will reply.", "assets/images/hero.webp"), body)

print("done")
