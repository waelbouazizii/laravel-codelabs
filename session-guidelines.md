# session-guidelines.md

Lessons learned while authoring, testing and proofing Session 01 (30 September 2026).
Read this file together with:

- `CLAUDE.md` for the hard rules;
- `laravel13-conventions.md` for code;
- `course-plan.md` for sequencing.

If this file conflicts with `CLAUDE.md`, `CLAUDE.md` wins and the conflict is flagged. This file explains how to apply the rules so that students are not confused.

## 1. Verified facts about the lab stack (Windows, 30 Sep 2026)

- **Installer prompts.** `laravel new` installs the skeleton `laravel/laravel` v13.10.1. Its first two prompts are:
  - `Do you want to use a starter kit? (yes/no) [no]`. The answer is `no`.
  - `Which frontend stack do you want to build on? [Blade]`, with the choices blade, react, svelte, vue and livewire. The answer is `blade`.

  The prompts that follow (testing framework, database, Laravel Boost, npm) are not verified yet. Keep them marked "(si demandé)" until they are confirmed on a lab PC.
- **`composer run dev` works on Windows.** Vite v8.3.1 prints `Local: http://localhost:5173/` prominently. The application itself is on the `APP_URL` line, `http://localhost:8000`, so every session must tell students to open port 8000, not 5173.
- **fontaine warning.** laravel-vite-plugin v3.2.0 prints `[laravel:fonts] Optimized font fallbacks require the optional "fontaine" package`. The warning is harmless, so say so in the "Résultat attendu" card.
- **Framework version.** The Vite plugin reports Laravel v13.34.0.
- **php.new is not used anymore (observed 1 Oct 2026, three groups).** After a php.new (herd-lite) install, `laravel new` sometimes failed with OpenSSL errors, and no fix inside that install worked reliably.
- **The install that works.** Install PHP with the official PowerShell command from https://www.php.net/downloads (Windows). The extensions are disabled by default, so enable them in `php.ini`: `extension_dir = "ext"`, curl, fileinfo, intl, mbstring, mysqli, openssl, pdo_mysql, pdo_sqlite, sqlite3 and zip. Then install Composer with the official `Composer-Setup.exe`, and the Laravel installer with `composer global require laravel/installer`.
- **Composer-Setup.exe (verified 2 Oct 2026).** It offers "Install for me only", which needs no admin rights. It proposes the first `php.exe` found in the PATH, so a leftover herd-lite PHP is picked silently unless step A1 removed it.
- **PATH conflicts.** A PC that already had php.new keeps `herd-lite` in the user PATH, which can shadow the new PHP. `where.exe php` shows which one wins, and the herd-lite entry must be removed.
- **Node.js and Git** are separate installs, and they usually need admin rights.

## 2. Do

### Self-guided pages

- Every page is fully self-guided: a student alone at a PC must be able to finish it without asking anyone.
- Replace oral or peer checks with written self-checks. Use a short notes file (`notes/sXX-*.md`) and a model answer hidden in `<details><summary>Voir un corrigé</summary>`.
- A self-check always compares the student's answer with something on the page: a diagram, a table or a model answer.

### Toolchain coherence

- Every tool the session checks has an install path on the page, and every tool the session uses is checked first.
  - Open gap: `code .` is used in S01 step 7, but VS Code is never checked.
- The environment check has exactly one command block and one table. The table's last column links to the exact install sub-part (Étape 1, partie A, B or C).
- A cross-reference must lead to a visible command. If step X says "à l'Étape Y, lancez Z", step Y must show Z in a code block.

### Copy blocks

- One block means one terminal, running its commands from top to bottom.
- A long-running command (`composer run dev`, `php artisan serve`, `npm run dev`) is always the last line of its block. Two long-running commands never share a block; use "Terminal 1" and "Terminal 2".
- A command that must run after a manual edit goes in its own block, placed after the sentence that tells the student to edit and save.
- A conditional command gets its own block labelled "Seulement si …". A conditional command never sits unlabelled in the main sequence.
- Every block has a label: "Bash et PowerShell (identique) :" or the two shell-specific labels.
- File content shown for reading is reproduced literally, including comments that end with "...". The no-truncation rule targets code students write, not literal comment text.

### Insights

- End every guided step with an "À retenir" md-card (icon `fa-lightbulb`). Do the same for the environment check, the challenge and the deliverable.
  - A "Pourquoi ?" callout explains the concept behind the step.
  - An "Erreurs fréquentes" callout, where useful, gives the exact error text a student will see, in `<code>`, and what it means.
- Keep each callout to 2-4 sentences.

### Quiz

- Wrong options must be plausible mistakes that students actually make.
- Vary the position of the correct answer from one question to the next.
- One idea per question.
- Count about 1 minute per question; quiz time is included in the step durations.

### URLs

- Use `http://localhost:8000` everywhere, matching `APP_URL`. Mention `127.0.0.1:8000` once, as an equivalent.

### Order of parts

- The Assessment Checklist (part 6) covers only work done before it.
- Screenshots, the commit and the tag are verified in the Vérification card of the Deliverable (part 7).
- Checklist items use empty boxes: `fa-regular fa-square`.

### Git identity and credentials

- Run `git config user.name` / `user.email` without `--global`: a local identity works on both laptops and shared PCs.
- The email must be the student's GitHub account email, or the email they will create the account with before S02.
- No GitHub login on university PCs before S02's credential hygiene.
- Credential cleanup (cmdkey, browser sign-out) only applies to university PCs, and personal laptops keep the GCM credential.
- Offer `git commit --amend --reset-author --no-edit` as a conditional block, for when the installer's commit carries another identity.

### Screenshots

