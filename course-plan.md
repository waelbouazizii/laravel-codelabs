# course-plan.md

Atelier Framework Côté Serveur — Laravel 13.x / PHP 8.3+ — 3e année MDW (MDW32, MDW33), ISET Sidi Bouzid.
16 sessions of about 3h10, 2 per week over 8 weeks. This file is the sequencing authority: a session may only use concepts introduced in the same or an earlier session (see the Concept Index at the end).

## Evolving student project: Mini-CMS

Every student builds one application, `mini-cms`, from S01 to S16, in one GitHub repository.

| Entity | Introduced | Purpose |
|---|---|---|
| Static pages (home, a-propos) | S01-S04 | Routing, controllers, Blade layout |
| `Post` (title, slug, body, is_published, published_at) | S05 | First model, CRUD |
| `Category` (1:N with Post), `Tag` (N:N via `post_tag`) | S07 | Relationships |
| `User` as author, `role` column (`author` / `admin`) | S07 (author link), S11 (auth, role) | Ownership, authorization |
| Read-only JSON API `/api/posts`, `/api/categories` | S13 | API Resources |
| Token-protected write API | S15 | Sanctum |

Final result: a small publishing platform with public pages, an authenticated back office (authors manage their own posts, admins manage categories and tags), a JSON API, and a green Pest suite.

## Conventions for the whole course

- Session file: `docs/session-XX.html`, XX = 01 to 16.
- Session A (odd numbers) = guided codelab. Session B (even numbers) = applied sprint + assessment on the same repository. B sessions keep the 7-part structure from CLAUDE.md; in a B session, "Guided Steps" are sprint tasks with checkpoints, and the Assessment Checklist is graded.
- Git tags: Session A of week W produces `lab-0W`, Session B produces `lab-0Wb` (week 1: `lab-01`, `lab-01b`; week 8: `lab-08`, `lab-08b`).
- Stack: `laravel new mini-cms` with no starter kit (Blade frontend stack), Pest, SQLite. Run with `composer run dev`.
- Windows lab PCs: every command that differs between bash and PowerShell is given in both.
- Repositories are public (portfolio). To limit copying, the Git history is graded: small meaningful commits between tags, one tag per session, commits authored with the student's own identity.
- Toolchain: PHP 8.3+, Composer, Laravel installer (php.new or Herd), Node.js LTS + npm (required by Vite / `composer run dev`, not installed by php.new), Git for Windows, VS Code (the `code` command is used from S01).

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
| S14 | W7 | B | Sprint : API complète, tests et collection Postman | lab-07b |
| S15 | W8 | A | Authentification API par jetons Sanctum | lab-08 |
| S16 | W8 | B | Soutenance du projet final | lab-08b |

---

## Week 1

### S01 — Architecture MVC et premier projet Laravel 13
- Week: W1 — Type: A — Tag: `lab-01` (local only; pushed in S02)
- Learning outcomes:
  1. Describe the MVC pattern and the Laravel request lifecycle (`public/index.php` -> `bootstrap/app.php` -> routing -> controller/closure -> response).
  2. Verify a working PHP 8.3+ / Composer / Laravel installer toolchain (php.new or Laravel Herd) and Node.js LTS + npm on Windows. Fallback if Node is missing: `php artisan serve` without Vite (no Tailwind in S01).
  3. Create a Laravel 13 project with SQLite and Pest, and run it with `composer run dev`.
  4. Navigate the Laravel 13 skeleton (no `app/Http/Kernel.php`, no `routes/api.php`, configuration in `bootstrap/app.php`).
  5. Write a first closure route returning a string and a view.
- Key commands: `php -v`, `composer -V`, `laravel --version`, `node -v`, `npm -v`, `git --version`, `laravel new mini-cms`, `composer run dev`, `php artisan --version`, `php artisan route:list`, `php artisan about`.
- Git (copy-paste only, explained in S02): `git config user.name` and `git config user.email` run inside the project (local, not `--global`, because lab PCs are shared), `git init` (only if the installer did not create the repository), `git add -A`, `git commit -m "lab-01"`, `git tag lab-01`. The email is the student's GitHub account email, or the one they will create the account with before S02. No GitHub account is needed in S01, and students do not log into GitHub on lab PCs.
- Reuses: nothing (first session). Assumes PHP basics and HTML/CSS from years 1-2.

### S02 — Git, GitHub et publication du projet
- Prerequisite: every student arrives with a GitHub account whose email matches the `git config user.email` set in S01.
- Week: W1 — Type: B — Tag: `lab-01b`
- Learning outcomes:
  1. Explain the working tree / staging area / commit / tag model and read `git status` and `git log --oneline`.
  2. Explain why `.env`, `vendor/`, `node_modules/` and `database/*.sqlite` are ignored and verify `.gitignore`.
  3. Authenticate to GitHub from a Windows lab PC with Git Credential Manager (HTTPS) and push the project and its tags.
  4. Write a README with setup instructions and screenshots.
