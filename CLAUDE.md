# CLAUDE.md

Permanent rules for this repository. Read this before creating or editing any
course session. These rules do not change between sessions; if a new request
conflicts with a rule here, flag the conflict instead of silently overriding it.

## Course

Atelier Framework Côté Serveur — 3e année MDW, ISET Sidi Bouzid, Prof. Wael
Bouaziz. Groups: MDW32, MDW33.

## Site structure (fixed)

- The published site lives entirely in `docs/` (GitHub Pages serves the
  `main` branch's `/docs` folder).
- The reusable skeleton lives in `templates/codelab-template.html`.
- Every session is **one self-contained file**: `docs/session-XX.html`, where
  `XX` is a two-digit number from `01` to `16`.
- A new session is created by copying `templates/codelab-template.html` to
  `docs/session-XX.html` and filling in the step panels. **Never change the
  skeleton markup, the navigation JavaScript, or the pinned asset versions**
  when authoring a session — only add/edit step content inside the existing
  structure. Any change to the skeleton itself happens in the template file
  and is a deliberate, separate decision, not a side effect of writing a
  session.

## Zero emojis

No emoji characters anywhere in the site (titles, body text, code comments,
commit messages in examples, etc.). Icons come exclusively from **Font
Awesome 6.4.0**. Decorative icons get `aria-hidden="true"`. Icon-only buttons
(no visible text label) get an `aria-label` describing the action.

## Target stack

- Laravel 13.x, PHP 8.3+, SQLite as the default database, Pest for tests,
  Blade + Tailwind for the UI.
- API routes are only introduced after running `php artisan install:api`.
- Middleware aliases are registered in `bootstrap/app.php` — there is no
  `app/Http/Kernel.php` in this stack.
- Models use `protected $fillable = [...]` and a `casts(): array` method
  (not the `$casts` property).
- Laravel Breeze is legacy for this course: never use it. Use the current
  Laravel starter-kit guidance instead.

## Code blocks

- Use `<pre><code class="language-php">`, `language-bash`,
  `language-powershell`, `language-json`, `language-sql`, or `language-markup`
  as appropriate.
- Code text is HTML-escaped (`&lt;`, `&gt;`, `&amp;`, ...).
- Code is always **complete and runnable** — never truncated with `...` or
  similar placeholders. If a snippet needs to omit unrelated code for
  brevity, write the full, real code instead; do not fake it.

## Every step must contain

1. Goal
2. Commands
3. Full code
4. Expected result
5. Verification

## Session structure (in order)

1. Prerequisites & Objectives
2. Environment check (10 min)
3. Concept Brief (15 min)
4. Guided Steps (120 min)
5. Independent Challenge (30 min)
6. Assessment Checklist
7. Deliverable — commit, tag `lab-XX`, README with screenshots (10-15 min)

## Windows lab PCs

Students work on Windows lab machines. Wherever a command differs between
bash and PowerShell, give both — do not assume bash-only students can adapt
PowerShell-only commands, or vice versa.

## After creating a session

1. Add an entry for it in `docs/index.html` (card with title, week, and
   status `Disponible`).
2. Run `scripts/check.py` and fix every reported issue before committing.
3. Confirm every sidebar link in the new session targets a step id that
   actually exists in that same file.
