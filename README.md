# sfatbebe-frontend

Static frontend for sfatbebe.ro — a conversational baby-product finder. A parent
describes what they need in plain Romanian; the page calls the backend `/ask`
endpoint and shows matching products that can be bought in Romania right now,
ranked by a recommendation score, with prices and discounts.

Single-page static site (HTML + CSS + vanilla JS). No build step.

## Configure

Open `index.html` and set your backend URL near the top of the `<script>`:

    const API_URL = "https://your-backend.onrender.com";   // no trailing slash

## Run locally

Just open `index.html` in a browser, or serve the folder:

    python -m http.server 8000
    # then visit http://localhost:8000

## Deploy on Vercel

1. Push this repo to GitHub.
2. Vercel → Add New → Project → import this repo.
3. It is detected as a static site — no build command needed. Deploy.
4. The repo must be **public** on the Vercel Hobby plan (a static frontend has
   no secrets, so public is fine).

Every push to `main` redeploys automatically.

## Custom domain (later)

Vercel → project → Settings → Domains → add `sfatbebe.ro`, then set the DNS
records Vercel shows at your domain registrar.

## Notes

- The backend must allow CORS for this origin (it currently allows all origins
  for MVP; tighten to the real domain later).
- Product titles from the feed are cleaned for display in `cleanName()`.
- The "Recomandate" / "Preț" toggle sends `sort` to `/ask`.

## Guide figures

Guides in `ghiduri/` can carry figures. Each guide keeps its CSS inline, so a
guide that uses figures has the `.fig` rules in its `<style>` (copy them from
`ghiduri/cum-alegi-scaun-auto`). Images live in `ghiduri/img/`.

    <!-- one image -->
    <figure class="fig"><img src="/ghiduri/img/x.svg" width="640" height="320"
      alt="What the image shows, in context" loading="lazy" decoding="async">
      <figcaption>What to look at and why it matters.
      <small>Ilustrație schematică: sfatbebe.ro</small></figcaption></figure>

    <!-- side-by-side comparison; stacks under 560px -->
    <figure class="fig"><div class="fig-pair">
      <div><img ... width="400" height="300"><span>Label A</span></div>
      <div><img ... width="400" height="300"><span>Label B</span></div>
    </div><figcaption>... <small>source</small></figcaption></figure>

- Always set `width`/`height` to the image's intrinsic size (no layout shift).
- The first figure of a page loads eagerly (no `loading`); later ones get `loading="lazy"`.
- A featured image is just a first figure placed right after the lead; optional.
- `<small>` carries the source. For an external image, write author, licence and
  a link to the original, e.g. `Foto: Nume, CC BY-SA 4.0 (Wikimedia Commons)`.
- Current figures are original schematic SVGs: 640 wide for a full-width figure,
  400x300 for each half of a pair, text at least ~20px in the viewBox so it stays
  readable on a phone. Palette: the site's `:root` colours.
- Only add a figure when it explains something the text can't; otherwise stay text-only.
