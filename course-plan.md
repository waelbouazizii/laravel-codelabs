# course-plan.md

Atelier Framework Côté Serveur — Laravel 13.x / PHP 8.3+ — 3e année MDW (MDW32, MDW33), ISET Sidi Bouzid.
16 session slots of about 3h10, 2 per week over 8 weeks. Since 19 Nov 2026 the course ends with S14 (S14 and S15 merged into one class) and S16 is a take-home final submission; see Calendar buffer. This file is the sequencing authority: a session may only use concepts introduced in the same or an earlier session (see the Concept Index at the end).

## Evolving student project: Mini-CMS

Every student builds one application, `mini-cms`, from S01 to S16, in one GitHub repository.

| Entity | Introduced | Purpose |
|---|---|---|
| Static pages (home, a-propos) | S01-S04 | Routing, controllers, Blade layout |
| `Post` (title, slug, body, is_published, published_at) | S05 | First model, CRUD |
| `Category` (1:N with Post), `Tag` (N:N via `post_tag`) | S07 | Relationships |
| `User` as author, `role` column (`author` / `admin`) | S07 (author link), S11 (auth, role) | Ownership, authorization |
| Read-only JSON API `/api/posts`, `/api/categories` | S13 (posts), S14 (categories, filters) | API Resources |
| Token-protected write API | S14 | Sanctum |

Final result: a small publishing platform with public pages, an authenticated back office (authors manage their own posts, admins manage categories and tags), a JSON API, and a green Pest suite.

## Conventions for the whole course

- Session file: `docs/session-XX.html`, XX = 01 to 16. S15 is retired: there is no `docs/session-15.html` and no S15 card in `docs/index.html`.
- Session A (odd numbers) = guided codelab. Session B (even numbers) = applied sprint + assessment on the same repository. B sessions keep the 7-part structure from CLAUDE.md; in a B session, "Guided Steps" are sprint tasks with checkpoints, and the Assessment Checklist is graded. Exceptions: S14 is a guided codelab (A format) in a B slot, and S16 is a take-home submission (B format, no class).
- Git tags: Session A of week W produces `lab-0W`, Session B produces `lab-0Wb` (week 1: `lab-01`, `lab-01b`; week 8: `lab-08`, `lab-08b`). Exception: S14 produces two tags, `lab-07b` (middle of the session) and `lab-08` (end of the session).
- Stack: `laravel new mini-cms` with no starter kit (Blade frontend stack), Pest, SQLite. Run with `composer run dev`. SQLite stays the default database for all sessions; PostgreSQL is an optional driver switch in S08 and is never required afterwards.
- Windows PCs (mostly personal laptops, some university lab PCs): every command that differs between bash and PowerShell is given in both.
- Repositories are public (portfolio). To limit copying, the Git history is graded: small meaningful commits between tags, one tag per session (two in S14), commits authored with the student's own identity.
- Toolchain: PHP 8.3+, Composer, Laravel installer (composer global require laravel/installer), Node.js LTS + npm (required by Vite / `composer run dev`, installed separately from PHP), Git for Windows, VS Code (the `code` command is used from S01).

## Overview

| Session | Week | Type | Title | Tag |
|---|---|---|---|---|
| S01 | W1 | A | Architecture MVC et premier projet Laravel 13 | lab-01 |
| S02 | W1 | B | Git, GitHub et publication du projet | lab-01b |
| S03 | W2 | A | Routage, contrôleurs et layouts Blade | lab-02 |
| S04 | W2 | B | Sprint : pages statiques et composants Blade | lab-02b |
| S05 | W3 | A | Migrations, Eloquent et CRUD des articles | lab-03 |
| S06 | W3 | B | Sprint : CRUD complet et tests Pest | lab-03b |
| S07 | W4 | A | Relations Eloquent, factories et seeders | lab-04 |
| S08 | W4 | B | Sprint : catégories, tags et chargement anticipé | lab-04b |
| S09 | W5 | A | Form Requests, messages flash, middleware et exceptions | lab-05 |
| S10 | W5 | B | Sprint : validation et robustesse de l'application | lab-05b |
| S11 | W6 | A | Authentification manuelle, Gates et Policies | lab-06 |
| S12 | W6 | B | Sprint : autorisations et comparaison avec le starter kit Livewire | lab-06b |
| S13 | W7 | A | Première API REST : install:api et API Resources | lab-07 |
| S14 | W7 | A (créneau B) | API complète et authentification par jetons Sanctum | lab-07b, lab-08 |
| S15 | — | — | Fusionnée avec S14 (pas de séance) | — |
| S16 | W8 | B (à distance) | Livraison finale du projet | lab-08b |