- Key commands: `git status`, `git log --oneline --decorate`, `git branch -M main`, `git remote add origin <url>`, `git push -u origin main`, `git push origin --tags`, `git tag -n`.
- Sprint: add a second closure route `/a-propos` returning a view (closure routes only, as in S01), README (project description, install steps bash + PowerShell, screenshots in `screenshots/`), push `lab-01` and `lab-01b`.
- End-of-session hygiene (mandatory on shared lab PCs): remove the `git:https://github.com` entry from Windows Credential Manager (`cmdkey /delete:git:https://github.com` or Control Panel > Credential Manager) so the next group cannot push to the student's repository.
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
  3. Add a local query scope (`scopePublished`) and use it on the public list.
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
- Key commands: `php artisan migrate:fresh --seed`, `php artisan route:list`, `php artisan test`.
- Assessment focus: no lazy-loading violation, seeders produce a realistic dataset, forms persist relations, tests green.
- Reuses: S07 models, pivot, factories, seeders.

## Week 5

### S09 — Form Requests, messages flash, middleware et exceptions
- Week: W5 — Type: A — Tag: `lab-05`
- Learning outcomes:
  1. Move validation into `StorePostRequest` / `UpdatePostRequest` and use `$request->validated()` (unique slug ignoring the current post on update).
  2. Show flash messages with `->with('success', ...)` and a reusable Blade alert component.
  3. Write a custom middleware (`EnsureSiteIsWritable`: blocks write requests with 503 when a config flag is on) and register it as an alias in `bootstrap/app.php`.
  4. Customize exception handling in `bootstrap/app.php` (`withExceptions` render callback for 404 on posts) and custom error views in `resources/views/errors/`. The callback must return `null` for API/JSON requests (`if ($request->expectsJson()) { return null; }`) so S13 API errors stay JSON.
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
- Note: write endpoints and tokens are not taught here (S15).

### S14 — Sprint : API complète, tests et collection Postman
- Week: W7 — Type: B — Tag: `lab-07b`
- Learning outcomes:
  1. Add read endpoints for categories and tags, and query-string filters (`?category=`, `?tag=`).
  2. Test the API with Pest (`getJson`, `assertJsonPath`, `assertJsonCount`, `assertJsonStructure`).
  3. Export a Postman collection into the repository (`docs/postman/`).
- Key commands: `php artisan make:controller Api/CategoryController --api --model=Category`, `php artisan test --filter=Api`, `curl.exe -H "Accept: application/json" http://127.0.0.1:8000/api/posts`.
- Assessment focus: consistent JSON shape, pagination, API tests green, collection committed.
- Reuses: S13 API layer.

## Week 8

### S15 — Authentification API par jetons Sanctum
- Week: W8 — Type: A — Tag: `lab-08`
- Learning outcomes:
  1. Add `HasApiTokens` to `User` and issue tokens with `createToken('api')->plainTextToken` from an `Api\AuthController` login endpoint.
  2. Protect write endpoints with `auth:sanctum` and revoke the current token on logout.
  3. Reuse `PostPolicy` and Form Requests for API writes (JSON 401/403/422).
  4. Test protected endpoints with `Sanctum::actingAs` in Pest and with `Authorization: Bearer <token>` in Postman and `curl.exe`.
- Key commands: `php artisan make:controller Api/AuthController`, `php artisan route:list --path=api`, `php artisan test`.
- Reuses: S11 policies, S09 Form Requests, S13-S14 API.

### S16 — Soutenance du projet final
- Week: W8 — Type: B — Tag: `lab-08b`
- Learning outcomes:
  1. Deliver a working Mini-CMS from a clean clone (`composer install`, `npm install`, `.env`, `php artisan key:generate`, `migrate:fresh --seed`).
  2. Demonstrate web and API features in a 5-minute demo and answer questions on the architecture.
  3. Present a green Pest suite and a final README (setup, features, API documentation, screenshots).
- Key commands: `git clone`, `composer install`, `copy .env.example .env` (PowerShell) / `cp .env.example .env` (bash), `php artisan key:generate`, `php artisan migrate:fresh --seed`, `php artisan test`, `git tag lab-08b`, `git push origin --tags`.
- Assessment focus: final rubric (functionality, code conventions, tests, Git history and tags, README, demo).
- Timing: 5-minute demos for ~30 students take about 2h30 plus transitions. Run demos in parallel pairs or cap at 4 minutes + 1 minute questions; students who do not demo are graded from a recorded screencast linked in the README.
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
| Slug route binding, `withCount`, `sync` in forms | S08 |
| Form Requests, flash messages, custom middleware, `withExceptions` | S09 |
| Validation messages, `assertSessionHasErrors` | S10 |
| Manual auth, `auth`/`guest` middleware, Gates, Policies | S11 |
| `admin` middleware alias, Livewire starter kit (comparison only) | S12 |
| `install:api`, `apiResource`, API Resources, Postman, `curl.exe` | S13 |
| API filters, JSON assertions | S14 |
| Sanctum tokens, `auth:sanctum` | S15 |

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

## Calendar buffer

No buffer week is planned. If a holiday or exam period removes a session, merge the B session into the next A session (sprint tasks become homework) rather than dropping content; tags keep their numbering.
