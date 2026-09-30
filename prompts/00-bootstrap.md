Go with MY steps below, not your alternative plan. Notes before starting:
- Laravel 13 is released (March 2026, PHP 8.3+). Your training data may stop at 12.x; do not downgrade. If you need to confirm an API, say so and I will check the docs.
- Language: French UI text (titles, explanations, buttons), English for code, comments, commands and file names.
- Folder layout is fixed: site lives in docs/ (GitHub Pages serves main /docs), template in templates/.

Do these steps in order and show me the result of each:

1. Create CLAUDE.md with these permanent rules:
   - Every session is ONE self-contained file docs/session-XX.html (XX = 01..16), copied from templates/codelab-template.html. Never change the skeleton, navigation JS, or asset versions.
   - Zero emojis anywhere. Icons: Font Awesome 6.4.0 only; decorative icons get aria-hidden="true"; icon-only buttons get aria-label.
   - Target stack: Laravel 13.x, PHP 8.3+, SQLite default, Pest tests, Blade + Tailwind. API routes only after `php artisan install:api`. Middleware aliases in bootstrap/app.php (no Kernel.php). Models use $fillable and a casts() method. Breeze is legacy: never use it.
   - Code blocks: <pre><code class="language-php|bash|json|sql|markup">, HTML-escaped, complete (no "...").
   - Every step contains: goal, commands, full code, expected result, verification.
   - Session structure: Prerequisites & Objectives; Environment check (10 min); Concept Brief (15 min); Guided Steps (120 min); Independent Challenge (30 min); Assessment Checklist; Deliverable (commit, tag lab-XX, README with screenshots) (10-15 min).
   - Students use Windows lab PCs: give PowerShell-compatible commands where they differ from bash.
   - After creating a session: add it to docs/index.html, run scripts/check.py, confirm every sidebar link targets an existing step.

2. Create scripts/check.py (Python 3, no dependencies): scans docs/*.html and fails if it finds emoji characters (U+1F300-U+1FAFF, U+2600-U+27BF), sidebar links pointing to missing step ids, or "..." inside code blocks. Print a clear pass/fail report.

3. Create templates/codelab-template.html: Material-inspired codelab with dark left sidebar (step links, active state, completed-step markers), top header with current step title and Prev/Next buttons, content cards (.md-card), keyboard arrow navigation, step number in URL hash (#step-3) so refresh keeps position, a copy button on every code block, a progress bar, responsive layout (sidebar collapses on mobile), html lang="fr". Assets: Tailwind play CDN, Font Awesome 6.4.0 from cdnjs, Roboto from Google Fonts, Prism 1.29.0 prism-tomorrow theme with prism-core plus plugins/autoloader (so php, bash, powershell, json, sql highlight). Include 3 placeholder steps.

4. Create docs/index.html: course home page in the same visual style, listing sessions 01-16 as cards (title, week, status "Disponible" or "Bientôt"), course info (Atelier Framework Côté Serveur, 3e année MDW, ISET Sidi Bouzid, Prof. Wael Bouaziz), groups MDW32 and MDW33.

5. Create docs/.nojekyll and replace README.md with a short explanation of the repo and how to preview locally: python -m http.server -d docs 8000

6. Run python scripts/check.py, then git add, commit "Bootstrap course site", and stop. Do not push.