---

## Week 1

### S01 — Architecture MVC et premier projet Laravel 13
- Week: W1 — Type: A — Tag: `lab-01` (local only; pushed in S02)
- Learning outcomes:
  1. Describe the MVC pattern and the Laravel request lifecycle (`public/index.php` -> `bootstrap/app.php` -> routing -> controller/closure -> response).
  2. Verify a working PHP 8.3+ / Composer / Laravel installer toolchain (official PHP for Windows with php.ini extensions enabled, Composer-Setup.exe, composer global require laravel/installer) and Node.js LTS + npm on Windows. Fallback if Node is missing: `php artisan serve` without Vite (no Tailwind in S01).
  3. Create a Laravel 13 project with SQLite and Pest, and run it with `composer run dev`.
  4. Navigate the Laravel 13 skeleton (no `app/Http/Kernel.php`, no `routes/api.php`, configuration in `bootstrap/app.php`).
  5. Write a first closure route returning a string and a view.
- Key commands: `php -v`, `php --ini`, `where.exe php`, `composer -V`, `composer global require laravel/installer`, `laravel --version`, `node -v`, `npm -v`, `git --version`, `laravel new mini-cms`, `composer run dev`, `php artisan --version`, `php artisan route:list`, `php artisan about`.
- Git (copy-paste only, explained in S02): `git config user.name` and `git config user.email` run inside the project (local, not `--global`: the identity stays specific to this repository, which is required on university lab PCs), `git init` (only if the installer did not create the repository), `git add -A`, `git commit -m "lab-01"`, `git tag lab-01`. The email is the student's GitHub account email, or the one they will create the account with before S02. No GitHub account is needed in S01, and students do not log into GitHub on lab PCs.
- Reuses: nothing (first session). Assumes PHP basics and HTML/CSS from years 1-2.

### S02 — Git, GitHub et publication du projet
- Prerequisite: every student arrives with a GitHub account whose email matches the `git config user.email` set in S01.
- Week: W1 — Type: B — Tag: `lab-01b`
- Learning outcomes:
  1. Explain the working tree / staging area / commit / tag model and read `git status` and `git log --oneline`.
  2. Explain why `.env`, `vendor/`, `node_modules/` and `database/*.sqlite` are ignored and verify `.gitignore`.
  3. Authenticate to GitHub from a Windows PC (personal laptop or university lab PC) with Git Credential Manager (HTTPS) and push the project and its tags.
  4. Write a README with setup instructions and screenshots.
- Key commands: `git status`, `git log --oneline --decorate`, `git branch -M main`, `git remote add origin <url>`, `git push -u origin main`, `git push origin --tags`, `git tag -n`.
- Sprint: add a second closure route `/a-propos` returning a view (closure routes only, as in S01), README (project description, install steps bash + PowerShell, screenshots in `screenshots/`), push `lab-01` and `lab-01b`.
- End-of-session hygiene (mandatory on shared lab PCs): remove the `git:https://github.com` entry from Windows Credential Manager (`cmdkey /delete:git:https://github.com` or Control Panel > Credential Manager) so the next group cannot push to the student's repository; not needed on personal laptops, which keep the credential.
- Assessment focus: public repository reachable, both tags on GitHub, `.env` not committed, README renders with screenshots, commits authored with the student's own identity.
- Reuses: S01 project, the local `lab-01` tag.

## Week 2

