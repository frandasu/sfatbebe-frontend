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
