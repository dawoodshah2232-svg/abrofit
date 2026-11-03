# ABROFIT — Online Fitness Coaching by LARGAMS FITNESS

Static, build-free website for **ABROFIT only**. ABROFIT is the main brand here;
**LARGAMS FITNESS is the parent company** ("ABROFIT — by LARGAMS FITNESS" in the
header strip, About page, and footer of every page).

Live: https://dawoodshah2232-svg.github.io/abrofit/

## Pages
- `index.html` — Fit Abroad. 30 Minutes A Day.
- `how-it-works.html` — 6 steps: Contact → Free Consultation → Goal Assessment → Personalized Plan → Begin Training → Track Progress
- `programs.html` — ABROFIT services (adapted from the Largams site) + 30-Day Program, 90-Day Transformation Challenge, One-to-One Coaching, Free Consultation, One-Day Free Trial
- `why-it-matters.html` — Importance: why fitness fails abroad, cost of doing nothing (general wellness terms only)
- `comparison.html` — Feature comparison: ABROFIT vs gym alone vs no plan vs random online videos
- `value.html` — What you get, time saved, packages/durations
- `a-day.html` — Example day (labelled as an example; plans are personalized)
- `faq.html` — Real questions from the concept
- `calculator.html` — Working BMI calculator (pure JS, disclaimer, not a diagnosis)
- `about.html` — ABROFIT story + parent-company section
- `contact.html` — WhatsApp + Instagram, free consultation CTA

## Brand
- Base #090909, white, silver #BFC3C7, ABROFIT lime #8DE32C, darker green #5FA812, light green #C6F48A.
- **No gold anywhere on this site** (gold belongs to Largams).
- Header/footer backgrounds are pure black #000 so the black-background ABROFIT logo blends with no card edge. Logo files are used unchanged (CSS display sizing only).
- Hero highlighted words use an animated running green gradient (`greenRun`), with `prefers-reduced-motion` respected.

## Assets
- `assets/logo-abrofit.png` — official ABROFIT logo, byte-identical copy (SHA-256 11f036664ae98889c77183ef887cb33e149b6a7acede62f202d54f806820ec5d)
- `assets/logo-largams-dark.png` — LARGAMS dark logo, used SMALL in parent-company sections only (SHA-256 f44637e5d8ba3d7d9ae48fd4b2864399e3565f7f2103431f7efe6c9d3a416faf)
- `assets/images/*.webp` — generated concept images, labelled in alt text as illustrative concept images, never real clients/trainers/facilities.

## Content rules (do not break these)
- Prices: **On enquiry** everywhere for paid programs. Never invent a price, trainer name/qualification, testimonial, transformation photo, client count, success rate, or achievement.
- No guaranteed transformation claims. The 30-Day Program is "designed to help you build the habit and follow a plan for 30 days"; results vary by person and consistency.
- General fitness information only — not medical advice. No medical claims, diagnoses, or guaranteed outcomes.
- No fake login, payment, booking, or admin system. CTAs are WhatsApp enquiry + free consultation only.
- The Largams gym-only Trivandrum freelance home-training service is NOT an ABROFIT service and is not on this site.
- WhatsApp: `wa.me/918137008663` — **+91 is PROVISIONAL and unverified** (see `assets/config.js` comment). Do not present +91 as verified publicly until the owner confirms it.
- To rebuild pages after editing `build.py`, run: `python3 build.py` (it regenerates all 11 HTML files from the shared template; do not hand-edit generated pages without updating the template).

## Deploy
GitHub Pages from `main`, root. After each push, check `pages/builds` and wait for status `built` before pushing again.