### S03 — Routage, contrôleurs et layouts Blade
- Week: W2 — Type: A — Tag: `lab-02`
- Learning outcomes:
  1. Define routes with parameters, constraints (`whereNumber`, `where`) and names, and generate URLs with `route()`.
  2. Group routes with `prefix` and `name`, and inspect them with `route:list`.
  3. Move logic from closures to controllers using the `[Controller::class, 'method']` syntax.
  4. Build an anonymous Blade layout component (`<x-layout>`) with `{{ $slot }}` and a named `title` slot; show `@extends/@section` once as the classic alternative.
  5. Load Tailwind through Vite with `@vite(...)`.
- Key commands: `php artisan make:controller PageController`, `php artisan make:controller PostController`, `php artisan route:list --except-vendor`, `php artisan view:clear`.
- Data: posts are a hard-coded PHP array in `PostController` (no database yet); unknown slug -> `abort(404)`.
- Reuses: S01-S02 routes and repository; converts the S01/S02 closure routes to `PageController`.

### S04 — Sprint : pages statiques et composants Blade
- Week: W2 — Type: B — Tag: `lab-02b`
- Learning outcomes:
  1. Create reusable anonymous components with `@props` (navigation bar, post card, alert box).
  2. Highlight the active navigation link with `request()->routeIs()`.
  3. Use Blade control structures (`@foreach`, `@forelse`, `@if`) and always-escaped output `{{ }}`.
  4. Keep every link built from named routes (no hard-coded URLs).
- Key commands: `php artisan make:component PostCard --view`, `php artisan route:list`, `git tag lab-02b`, `git push origin main --tags`.
- Sprint: home page, a-propos page, posts list and post detail from the array, all inside `<x-layout>`.
- Assessment focus: no hard-coded URLs, layout used by every page, components with props, tag pushed.
- Reuses: S03 controllers, array data, layout.

## Week 3

### S05 — Migrations, Eloquent et CRUD des articles
- Week: W3 — Type: A — Tag: `lab-03`
- Learning outcomes:
  1. Explain the SQLite default configuration (`.env`, `database/database.sqlite`) and the migration workflow.
  2. Write the `posts` migration (title, slug unique, body, is_published, published_at, timestamps) — no foreign keys yet.
  3. Create the `Post` model with `$fillable` and the `casts()` method, and explore it in Tinker.
  4. Implement the read and create half of a resource controller with route model binding: `index` (with `paginate()`), `show`, `create`, `store`; forms with `@csrf`, `old()`, and inline `$request->validate()` with `@error` (Form Requests come in S09). Edit, update and destroy are the S06 sprint.
  5. Write and run a first Pest feature test.
- Key commands: `php artisan migrate:status`, `php artisan make:model Post -m`, `php artisan migrate`, `php artisan migrate:rollback`, `php artisan tinker`, `php artisan make:controller PostController --resource --model=Post --force` (the S03 array-based controller already exists; without `--force` Artisan refuses to overwrite it. The codelab explains this and tells students to note any custom code first), `php artisan make:test PostPagesTest`, `php artisan test`.
- Pest setup: enable `RefreshDatabase` in `tests/Pest.php`.
- Reuses: S03-S04 layout, components and named routes; the post card component now receives a `Post` model.

### S06 — Sprint : CRUD complet et tests Pest
- Week: W3 — Type: B — Tag: `lab-03b`
- Learning outcomes:
  1. Complete the post CRUD: `edit`, `update` (`@method('PUT')`, unique slug ignoring the current post), `destroy` (`@method('DELETE')` with confirmation form).
  2. Add a column with a new migration instead of editing an old one (`excerpt`, nullable).
  3. Add a local query scope (`scopePublished`) and use it on the home page and the archive (/posts stays the working list until S11).
  4. Cover store, update and destroy with Pest tests using `assertDatabaseHas` / `assertDatabaseMissing`.
- Key commands: `php artisan make:migration add_excerpt_to_posts_table --table=posts`, `php artisan migrate`, `php artisan test --filter=Post`.
- Assessment focus: all 7 actions work, tests green, no edited old migrations.
- Reuses: S05 model, controller, views, first test.

## Week 4

