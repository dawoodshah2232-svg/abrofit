#!/usr/bin/env python3
"""Build ABROFIT static site pages from a shared template. Run: python3 build.py"""
import pathlib

WA = "https://wa.me/918137008663"
WA_JOIN = WA + "?text=Hi%20ABROFIT%2C%20I%20would%20like%20a%20free%20consultation.%20Please%20share%20the%20details."
WA_TRIAL = WA + "?text=Hi%20ABROFIT%2C%20I%20would%20like%20to%20try%20the%20one-day%20free%20trial."
IG_ABRO = "https://www.instagram.com/abrofitbylf"
IG_LARG = "https://www.instagram.com/largamsfitness"
WA_MSG = "https://wa.me/message/2R23YX4M53E4C1"
LARG_SITE = "https://dawoodshah2232-svg.github.io/largams-fitness/"

NAV = [
    ("index.html", "Home", None),
    (None, "Coaching", [("how-it-works.html", "How It Works"), ("programs.html", "Programs"), ("a-day.html", "A Day With ABROFIT")]),
    (None, "Why ABROFIT", [("why-it-matters.html", "Why It Matters"), ("comparison.html", "Comparison"), ("value.html", "Value")]),
    ("faq.html", "FAQ", None),
    ("calculator.html", "BMI Calculator", None),
    ("about.html", "About", None),
    ("contact.html", "Contact", None),
]

def nav_html(active):
    out = []
    for href, label, drop in NAV:
        if drop:
            items = "".join(f'<a href="{h}"{" class=\"active\"" if h == active else ""}>{l}</a>' for h, l in drop)
            act = " active-drop" if any(h == active for h, _ in drop) else ""
            out.append(f'<div class="drop{act}"><button type="button" class="drop-parent">{label} <span class="caret" aria-hidden="true">\u25be</span></button><button class="drop-toggle" type="button" aria-expanded="false" aria-label="Show {label} submenu">\u25be</button><div class="drop-menu">{items}</div></div>')
        else:
            out.append(f'<a href="{href}"{" class=\"active\"" if href == active else ""}>{label}</a>')
    out.append(f'<a class="btn small" href="{WA_JOIN}">Free Consultation</a>')
    return "".join(out)

