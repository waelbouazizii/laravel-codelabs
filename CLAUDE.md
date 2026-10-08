# CLAUDE.md

Permanent rules for this repository. Read this before creating or editing any
course session. These rules do not change between sessions; if a new request
conflicts with a rule here, flag the conflict instead of silently overriding it.

Also read `session-guidelines.md`: lessons learned from authoring Session 01
(verified lab-stack facts, copy-block rules, review workflow). It explains how
to apply these rules; if it conflicts with this file, this file wins.

## Course

Atelier Framework Côté Serveur — 3e année MDW, ISET Sidi Bouzid, Prof. Wael
Bouaziz. Groups: MDW32, MDW33.

## Site structure (fixed)

- The published site lives entirely in `docs/` (GitHub Pages serves the
  `main` branch's `/docs` folder).
- The reusable skeleton lives in `templates/codelab-template.html`.
- Every session is **one self-contained file**: `docs/session-XX.html`, where
  `XX` is a two-digit number from `01` to `16`.
- Exception: screenshots. They live in `docs/img/sXX/`, are referenced with a
  relative path, and are kept to steps that are hard to do or hard to fix.
  Every image has a French alt text, `width` and `height` attributes,
  `loading="lazy"`, and a `figcaption` (see `session-guidelines.md`).
  Inline figures follow the section Diagrammes et figures.
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
- PostgreSQL appears once, in S08, as an optional driver switch through
  `.env`. It is never a prerequisite: every session, every test and every
  graded deliverable must work on SQLite. MySQL is not taught.
- API routes are only introduced after running `php artisan install:api`.
- Middleware aliases are registered in `bootstrap/app.php` — there is no
  `app/Http/Kernel.php` in this stack.
- Models use `protected $fillable = [...]` and a `casts(): array` method
  (not the `$casts` property).
- Laravel Breeze is legacy for this course: never use it. Use the current
  Laravel starter-kit guidance instead.

## Student pages are self-guided

- A student alone at a PC must be able to finish the page without asking
  anyone: no "prévenez l'enseignant", no peer or oral tasks. Use written
  self-checks with a hidden model answer instead.
- No "Plan de secours" cards. Instructor contingencies belong in the session
  spec's RISKS section. Only exception: one inline sentence when a missing
  tool changes a command, and the step it points to must show that command.
- Use `http://localhost:8000` (the `APP_URL`) for the application, never the
  Vite URL (`http://localhost:5173`).

## Code blocks

- Use `<pre><code class="language-php">`, `language-bash`,
  `language-powershell`, `language-json`, `language-sql`, or `language-markup`
  as appropriate.
- Code text is HTML-escaped (`&lt;`, `&gt;`, `&amp;`, ...).
- Code is always **complete and runnable** — never truncated with `...` or
  similar placeholders.
- A file is shown in full when it is created or restructured. When a later
  step changes only a few lines, show only those lines with their exact
  position ("juste après la ligne ...", "avant la dernière accolade"),
  followed by the complete file in
  `<details><summary>Voir le fichier complet à ce stade</summary>`.
  Snippets are never truncated with "...".

## Copy blocks

- One block = one terminal, commands run top to bottom. A long-running
  command (`composer run dev`, `php artisan serve`, `npm run dev`) is the last
  line of its block, and two long-running commands never share a block
  (use "Terminal 1" and "Terminal 2").
- A command that must run after a manual edit goes in its own block, placed
  after the sentence that tells the student to edit and save.
- A conditional command gets its own block labelled "Seulement si ...", and
  never sits unlabelled in the main sequence.
- Every block has a label: "Bash et PowerShell (identique) :" or the two
  shell-specific labels.
- File content shown for reading is reproduced literally, including comments
  that end with "..."; the no-truncation rule targets code students write.

## Every step must contain

1. Goal
2. Commands
3. Full code
4. Expected result
5. Verification

The five elements stay mandatory, but "Expected result" and "Verification"
may share one card titled "Résultat et vérification" (`fa-list-check`, items
with `fa-regular fa-square`).

Each guided step ends with a sixth card, "À retenir" (`fa-lightbulb`), with a
"Pourquoi ?" callout and, where useful, an "Erreurs fréquentes" callout (see
`session-guidelines.md` for the class strings).

## Quiz éclair

- Each conceptual guided step, and the Concept Brief, may end with one
  "Quiz éclair" card placed just before "À retenir".
- 1 to 3 questions per card, 3 options each, exactly one correct.
- Question ids follow `quiz-sXX-qNN` and are unique in the page.
- Every question has an explanation (`.quiz-explain`).
- Questions test understanding or ask to predict a result, never recall of a
  command name.
- No points, no grade: the score line only counts first-try answers.
- The quiz script and CSS belong to the skeleton (see
  `templates/codelab-template.html`, step 2, for the card markup) and are
  never edited in a session. Never put a display utility class (`block`,
  `flex`, ...) on `.quiz-feedback` or `.quiz-explain`: it would defeat the
  `hidden` attribute.

## Diagrammes et figures

- A figure is content inside a step panel. It never changes the skeleton.
- Prefer, in this order: an HTML figure built with Tailwind utilities or a real
  table; a hand-written inline SVG; an image file in `docs/img/sXX/` for
  screenshots only.
- Every figure is a `<figure>` with a French `<figcaption>` numbered
  "Figure S.n" that states the takeaway.
- Inline SVG has `role="img"`, `aria-labelledby` pointing to a French
  `<title>` and `<desc>`, ids prefixed `sXX-`, a `viewBox` with `width` and
  `height`, the classes `w-full h-auto`, and text of 11 px or more. A wide
  diagram also gets a `min-w-[...]` class so that it scrolls inside
  `div.overflow-x-auto` instead of shrinking.
- Colour is never the only cue: use a thicker border, a number or a text label.
- No animation, no autoplay, no external diagram library.
- At most three figures in the Concept Brief and one per guided step.
- The request-cycle diagram introduced in session 04 (Figure 4.1) is the
  canonical layout: later sessions reuse it and only move the highlight.

## Session structure (in order)

1. Prerequisites & Objectives
2. Environment check (10 min)
3. Concept Brief (15 min)
4. Guided Steps (120 min)
5. Independent Challenge (30 min)
6. Assessment Checklist
7. Deliverable — commit, tag `lab-XX`, README with screenshots (10-15 min)

The written notes self-check of the Concept Brief may be replaced by a Quiz
éclair.

## Windows PCs

Most students work on their own Windows laptops; a few use the university's
shared Windows lab PCs. Pages must work on both. Shared-PC hygiene (credential
cleanup, browser sign-out) is a part labelled "Seulement si vous travaillez
sur un poste de l'université" (or "Seulement si vous avez travaillé sur un
poste de l'université" at the end of a session, in the Livrable).

Wherever a command differs between bash and PowerShell, give both — do not
assume bash-only students can adapt PowerShell-only commands, or vice versa.

The Assessment Checklist covers only work done before it. Screenshots, commit
and tag are verified in the Deliverable's own Vérification card.

## After creating a session

1. Add an entry for it in `docs/index.html` (card with title, week, and
   status `Disponible`).
2. Run `scripts/check.py` and fix every reported issue before committing.
3. Confirm every sidebar link in the new session targets a step id that
   actually exists in that same file.
4. Check that `docs/index.html` titles and weeks match the Overview table of
   `course-plan.md` (week = ceil(session number / 2)).