### S07 — Relations Eloquent, factories et seeders
- Week: W4 — Type: A — Tag: `lab-04`
- Learning outcomes:
  1. Model 1:N relationships (`Category` hasMany `Post`, `User` hasMany `Post`) with typed return values.
  2. Model an N:N relationship with a `post_tag` pivot (composite unique index, timestamps, `withTimestamps()`), and use `attach`, `detach`, `sync`.
  3. Write factories (with states such as `published()`) and seeders, and rebuild the database with `migrate:fresh --seed`.
  4. Detect an N+1 problem (`Model::preventLazyLoading(! app()->isProduction());` in `AppServiceProvider::boot()`) and fix it with `with()`.
- Key commands: `php artisan make:model Category -mfs`, `php artisan make:model Tag -mfs`, `php artisan make:factory PostFactory --model=Post`, `php artisan make:migration create_post_tag_table`, `php artisan make:migration add_user_and_category_to_posts_table --table=posts`, `php artisan migrate:fresh --seed`, `php artisan db:seed`.
- Design decision: `user_id` and `category_id` are added as nullable foreign keys (`nullOnDelete`) because posts exist before authentication; posts get an author from S11 onwards.
- Reuses: S05-S06 `Post` model, CRUD and tests; the default `UserFactory` and `DatabaseSeeder`.

### S08 — Sprint : catégories, tags et chargement anticipé
- Week: W4 — Type: B — Tag: `lab-04b`
- Learning outcomes:
  1. Add category selection (`<select>`) and tag selection (checkboxes + `sync`) to the post forms.
  2. Build public pages "posts by category" and "posts by tag" with route model binding on slug (`{category:slug}`).
  3. Use `withCount` and eager loading on every list page.
  4. Test relationships using factories in Pest.
  5. (Optional, not graded) Switch the application to PostgreSQL through `.env` (`DB_CONNECTION=pgsql`), rebuild the data with `migrate:fresh --seed`, and explain why migrations, models and tests did not change.
- Key commands: `php artisan migrate:fresh --seed`, `php artisan route:list`, `php artisan test`; optional part: `php -m`, `php artisan config:clear`, `php artisan db:show`.
- Optional PostgreSQL part: a bonus at the end of the Independent Challenge, never in the Assessment Checklist. The tag `lab-04b` is produced on SQLite; `.env` is not committed, so the repository is identical for students who skip the bonus. Students switch back to SQLite if the install fails.
- Assessment focus: no lazy-loading violation, seeders produce a realistic dataset, forms persist relations, tests green. The PostgreSQL bonus is not graded.
- Reuses: S07 models, pivot, factories, seeders.

## Week 5