def page(fname, title, desc, hero_kicker, hero_h1, hero_lead, hero_img, body, hero_cta=True):
    nav = nav_html(fname)
    cta = f'<div style="margin-top:24px"><a class="btn hero-cta" href="{WA_JOIN}">Book A Free Consultation</a></div>' if hero_cta else ""
    img = f'<img class="bg" src="{hero_img}" alt="Illustrative concept image">' if hero_img else ""
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | ABROFIT by LARGAMS FITNESS</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} — ABROFIT"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&display=swap" rel="stylesheet"><link rel="icon" type="image/png" href="assets/logo-abrofit.png"><link rel="stylesheet" href="assets/style.css"></head>
<body><a class="skip" href="#main">Skip to content</a><div class="spotlight" aria-hidden="true"></div>
<header class="site-header"><div class="parent-strip"><div class="wrap">ABROFIT &mdash; by LARGAMS FITNESS</div></div><div class="wrap nav-inner"><a class="logo" href="index.html"><img class="site-logo" src="assets/logo-abrofit.png" alt="ABROFIT — by LARGAMS FITNESS"></a><button class="hamburger" aria-label="Open menu" aria-expanded="false">&#9776;</button><nav class="main-nav">{nav}</nav></div></header>
<main id="main">
<section class="page-hero hero-center">{img}<div class="wrap hero-inner"><p class="kicker">{hero_kicker}</p><h1 class="hero-title">{hero_h1}</h1><p class="lead">{hero_lead}</p>{cta}</div></section>
{body}
</main>
<footer><div class="wrap"><div class="foot-grid"><div><img class="footer-logo" src="assets/logo-abrofit.png" alt="ABROFIT logo"><p>Online fitness coaching for people living abroad and people with no time for a gym. Train from anywhere, 30 minutes a day.</p></div><div><h4>Coaching</h4><ul><li><a href="how-it-works.html">How It Works</a></li><li><a href="programs.html">Programs</a></li><li><a href="a-day.html">A Day With ABROFIT</a></li><li><a href="faq.html">FAQ</a></li></ul></div><div><h4>Why ABROFIT</h4><ul><li><a href="why-it-matters.html">Why It Matters</a></li><li><a href="comparison.html">Comparison</a></li><li><a href="value.html">Value</a></li><li><a href="calculator.html">BMI Calculator</a></li></ul></div><div><h4>Contact</h4><ul><li><a href="{WA_JOIN}">WhatsApp — Free Consultation</a></li><li><a href="{IG_ABRO}">ABROFIT Instagram</a></li><li><a href="{IG_LARG}">LARGAMS FITNESS Instagram</a></li><li><a href="contact.html">Contact Page</a></li></ul></div><div class="parent-box"><img class="parent-logo" src="assets/logo-largams-dark.png" alt="LARGAMS FITNESS logo"><h4>A Product Of</h4><p>LARGAMS FITNESS — the main company behind ABROFIT. <a href="{LARG_SITE}">Visit the LARGAMS FITNESS website &rarr;</a></p></div></div><div class="foot-bottom"><p>&copy; <span id="year">2026</span> ABROFIT. ALL RIGHTS RESERVED.<br>ABROFIT &mdash; The Online Fitness Division of LARGAMS FITNESS. Prices on enquiry unless stated as free. Results vary by person and consistency.</p></div></div></footer>
<a class="wa-float" href="{WA_JOIN}"><span>WhatsApp Us</span></a>
<script src="assets/config.js"></script><script src="assets/app.js"></script></body></html>
"""
    pathlib.Path(fname).write_text(html)
    print("wrote", fname, len(html))

def section(kicker, h2, lead, inner):
    return f'<section class="section"><div class="wrap"><p class="kicker reveal">{kicker}</p><h2 class="reveal">{h2}</h2><p class="lead reveal">{lead}</p>{inner}</div></section>'

def cards(items):
    inner = "".join(f'<div class="card reveal"><div class="card-body"><h3>{h}</h3><p>{p}</p></div></div>' for h, p in items)
    return f'<div class="grid three" style="margin-top:28px">{inner}</div>'

CTA = f'<p class="reveal" style="margin-top:28px"><a class="btn" href="{WA_JOIN}">Book A Free Consultation</a> <a class="btn ghost" href="programs.html">See Programs</a></p>'
NOTE = '<p class="small reveal" style="margin-top:16px">General fitness information only — not medical advice. If you have a health condition, speak to a qualified professional before starting a new training or diet plan. Results vary by person and consistency.</p>'

# ---------------- INDEX ----------------
body = section("ABROFIT — Online Fitness Coaching", "Train From Anywhere.", "You live abroad, or your days are full, and the gym never fits. ABROFIT brings the coach, the plan, and the diet to your home — in 30 minutes a day.",
    cards([("30 Minutes A Day", "One focused session a day, built around your schedule — not the other way round."),
           ("A Coach Who Checks In Daily", "Your personal coach guides you, reviews your day, and keeps you on track."),
           ("Diet Plan Built For You", "Eating habits are part of the plan, not an afterthought — built around your routine and the food around you.")])
    + f'<figure class="reveal" style="margin-top:28px"><img loading="lazy" src="assets/images/coach-call.webp" alt="Illustrative concept image: online coach on a video call with a client training at home"><figcaption>Illustrative concept image — online coaching at home, not a real client session.</figcaption></figure>')
body += section("The 30-Minute Promise", "Small Daily. Big Difference.", "Thirty minutes is the promise because it is the part most people can actually keep. A short session done every day beats a long plan abandoned in week two.",
    cards([("No Commute", "No travel to a gym, no waiting for equipment, no lost hour around the workout."),
           ("No Gym Needed", "Train at home, in your room, or wherever you are — your plan is built for your space."),
           ("A Habit, Day By Day", "The program is built day by day, so the habit grows instead of depending on motivation alone.")]))
body += section("How It Works", "Six Steps. One Coach.", "From first message to daily progress — the same six steps for every client.",
    cards([("1. Contact", "Message ABROFIT on WhatsApp and say you want to start."),
           ("2. Free Consultation", "A free conversation about your life, your time, and your goal."),
           ("3. Goal Assessment", "Your coach assesses your goal and your starting point."),
           ("4. Personalized Plan", "A workout and diet plan built for you — not a generic program."),
           ("5. Begin Training", "Start with 30 minutes a day, guided by your coach."),
           ("6. Track Progress", "Daily check-ins and reviews keep the plan moving with you.")])
    + f'<p class="reveal" style="margin-top:24px"><a class="btn" href="how-it-works.html">See How It Works In Detail</a></p>')
body += section("Why It Matters", "Without A System, Fitness Slips.", "Abroad, without a gym nearby and with long work hours, fitness quietly drops off the list. Energy dips, weight creeps up, strength and stamina slip, sleep and stress get harder — and restarting feels harder every month. ABROFIT exists so the system holds when willpower alone does not.",
    f'<p class="reveal" style="margin-top:24px"><a class="btn" href="why-it-matters.html">Why It Matters</a> <a class="btn ghost" href="comparison.html">Compare Your Options</a></p>' + NOTE)
body += section("Programs", "Start Where You Are.", "A 30-day program to build the habit, a 90-day challenge to go further, and one-to-one coaching for the closest guidance. Every paid program is priced on enquiry.",
    cards([("30-Day Program", "Thirty days of guided training, diet, and daily check-ins. Price: On enquiry."),
           ("90-Day Transformation Challenge", "Ninety days with your coach, designed to build lasting change. Price: On enquiry. Results vary by person and consistency."),
           ("One-to-One Online Coaching", "Your own coach, your own plan, daily guidance. Price: On enquiry.")])
    + f'<p class="reveal" style="margin-top:24px"><a class="btn" href="programs.html">All Programs</a></p>')
body += section("Start Today", "Your First Step Is Free.", "A free consultation, and a one-day free trial to feel how ABROFIT works before you commit to anything.",
    f'<p class="reveal" style="margin-top:24px"><a class="btn" href="{WA_JOIN}">Book A Free Consultation</a> <a class="btn ghost" href="{WA_TRIAL}">Try One Day Free</a></p>')
page("index.html", "ABROFIT — Online Fitness Coaching", "ABROFIT by LARGAMS FITNESS: online fitness coaching for people abroad and people with no time for a gym. 30 minutes a day, a personal coach, a diet plan built for you.",
    "ABROFIT — By LARGAMS FITNESS", 'Fit Abroad. <span class="green-word">30 Minutes</span> A Day.',
    "Abroad? No gym? No time? No problem. A personal coach, a personalized plan, and a diet built for you — online, wherever you live.",
    "assets/images/home-workout.webp", body)

# ---------------- HOW IT WORKS ----------------
steps = [
    ("1. Contact", "You message ABROFIT on WhatsApp. No forms, no waiting rooms — just tell us you want to start, and where you are in your fitness journey."),
    ("2. Free Consultation", "A free conversation with ABROFIT about your life abroad or your busy schedule, your available time, your space, and what you want to change. This step costs nothing."),
    ("3. Goal Assessment", "Your coach assesses your goal and your starting point: what you can do now, how much time you really have, and what has stopped you before."),
    ("4. Personalized Plan", "You receive a workout plan and a diet plan built for you — your goal, your time, your food, your space. Not a generic program copied for everyone."),
    ("5. Begin Training", "You start training at home, or wherever you are, in sessions of around 30 minutes a day, with your coach guiding you."),
    ("6. Track Progress", "Your coach watches your daily progress, reviews your day with you, and adjusts the plan as you improve — so the plan keeps fitting your life."),
]
inner = "".join(f'<div class="card reveal"><div class="card-body"><h3>{h}</h3><p>{p}</p></div></div>' for h, p in steps)
body = section("How It Works", "Six Steps. One Coach.", "The same six steps for every client, from first message to daily progress.",
    f'<div class="grid two" style="margin-top:28px">{inner}</div>' + CTA + NOTE)
page("how-it-works.html", "How It Works", "ABROFIT in six steps: Contact, Free Consultation, Goal Assessment, Personalized Plan, Begin Training, Track Progress.",
    "How It Works", 'Six Steps To <span class="green-word">Your Plan</span>.',
    "No confusion, no guesswork. Here is exactly what happens when you start with ABROFIT.",
    "assets/images/coach-call.webp", body)

# ---------------- PROGRAMS ----------------
# Services adapted from the Largams site's ABROFIT services list (online only;
# the gym-only Trivandrum home-training service is deliberately NOT included).
services = [
    ("Worldwide Online Personal Training", "Professional fitness coaching wherever you are in the world — at home, abroad, or travelling."),
    ("One-to-One Online Coaching", "Your own coach, your own plan, daily guidance."),
    ("Customized Diet Plans", "Nutrition guidance built around your goal, routine, and the food where you live."),
    ("Personalized Workout Programs", "Workouts built for your goal, time, and space — not a generic program."),
    ("Weight Loss Programs", "Training and diet guidance structured around a weight-loss goal, with a coach tracking progress."),
    ("Muscle Building Programs", "Training and diet guidance structured around building strength and muscle, with a coach tracking progress."),
    ("Body Transformation Programs", "Longer programs that combine training, diet, and daily accountability. Results vary by person and consistency."),
    ("Fitness Guidance & Accountability", "A coach who checks in daily, so the plan holds when motivation alone does not."),
]
svc_inner = "".join(f'<div class="card reveal"><div class="card-body"><h3>{h}</h3><p>{p}</p></div></div>' for h, p in services)
programs_body = section("ABROFIT Services", "Everything Online.", "Adapted from the ABROFIT services on the LARGAMS FITNESS site — all online, all personalized.",
    f'<div class="grid two" style="margin-top:28px">{svc_inner}</div>')
progs = [
    ("30-Day Program", "Thirty days of guided training, a personalized diet plan, and daily coach check-ins — designed to help you build the habit and follow a plan for 30 days. Price: On enquiry. Results vary by person and consistency."),
    ("90-Day Transformation Challenge", "Ninety days with your coach, a plan that progresses with you, and daily accountability. Price: On enquiry. This is a challenge program, not a guaranteed transformation — results vary by person and consistency."),
    ("One-to-One Online Coaching", "Your own personal coach, your own plan, and guidance every day. For people who want the closest support ABROFIT offers. Price: On enquiry."),
    ("Free Consultation", "A free conversation about your goal, your time, and your life abroad or at home — before you commit to anything. Price: Free."),
    ("One-Day Free Trial", "Try one day of ABROFIT training free, and feel how online coaching works for you. Price: Free."),
]
inner = "".join(f'<div class="card reveal"><div class="card-body"><h3>{h}</h3><p>{p}</p></div></div>' for h, p in progs)
body = programs_body + section("Programs", "Choose Your Program.", "Every program includes a personalized plan and a coach who guides you daily. Paid programs are priced on enquiry — message us for current rates.",
    f'<div class="grid two" style="margin-top:28px">{inner}</div>' + CTA + NOTE)
page("programs.html", "Programs", "ABROFIT programs: 30-Day Program, 90-Day Transformation Challenge, One-to-One Online Coaching, Free Consultation, One-Day Free Trial. Prices on enquiry.",
    "Programs", 'Programs Built <span class="green-word">Around You</span>.',
    "Not one generic program for everyone. Pick the structure that fits your goal — your coach builds the plan inside it.",
    "assets/images/healthy-meal.webp", body)

# ---------------- WHY IT MATTERS ----------------
reasons = [
    ("No Time", "Long work hours and a full day leave no room for a gym trip — so fitness is the first thing dropped."),
    ("No Gym Nearby", "In a new city abroad, you may not know where to train, or there may be no gym that fits your life."),
    ("Unfamiliar Food", "New food, new routines, and eating on the go make old eating habits hard to keep."),
    ("Routine Lost After Moving", "Moving abroad resets everything — sleep, meals, movement — and the old routine does not come back on its own."),
    ("No One Watching", "Without a coach or a plan, nobody notices when a week slips into a month."),
]
inner = "".join(f'<div class="card reveal"><div class="card-body"><h3>{h}</h3><p>{p}</p></div></div>' for h, p in reasons)
costs = "".join(f'<div class="card reveal"><div class="card-body"><h3>{h}</h3><p>{p}</p></div></div>' for h, p in [
    ("Energy Drops", "Without regular movement, everyday energy can feel lower, and long days feel longer."),
    ("Weight Creeps Up", "Small daily habits — extra snacks, less movement — add up quietly over months abroad."),
    ("Strength & Stamina Slip", "Strength and stamina fade without use, so stairs, bags, and long days feel harder than they used to."),
    ("Stress & Poor Sleep", "A body that never moves and a mind that never switches off make stress and poor sleep more likely."),
    ("Restarting Gets Harder", "The longer the gap, the bigger restarting feels — which is why a system matters more than a burst of motivation."),
])
body = section("Why Fitness Fails Abroad", "It Is Not Laziness. It Is Life.", "Most people abroad do not stop caring about fitness. Life changes, and the system that held fitness in place disappears.",
    f'<div class="grid two" style="margin-top:28px">{inner}</div>')
body += section("The Cost Of Doing Nothing", "Quiet — Until It Is Not.", "Doing nothing has a cost too, in general wellness terms. None of this is a medical claim — it is what happens when movement and routine quietly leave a busy life.",
    f'<div class="grid two" style="margin-top:28px">{costs}</div>' + NOTE)
body += section("Why An App-Like Coach In Your Life Helps", "A System You Carry.", "ABROFIT is built to live in your day: a coach in your pocket, a plan for your 30 minutes, a diet that fits your food, and a daily check-in that notices when you slip — before a week becomes a month. That is why this type of coaching matters most for people abroad and people with no time: it replaces the gym trip with a system that travels with you.",
    cards([("Daily Accountability", "Someone checks in every day — so you are not doing this alone."),
           ("Built For Your Life", "Your time, your space, your food, your country — the plan bends to you, not the other way round."),
           ("Habit First", "Thirty minutes a day, every day, builds a habit that survives busy weeks.")]) + CTA)
page("why-it-matters.html", "Why It Matters", "Why fitness fails abroad without a system, and what doing nothing costs in general wellness terms. General fitness information, not medical advice.",
    "Why It Matters", 'Why Fitness <span class="green-word">Needs A System</span>.',
    "Abroad, busy, and without a gym — this is the part of life where fitness quietly disappears. Here is why, and what changes it.",
    "assets/images/morning-routine.webp", body)

# ---------------- COMPARISON ----------------
rows = [
    ("Personalized plan", "Yes", "No — you plan it yourself", "No", "No — generic videos"),
    ("Professional coach guiding you", "Yes — daily guidance", "Only if you hire one", "No", "No"),
    ("Diet plan built for you", "Yes", "No", "No", "No — general advice only"),
    ("Daily accountability", "Yes — daily check-ins", "No", "No", "No"),
    ("30 minutes a day", "Yes — built around 30 minutes", "Depends on you", "No training", "Varies — no structure"),
    ("Train from anywhere", "Yes — at home, abroad, anywhere", "No — you must go to the gym", "—", "Yes — but unguided"),
    ("Works around your schedule", "Yes — plan fits your day", "Only if the gym hours fit", "—", "Only if you stay consistent alone"),
]
trs = "".join(f'<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in rows)
body = section("Comparison", "Compare Honestly.", "Features only — no invented competitor prices or claims. Other services vary; this table compares what each option typically includes as described here.",
    f'<div class="table-wrap reveal" style="margin-top:28px"><table><thead><tr><th>Feature</th><th>ABROFIT</th><th>Gym Alone</th><th>No Plan</th><th>Random Online Videos</th></tr></thead><tbody>{trs}</tbody></table></div>' + CTA + NOTE)
page("comparison.html", "Comparison", "ABROFIT vs going to a gym alone vs no plan vs random online videos — an honest feature comparison.",
    "Comparison", 'ABROFIT Vs <span class="green-word">The Alternatives</span>.',
    "Same goal, very different support. Here is what each path actually gives you.",
    "assets/images/home-workout.webp", body)

# ---------------- VALUE ----------------
body = section("What You Get", "Everything In One Place.", "A coach, a plan, a diet, and daily check-ins — together, instead of pieced together from different places.",
    cards([("Your Personal Coach", "A professional coach who guides you and reviews your day."),
           ("Your Personalized Plan", "Workouts built for your goal, time, and space."),
           ("Your Diet Plan", "Eating habits built into the plan, around your routine and food."),
           ("Daily Check-Ins", "Your coach watches your daily progress and adjusts the plan."),
           ("30 Minutes A Day", "Training that fits a busy life, not a life built around training."),
           ("From Anywhere", "At home, abroad, travelling — your coaching travels with you.")]))
body += section("Time Saved", "No Commute. No Waiting.", "A gym trip is rarely just the workout: travel there, change, wait for equipment, travel back. ABROFIT removes the trip. Thirty minutes of training is thirty minutes of your day — not an hour and a half around it.",
    cards([("No Travel Time", "Train where you already are."),
           ("No Waiting", "Your session starts when you start it."),
           ("Fits Work & Family", "Built around shifts, family, and life abroad.")]))
body += section("Packages & Durations", "Priced On Enquiry.", "Durations follow the programs: 30 days, 90 days, and ongoing one-to-one coaching. Prices are on enquiry — message ABROFIT for current rates. Free consultation and one-day free trial are free.",
    cards([("30 Days", "Price: On enquiry"), ("90 Days", "Price: On enquiry"), ("One-to-One Coaching", "Price: On enquiry")]) + CTA + NOTE)
page("value.html", "Value", "What you get with ABROFIT and why it is worth it: coach, plan, diet, and daily check-ins in one place, with time saved and no commute.",
    "Value", 'Why ABROFIT Is <span class="green-word">Worth It</span>.',
    "Not another subscription you forget. A coach, a plan, and a diet — in one place, in your day.",
    "assets/images/coach-call.webp", body)

# ---------------- A DAY ----------------
timeline = [
    ("Morning — Check-In", "Your day starts with a check-in: how you slept, how you feel, and what today looks like. Your coach sees it and adjusts if needed."),
    ("Midday — 30-Minute Workout", "Your workout for the day, around 30 minutes, at home or wherever you are. No gym trip, no equipment hunt — your plan tells you exactly what to do."),
    ("Meals — Per Your Plan", "Your meals follow your personalized diet plan, built around your routine and the food available where you live."),
    ("Evening — Coach Review", "Your coach reviews your day: workout done, meals followed, what was hard. Small corrections now, so tomorrow is easier."),
    ("Night — Ready For Tomorrow", "Tomorrow's plan is already set. No deciding, no searching — just the next 30 minutes, when you are ready."),
]
inner = "".join(f'<div class="card reveal"><div class="card-body"><h3>{h}</h3><p>{p}</p></div></div>' for h, p in timeline)
body = section("An Example Day", "Your Day With ABROFIT.", "Example day — your plan is personalized. Times, exercises, and meals change with your coach, your goal, and your life.",
    f'<div class="grid two" style="margin-top:28px">{inner}</div><figure class="reveal" style="margin-top:28px"><img loading="lazy" src="assets/images/morning-routine.webp" alt="Illustrative concept image: morning routine at home abroad"><figcaption>Illustrative concept image.</figcaption></figure>' + CTA + NOTE)
page("a-day.html", "A Day With ABROFIT", "An example day with ABROFIT: morning check-in, 30-minute workout, meals per plan, evening coach review. Example only — your plan is personalized.",
    "A Day With ABROFIT", 'One Day, <span class="green-word">30 Minutes</span>.',
    "This is what a day looks like when the system holds it together.",
    "assets/images/morning-routine.webp", body)

# ---------------- FAQ ----------------
faqs = [
    ("I live abroad. Can I join?", "Yes. ABROFIT is built for people living abroad. Coaching is online, so your country does not stop you — you train where you live, and your coach works around your time zone and schedule as discussed in your consultation."),
    ("I have no gym. Can I train at home?", "Yes. ABROFIT programs are built for training at home or wherever you are. Your plan is made for your space."),
    ("I only have 30 minutes. Is that enough?", "That is exactly what ABROFIT is built around: around 30 minutes a day, with a plan and a coach, instead of long sessions you cannot keep. Consistency over 30 days matters more than one long workout."),
    ("Who guides me?", "A professional ABROFIT coach guides you: they build your plan, check in daily, review your day, and adjust the plan as you progress. We do not publish individual coach names or qualifications on this site — ask in your free consultation if you want to know more."),
    ("What about my food and eating habits?", "Your diet plan is part of your personalized plan. Your coach looks at your eating habits and your routine where you live, and builds eating guidance into the plan — including help controlling eating habits, day by day."),
    ("Do I need equipment?", "Most plans start with bodyweight training at home. If equipment would help your goal, your coach discusses it in your consultation and confirms it in your personalized plan. No equipment purchase is required to start."),
    ("How do I start?", "Start with a free consultation on WhatsApp. After that, you can also try a one-day free trial before committing to a program."),
    ("How much does it cost?", "Paid programs are priced on enquiry — message ABROFIT on WhatsApp for current rates. The consultation and the one-day trial are free."),
    ("Will I transform in 30 days?", "The 30-Day Program is designed to help you build the habit and follow a plan for 30 days. It is not a guaranteed transformation — results vary by person and consistency, and your coach will be honest with you about that in your consultation."),
]
inner = "".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
body = section("FAQ", "Questions, Answered.", "Short answers, no fine print. Anything else — ask in your free consultation.",
    f'<div style="margin-top:28px">{inner}</div>' + CTA)
page("faq.html", "FAQ", "ABROFIT FAQ: joining from abroad, training at home, 30 minutes a day, coaching, food, equipment, how to start, and pricing on enquiry.",
    "FAQ", 'Questions, <span class="green-word">Answered</span>.',
    "Everything people usually ask before their free consultation.",
    "assets/images/home-workout.webp", body)

# ---------------- CALCULATOR ----------------
body = section("BMI Calculator", "Check Your BMI.", "Enter your height and weight. This is general health information only — it is not a diagnosis, and it does not replace professional advice.",
    '''<div class="card reveal" style="margin-top:28px"><div class="card-body"><label for="bmi-h">Height (cm)</label><input id="bmi-h" type="number" inputmode="decimal" placeholder="e.g. 175" style="width:100%;padding:12px;margin:6px 0 14px;border:1px solid var(--line);border-radius:10px;background:#111;color:#fff"><label for="bmi-w">Weight (kg)</label><input id="bmi-w" type="number" inputmode="decimal" placeholder="e.g. 78" style="width:100%;padding:12px;margin:6px 0 14px;border:1px solid var(--line);border-radius:10px;background:#111;color:#fff"><button class="btn" type="button" id="bmi-btn">Calculate BMI</button><p id="bmi-out" style="margin-top:16px;font-size:1.2rem"></p><p class="small">BMI categories (standard): under 18.5 underweight, 18.5–24.9 healthy range, 25–29.9 overweight, 30+ obesity range. BMI does not measure muscle, body composition, or health on its own.</p></div></div>''' + CTA + NOTE)
page("calculator.html", "BMI Calculator", "ABROFIT BMI calculator: working, pure JavaScript, with a health-information disclaimer. Not a diagnosis.",
    "BMI Calculator", 'Know Your <span class="green-word">Starting Point</span>.',
    "A quick number before your consultation — nothing more than that.",
    "", body)

# ---------------- ABOUT ----------------
body = section("About ABROFIT", "Online Coaching, Built For Real Lives.", "ABROFIT is the online fitness division of LARGAMS FITNESS. It was built for one kind of person above all: someone living abroad, or someone whose days leave no time for a gym — who still wants a coach, a plan, and a diet that actually fits their life.",
    cards([("For People Abroad", "Coaching that crosses borders with you — train wherever you live."),
           ("For Busy People", "Thirty minutes a day, built around work, family, and travel."),
           ("With A Coach", "Not an app you open alone — a coach who checks in daily.")]))
body += section("A Product Of LARGAMS FITNESS", "The Main Company Behind ABROFIT.", "LARGAMS FITNESS is the main company; ABROFIT is its online fitness product. Everything on this site is ABROFIT — the gym side of LARGAMS FITNESS lives on its own website.",
    f'<div class="card reveal" style="margin-top:28px"><div class="card-body"><img class="parent-logo" src="assets/logo-largams-dark.png" alt="LARGAMS FITNESS logo" style="height:56px;width:auto;display:block"><p style="margin-top:12px">LARGAMS FITNESS — the main company behind ABROFIT. <a href="{LARG_SITE}">Visit the LARGAMS FITNESS website &rarr;</a></p></div></div>' + CTA)
page("about.html", "About ABROFIT", "ABROFIT is the online fitness division of LARGAMS FITNESS, built for people abroad and people with no time for a gym.",
    "About ABROFIT", 'ABROFIT, By <span class="green-word">LARGAMS FITNESS</span>.',
    "The online fitness product of LARGAMS FITNESS — for people abroad and people with no time for a gym.",
    "assets/images/coach-call.webp", body)

# ---------------- CONTACT ----------------
body = section("Contact", "Start With A Free Conversation.", "No address, no email published yet — contact ABROFIT directly on WhatsApp or Instagram, and start with a free consultation.",
    cards([("WhatsApp — Free Consultation", f'<a href="{WA_JOIN}">Message ABROFIT on WhatsApp &rarr;</a>'),
           ("WhatsApp Message Link", f'<a href="{WA_MSG}">Open the ABROFIT WhatsApp message link &rarr;</a>'),
           ("Instagram — ABROFIT", f'<a href="{IG_ABRO}">@abrofitbylf on Instagram &rarr;</a>'),
           ("Instagram — LARGAMS FITNESS (Parent)", f'<a href="{IG_LARG}">@largamsfitness on Instagram &rarr;</a>')])
    + f'<p class="reveal" style="margin-top:28px"><a class="btn" href="{WA_JOIN}">Book A Free Consultation</a> <a class="btn ghost" href="{WA_TRIAL}">Try One Day Free</a></p><p class="small reveal" style="margin-top:16px">Prices for paid programs are on enquiry. Free consultation and one-day free trial are free.</p>')
page("contact.html", "Contact", "Contact ABROFIT on WhatsApp or Instagram. Book a free consultation or try a one-day free trial.",
    "Contact", 'Talk To <span class="green-word">ABROFIT</span>.',
    "One message is all it takes to start.",
    "assets/images/morning-routine.webp", body)

print("done")