- Use screenshots only for steps that are hard to do or hard to fix: installer prompts, installer windows, and output where the student must pick the right line. Plain terminal output is shown as text instead.
- Store them in `docs/img/sXX/` as `sXX-eN-description.png`, captured on a lab PC, cropped, without personal data, about 1200 px wide at most and compressed.
- Annotate with at most a box or two and a short French label. The caption repeats what the annotation says, so colour is never the only cue.
- Markup: `<figure>` containing `<img>` with a relative `src`, a French `alt`, `width`/`height` and `loading="lazy"`, followed by a `<figcaption>`.

### Markup and accessibility

- Wrap every table in `div.overflow-x-auto`. Key/value tables use `<th scope="row">` in the first column.
- Callout classes, reused from session 01 for consistency:

  | Callout | Border and background | Icon | Text |
  |---|---|---|---|
  | Info | `border-blue-500 bg-blue-50` | `fa-circle-info` | default |
  | Warning | `border-amber-500 bg-amber-50` | `fa-triangle-exclamation` | default |
  | Pourquoi ? | `border-indigo-500 bg-indigo-50` | `fa-lightbulb text-indigo-500` | `text-sm text-indigo-900` |
  | Erreurs fréquentes | `border-rose-500 bg-rose-50` | `fa-bug text-rose-500` | `text-sm text-rose-900` |
  | Danger (mandatory security action only) | `border-red-600 bg-red-50` | `fa-triangle-exclamation text-red-600` | `text-sm text-red-900` |

  Every callout also uses `border-l-4 p-4 rounded flex gap-3`, and every icon has `aria-hidden="true"`.

## 3. Don't

- **No "Plan de secours" cards on student pages.** Contingencies belong in the RISKS section of the session spec, for the instructor only.
  - The only exception is one inline sentence, when a missing tool changes a command (for example: no Node.js, so run `php artisan serve`). The step it points to must show that command.
- **No teacher or peer interaction prompts:** no "prévenez l'enseignant", "expliquez à un voisin", "en binôme" or oral tasks.
- **No duplicate checks inside one step,** such as a second "where are the tools" block after the version checks.
- **No hardcoded PHP install command.** The command embeds a PHP version, so link to https://www.php.net/downloads instead. The `php.ini` script and the Composer and Laravel installer commands are version-independent, so they are given in full.
- **No concept before its session,** even when `laravel13-conventions.md` says "always". For example, routes stay unnamed until S03, because `course-plan.md` sequencing wins.
- **No checklist item about something done later on the page.**

## 4. Review ("proof") workflow

- **Review the exact committed file.** Use the latest commit SHA: `https://raw.githubusercontent.com/<user>/<repo>/<sha>/docs/session-XX.html`. The `/main/` raw URL can stay cached for several minutes, and GitHub Pages lags as well.
- **Run these automated checks on every round:**
  - CSS, markup outside the panels and navigation JavaScript identical to `templates/codelab-template.html`;
  - panel ids identical to the sidebar `data-step` values, and every in-page link resolving;
  - no emoji or pictographic symbols;
  - every `<i>` has `aria-hidden="true"`, every copy button has an `aria-label`, and the `<div>` tags are balanced;
  - a sequencing grep: `->name(`, `make:controller`, `@vite`, `php artisan test`, `php artisan migrate`, `git push`, `x-layout`, adapted to the session;
  - a forbidden-phrase grep: "plan de secours", "enseignant", "voisin", "binôme";
  - Install grep: php.new and herd.laravel.com zero hits on every page; herd-lite only in session-01.html, Étape 1, parties A1 and A4.
  - a URL consistency grep (`127.0.0.1` appears only once, as the equivalence note). The grep targets the application URL: `DB_HOST=127.0.0.1` inside an `.env` code block (S08, PostgreSQL bonus) is allowed.
  - quiz script and CSS identical to the template;
  - every `.quiz-question` has a unique id, a `data-answer` matching exactly one of its `data-option` values, three options, one `.quiz-feedback` with `aria-live="polite"` and one non-empty `.quiz-explain`;
  - at least one `[data-quiz-score]` in every page that has questions.
  - every `<svg>` has `role="img"`, a `<title>` and a `<desc>`, and every `<figure>` has a `<figcaption>`;
- When a shared fact changes (install method, URL, prompt wording), grep every docs/session-*.html for the old wording, not only the session being edited.
- **Check `docs/index.html`** against the Overview table of `course-plan.md`: titles, and a week equal to `ceil(session / 2)`.
- **Use the quoted-heredoc form for Claude Code prompts,** so that `$`, backticks and quotes reach Claude Code literally:

  ```bash
  claude "Read CLAUDE.md ... then ...
  $(cat <<'SPEC'
  ...full specification...
  SPEC
  )"
  ```

- **Save instructor-only material outside the student page.** Examples are the offline project archive `mini-cms-base.tar.gz` on USB and the lab-PC checks.

## 5. Still to verify on a lab PC

- Whether `Composer-Setup.exe` adds the Composer global `vendor\bin` folder to the PATH.
- Where the official php.net PowerShell command installs PHP (the folder students should see in `where.exe php`).
- The Session 02 php -r extension check (based on get_loaded_extensions) prints an empty line on a PC that completed Session 01, Étape 1, partie A (A3).

- The `laravel new` prompts after the frontend-stack question.
- The VS Code `code` command on every lab PC.
- Whether the Node.js and Git for Windows installers run with the lab accounts' rights.
- Whether `laravel new` initializes a Git repository or makes a first commit, and with which identity.
- Whether the welcome page renders without a Vite build (the no-Node path).
- The PostgreSQL bonus of S08: install path on Windows, the two PHP extensions, and whether `php artisan migrate` can create the missing database.
