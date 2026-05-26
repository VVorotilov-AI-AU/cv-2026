# SEO and AI Discovery Plan

Date: 2026-05-26

## Current Finding

Google currently surfaces Vladimir's LinkedIn profile for profile-name searches.
The LinkedIn result includes the resume and portfolio URLs, but the GitHub Pages
site itself is not yet reliably appearing as a direct result for site-specific
queries.

## Applied Technical Fixes

- Added `sitemap.xml` with resume, portfolio, showcase, and project pages.
- Updated `robots.txt` to point to the sitemap.
- Added `index, follow` robot directives.
- Added structured JSON-LD for the resume page as a `Person`.
- Added structured JSON-LD for the portfolio page as a `CollectionPage`.
- Added `llms.txt` as a concise AI-readable profile and page index.
- Kept canonical URLs on resume and portfolio pages.
- Kept LinkedIn and GitHub as cross-profile identity signals.

## External Actions Needed

1. Add the site to Google Search Console.
2. Submit `https://vvorotilov-ai-au.github.io/cv-2026/sitemap.xml`.
3. Request indexing for:
   - `https://vvorotilov-ai-au.github.io/cv-2026/`
   - `https://vvorotilov-ai-au.github.io/cv-2026/portfolio.html`
   - the strongest project pages.
4. Keep LinkedIn website links exactly aligned with the canonical resume and
   portfolio URLs.
5. Add one or two contextual backlinks from public profiles or posts where
   natural, especially LinkedIn featured links, GitHub profile README, and
   portfolio project READMEs.
6. Consider a custom domain if this site becomes the permanent public identity
   surface.

## Search Targets

- Vladimir Vorotilov resume
- Vladimir Vorotilov portfolio
- Vladimir Vorotilov mining operations AI
- Perth industrial AI consultant
- mining operations AI automation Perth
- Claude Code industrial AI portfolio

## Maintenance

- Refresh `lastmod` in `sitemap.xml` after meaningful page changes.
- Keep the resume, portfolio, LinkedIn, and GitHub descriptions consistent.
- Avoid adding private context, internal C-3PO paths, or non-public career
  strategy to indexable pages.