### S09 — Form Requests, messages flash, middleware et exceptions
- Week: W5 — Type: A — Tag: `lab-05`
- Learning outcomes:
  1. Move validation into `StorePostRequest` / `UpdatePostRequest` and use `$request->validated()` (unique slug ignoring the current post on update).
  2. Show flash messages with `->with('success', ...)` and a reusable Blade alert component.
  3. Write a custom middleware (`EnsureSiteIsWritable`: blocks write requests with 503 when a config flag is on) and register it as an alias in `bootstrap/app.php`.
  4. Customize exception handling in `bootstrap/app.php` (`withExceptions` render callback for 404 on posts) and custom error views in `resources/views/errors/`. The callback must return `null` for API/JSON requests (`if ($request->is('api/*') || $request->expectsJson()) { return null; }`, the same rule as the skeleton's `shouldRenderJsonWhen`) so S13 API errors stay JSON, even when a browser opens an `/api/*` URL.
- Key commands: `php artisan make:request StorePostRequest`, `php artisan make:request UpdatePostRequest`, `php artisan make:middleware EnsureSiteIsWritable`, `php artisan vendor:publish --tag=laravel-errors`, `php artisan config:clear`.
- Reuses: S05-S08 controller, forms, `@error`, alert component from S04.
- Note: no auth-based middleware yet (`admin` alias arrives in S11).

### S10 — Sprint : validation et robustesse de l'application
- Week: W5 — Type: B — Tag: `lab-05b`
- Learning outcomes:
  1. Apply Form Requests and flash messages to Category and Tag CRUD.
  2. Customize validation messages and attribute names in French.
  3. Test validation errors (`assertSessionHasErrors`) and the middleware (503 when the flag is on) with Pest.
  4. Provide custom 404 and 503 pages matching the layout.
- Key commands: `php artisan make:controller CategoryController --resource --model=Category`, `php artisan make:request StoreCategoryRequest`, `php artisan test`.
- Assessment focus: no validation left in controllers, no try/catch in actions, error pages styled, tests green.
- Reuses: S09 Form Requests, middleware, exception handling.

## Week 6

### S11 — Authentification manuelle, Gates et Policies
- Week: W6 — Type: A — Tag: `lab-06`
- Learning outcomes:
  1. Implement register, login and logout manually with `Hash::make`, `Auth::attempt`, `$request->session()->regenerate()`, `Auth::logout()`, session invalidation and token regeneration.
  2. Protect routes with the `auth` and `guest` middleware and attach new posts to `$request->user()`.
  3. Add a `role` column and define Gates in `AppServiceProvider::boot()` (`manage-categories`), used with `@can` and `Gate::authorize()`.
  4. Write a `PostPolicy` (authors edit their own posts, admins edit all) and apply it with `Gate::authorize('update', $post)` or the `can:update,post` middleware.
- Key commands: `php artisan make:controller Auth/LoginController`, `php artisan make:controller Auth/RegisterController`, `php artisan make:migration add_role_to_users_table --table=users`, `php artisan make:policy PostPolicy --model=Post`.
- Laravel 13 note: the base `App\Http\Controllers\Controller` in a fresh app has no `AuthorizesRequests` trait, so `$this->authorize()` fails unless the trait is added; the codelab uses `Gate::authorize()` (verify on a lab PC).
- Reuses: S07 `User` relation, S09 middleware registration and Form Requests.

### S12 — Sprint : autorisations et comparaison avec le starter kit Livewire
- Week: W6 — Type: B — Tag: `lab-06b`
- Learning outcomes:
  1. Apply policies to every post action and gates to category/tag management.
  2. Create an `EnsureUserIsAdmin` middleware, register it as the `admin` alias in `bootstrap/app.php`, and protect the category/tag back office with it.
  3. Test authorization with Pest (`actingAs`, `assertForbidden`, `assertRedirect(route('login'))`).
  4. Compare the manual implementation with the official Livewire starter kit (never Breeze). The kit is shown as an instructor demo in the last 30 minutes (one project, projected); students reproduce it as homework only if their connection allows, since `npm install` for a whole group can exhaust the lab bandwidth.
  5. Document the comparison (features, files, security measures) in the README.
- Key commands: `php artisan make:middleware EnsureUserIsAdmin`, `php artisan test`, `laravel new mini-cms-livewire` (Livewire starter kit, outside the main repository), `composer run dev`.
- Assessment focus: no unauthorized action reachable, authorization tests green, comparison table in README.
- Reuses: S11 auth, gates, policies. The Livewire project is not committed to the main repository.

## Week 7

### S13 — Première API REST : install:api et API Resources
- Week: W7 — Type: A — Tag: `lab-07`
- Learning outcomes:
  1. Run `php artisan install:api` and explain what it adds (`routes/api.php`, Sanctum, `/api` prefix).
  2. Expose read-only endpoints with `Route::apiResource(...)->only(['index', 'show'])` and an `Api\PostController`.
  3. Shape responses with `PostResource` / `CategoryResource`, `whenLoaded`, ISO 8601 dates and paginated collections.
  4. Call the API with Postman and `curl.exe` (not the PowerShell `curl` alias) with `Accept: application/json`, and read 404/422 JSON errors.
- Key commands: `php artisan install:api`, `php artisan make:controller Api/PostController --api --model=Post`, `php artisan make:resource PostResource`, `php artisan make:resource CategoryResource`, `php artisan route:list --path=api`.
- Reuses: S07-S08 models and eager loading, S09 exception handling.
- Note: filters, JSON assertions, write endpoints and tokens are not taught here (S14).

### S14 — API complète et authentification par jetons Sanctum
- Week: W7 — Type: A, guided codelab in a B slot (merge of the former S14 sprint and S15 codelab; last class of the course, see Calendar buffer) — Tags: `lab-07b` (end of Étape 3), `lab-08` (end of session)
- Learning outcomes:
  1. Add read endpoints for categories (`Api\CategoryController`, index and show, reusing the S13 `CategoryResource`) and the query-string filters `?category=` and `?tag=` on `/api/posts`.
  2. Test the read API with Pest (`getJson`, `assertJsonPath`, `assertJsonCount`, `assertJsonStructure`).
  3. Add `HasApiTokens` to `User`, issue tokens with `createToken('api')->plainTextToken` from an `Api\AuthController` login endpoint, and revoke the current token on logout.
  4. Protect the post write endpoints (`store`, `update`, `destroy`) with `auth:sanctum`, reusing `StorePostRequest` / `UpdatePostRequest` and `PostPolicy` (JSON 401/403/422). Authorization stays in the Form Request's `authorize()` (session-guidelines.md, section 8); `destroy` calls `Gate::authorize('delete', $post)` first.
  5. Test protected endpoints with `Sanctum::actingAs` in Pest and call them with `Authorization: Bearer <token>` in Postman.
- Guided steps (120 min):

  | Étape | Content | Min |
  |---|---|---|
  | 1 | `Api\CategoryController` (index, show) with `CategoryResource`, `withCount` | 15 |
  | 2 | `?category=` and `?tag=` filters on `Api\PostController` (exact slug match, eager loading kept) | 20 |
  | 3 | Pest read-API tests (`getJson`, JSON assertions), commit, tag `lab-07b` | 20 |
  | 4 | `HasApiTokens`, `Api\AuthController` login and logout | 25 |
  | 5 | `auth:sanctum` write routes reusing Form Requests and `PostPolicy` | 25 |
  | 6 | Pest tests with `Sanctum::actingAs` (401, 403, 422, 201) | 15 |

- Independent Challenge (30 min, hints only): a Postman collection with `{{base_url}}` and `{{token}}` variables (the login request stores the token), exported to `docs/postman/`.
- Moved to S16 homework (former S14 sprint tasks): `Api\TagController` (index, show) with `TagResource`, tests for the `?tag=` filter, and a `curl.exe` Bearer example in the README.
- Key commands: `php artisan make:controller Api/CategoryController --api --model=Category`, `php artisan make:controller Api/AuthController`, `php artisan route:list --path=api`, `php artisan test --filter=Api`, `curl.exe -H "Accept: application/json" "http://localhost:8000/api/posts?category=<slug>"`.
- Portability: the `?category=` and `?tag=` filters compare slugs exactly, so they behave the same on SQLite and PostgreSQL.
- Deliverable: push `main`, `lab-07b` and `lab-08`; the Livrable panel links to `docs/session-16.html` and states the S16 deadline.
- Assessment focus: consistent JSON shape and pagination, filters work, 401 without a token, 403 on another author's post, 422 on an invalid body, API tests green, both tags on GitHub.
- Reuses: S13 API layer, S11 policies, S09 Form Requests and JSON exception rule, S07-S08 relations and eager loading.

## Week 8

### S15 — retired (merged into S14)
- No class, no page, no index card, no tag of its own: `lab-08` is produced at the end of S14.

### S16 — Livraison finale du projet
- Week: W8 — Type: B, take-home (no class) — Tag: `lab-08b`
- `docs/session-16.html` keeps the 7-part structure of a B session: Prerequisites & Objectives; Environment check = clean clone; Concept Brief = rubric and deadline; "Guided Steps" = submission tasks with checkpoints; Independent Challenge = optional bonus; graded Assessment Checklist; Deliverable. Durations on the page are estimates for home work. No Quiz éclair.
- Learning outcomes:
  1. Finish the S14 homework: `Api\TagController` (index, show) with `TagResource`, tests for the `?tag=` filter.
  2. Deliver a working Mini-CMS from a clean clone (`composer install`, `npm install`, `.env`, `php artisan key:generate`, `migrate:fresh --seed`, `php artisan test`), on SQLite.
  3. Write the final README: setup (bash and PowerShell), features, API documentation (endpoints, login, Bearer token, error codes, one `curl.exe` example), screenshots, and a "Choix d'architecture" section answering, in the student's own words: why API writes go through `PostPolicy`; why `preventLazyLoading` is on; why the API uses tokens instead of the session.
  4. Record a screencast demo (4 minutes maximum) of the web and API features, linked in the README.
- Key commands: `php artisan make:resource TagResource`, `php artisan make:controller Api/TagController --api --model=Tag`, `git clone`, `composer install`, `copy .env.example .env` (PowerShell) / `cp .env.example .env` (bash), `php artisan key:generate`, `php artisan migrate:fresh --seed`, `php artisan test`, `git tag lab-08b`, `git push origin --tags`.
- Grading: the instructor clones the repository at `lab-08b` and runs it on SQLite, whatever database the student used locally. The tag must be on GitHub before the deadline announced in S14. Rubric: functionality, code conventions, tests, Git history and tags, README (including "Choix d'architecture"), demo video.
- Reuses: the whole project.

---

## Concept Index (first introduction)

A session must not use a concept listed here with a later session number.

| Concept | First session |
|---|---|
| MVC, request lifecycle, closure routes, `composer run dev`, Node/Vite toolchain | S01 |
| Git remote, push, tags, README | S02 |
| Named routes, route parameters, controllers, `<x-layout>`, `abort(404)` | S03 |
| Components with `@props`, `routeIs()` | S04 |
| Migrations, Eloquent, `casts()`, Tinker, route model binding, `paginate()`, create/read CRUD, `$request->validate()`, Pest | S05 |
| Update/delete CRUD, `@method`, add-column migrations, local scopes | S06 |
| 1:N, N:N, pivot, factories, seeders, eager loading, `preventLazyLoading` | S07 |
| Slug route binding, `withCount`, `sync` in forms, PostgreSQL driver switch (optional) | S08 |
| Form Requests, flash messages, custom middleware, `withExceptions` | S09 |
| Validation messages, `assertSessionHasErrors` | S10 |
| Manual auth, `auth`/`guest` middleware, Gates, Policies | S11 |
| `admin` middleware alias, Livewire starter kit (comparison only) | S12 |
| `install:api`, `apiResource`, API Resources, Postman, `curl.exe` | S13 |
| API filters, JSON assertions, Sanctum tokens, `auth:sanctum`, `Sanctum::actingAs` | S14 |

S15 is retired. S16 introduces no new concept.

## Points to verify on a lab PC before the course

- Whether `laravel new` initializes a Git repository and makes a first commit automatically (affects S01 deliverable).
- `laravel new` prompts after the frontend-stack question (testing framework, database, Laravel Boost, npm). The first two prompts were verified on 30 Sep 2026.
- `make:test` output format with Pest installed.
- `install:api` prompts (migrations for `personal_access_tokens`).
- Livewire starter kit install flow and internet bandwidth for `npm install` in S12.
- Node.js LTS present on every lab PC (S01 blocker if missing).
- VS Code and its `code` command available on every lab PC.
- Node.js and Git for Windows installers runnable with the lab accounts' rights.
- S07 add-column migration with foreign keys (`foreignId()->nullable()->constrained()->nullOnDelete()`) runs cleanly on SQLite.
- `cmdkey /delete:git:https://github.com` removes the stored GitHub credential on the lab PCs.
- PostgreSQL for Windows on a student laptop: installer rights, `pdo_pgsql` and `pgsql` available in the php.net build, creation of the `mini_cms` database, and `migrate:fresh --seed` on PostgreSQL with the S07 migrations.
- Where the official php.net PowerShell command installs PHP, and whether Composer-Setup.exe adds the Composer global `vendor\bin` folder to the PATH.
- S14: resolved in source (19 Nov 2026): the actingAs token is a mock, so the logout test logs in with a real token.
- S14: whether the 120-minute guided part fits with a real group, since it now carries the former S14 sprint and the S15 codelab.

## Calendar buffer

No buffer week is planned. If a holiday or exam period removes a session, merge the B session into the next A session (sprint tasks become homework) rather than dropping content; tags keep their numbering.

Applied on 19 Nov 2026: the course ends with S14. The former S14 sprint and S15 codelab were merged into one guided S14 class (`lab-07b` and `lab-08`); the sprint tasks that did not fit (tag endpoints, tag filter tests, `curl.exe` documentation) moved to S16, which became a take-home final submission (`lab-08b`) graded from a clean clone and a screencast instead of a live soutenance.
