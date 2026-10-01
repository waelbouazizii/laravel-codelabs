# Laravel 13 Conventions – Atelier Framework Côté Serveur

Reference for all generated sessions. When a snippet here conflicts with older tutorials, this file wins. If something is not covered and you are unsure it exists in Laravel 13, say so explicitly instead of guessing.

## 1. Versions and environment

| Item | Rule |
|---|---|
| Framework | Laravel 13.x (released March 2026). Pin `laravel/framework:^13.0`. |
| PHP | 8.3 minimum. Verify with `php -v`. |
| Install | php.new (one-line installer for PHP + Composer + Laravel installer) or Laravel Herd on Windows. Copy the current Windows command from https://php.new rather than hardcoding a version. |
| New project | `laravel new app-name` (choose: no starter kit, Blade frontend stack, Pest, SQLite). Verified 30 Sep 2026: the installer asks `Do you want to use a starter kit? (yes/no) [no]`, then `Which frontend stack do you want to build on? [Blade]`. |
| Run dev | `composer run dev` (serves app + Vite together). Fallback: `php artisan serve` and `npm run dev` in two terminals. Verified working on Windows (30 Sep 2026). Students open the `APP_URL` (`http://localhost:8000`), not the Vite URL (`http://localhost:5173`); the `[laravel:fonts]` "fontaine" warning is harmless. |
| Database | SQLite by default (`database/database.sqlite`, created by the installer). MySQL only if explicitly taught via `.env`. |
| Tests | Pest. Run with `php artisan test`. |
| AI tooling (instructor only) | Laravel Boost: `composer require laravel/boost --dev` then `php artisan boost:install`. |

Lab PCs run Windows: give PowerShell equivalents where commands differ (paths with `\`, `copy` vs `cp`, `New-Item` vs `touch`).

## 2. Project skeleton facts (what does NOT exist anymore)

- No `app/Http/Kernel.php`. Middleware, exceptions and routing are configured in `bootstrap/app.php`.
- No `routes/api.php` in a new app until `php artisan install:api` is run.
- No `app/Console/Kernel.php`. Scheduling lives in `routes/console.php`.
- Laravel Breeze and Jetstream receive no further updates. Do not use them. Official starter kits: Livewire, React, Vue, Svelte (Fortify-based).

## 3. Routing

```php
// routes/web.php
use App\Http\Controllers\PostController;
use Illuminate\Support\Facades\Route;

Route::get('/', fn () => view('welcome'))->name('home');

Route::get('/posts/{post}', [PostController::class, 'show'])->name('posts.show');

Route::resource('posts', PostController::class);

Route::middleware('auth')->group(function () {
    Route::get('/dashboard', fn () => view('dashboard'))->name('dashboard');
});
```

Rules: callable array syntax `[Controller::class, 'method']` only (never `'PostController@index'`), always name routes (from S03 onwards: before S03, `course-plan.md` sequencing wins and routes stay unnamed), prefer route model binding over manual `find()`.

## 4. Migrations

```php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('posts', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->foreignId('category_id')->nullable()->constrained()->nullOnDelete();
            $table->string('title');
            $table->string('slug')->unique();
            $table->text('body');
            $table->boolean('is_published')->default(false);
            $table->timestamp('published_at')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('posts');
    }
};
```

Pivot table: singular model names in alphabetical order (`post_tag`), two `foreignId()->constrained()->cascadeOnDelete()` columns, composite unique index, `timestamps()` if using `->withTimestamps()`.

## 5. Models

```php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Post extends Model
{
    use HasFactory;

    protected $fillable = ['title', 'slug', 'body', 'is_published', 'published_at', 'category_id'];

    protected function casts(): array
    {
        return [
            'is_published' => 'boolean',
            'published_at' => 'datetime',
        ];
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function tags(): BelongsToMany
    {
        return $this->belongsToMany(Tag::class)->withTimestamps();
    }
}
```

Rules: `$fillable` property (not `$guarded = []`), `casts()` method (not `$casts` property), return types on every relationship. Laravel 13 also accepts attributes such as `#[Fillable([...])]`; mention once as an alternative, never mix both styles in one file. Use eager loading (`Post::with('user', 'tags')`) to avoid N+1.

Generator: `php artisan make:model Post -mfsc` (migration, factory, seeder, controller) or `--resource` / `-r` for a resource controller.

## 6. Controllers and validation

```php
namespace App\Http\Controllers;

use App\Http\Requests\StorePostRequest;
use App\Models\Post;

class PostController extends Controller
{
    public function index()
    {
        $posts = Post::with('user')->latest()->paginate(10);

        return view('posts.index', compact('posts'));
    }

    public function store(StorePostRequest $request)
    {
        $post = $request->user()->posts()->create($request->validated());

        return redirect()->route('posts.show', $post)->with('success', 'Article créé.');
    }

    public function show(Post $post)
    {
        return view('posts.show', compact('post'));
    }
}
```

```php
namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StorePostRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true;
    }

    public function rules(): array
    {
        return [
            'title' => ['required', 'string', 'max:255'],
            'slug' => ['required', 'string', 'max:255', 'unique:posts,slug'],
            'body' => ['required', 'string'],
        ];
    }
}
```

Rules: validation in Form Requests (`php artisan make:request`), use `$request->validated()`, no try/catch in controller actions. Rely on route model binding, `findOrFail()`, and centralized exception handling. Wrap only genuinely failing external operations (HTTP calls, file storage) in try/catch.

## 7. Blade

- Layouts via components: `resources/views/components/layout.blade.php` used as `<x-layout>...</x-layout>`, with `{{ $slot }}` and named slots. Show `@extends/@section` once as the classic alternative.
- Always `{{ }}` (escaped). `{!! !!}` only with an explicit security note.
- Forms: `@csrf`, `@method('PUT')`, `@error('field')`, `old('field')`.
- Flash: `@if (session('success')) ... @endif`.
- Tailwind through the app's Vite setup: `@vite(['resources/css/app.css', 'resources/js/app.js'])`.

## 8. Middleware and exceptions (bootstrap/app.php)

```php
use App\Http\Middleware\EnsureUserIsAdmin;
use Illuminate\Foundation\Application;
use Illuminate\Foundation\Configuration\Exceptions;
use Illuminate\Foundation\Configuration\Middleware;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        commands: __DIR__.'/../routes/console.php',
        health: '/up',
    )
    ->withMiddleware(function (Middleware $middleware): void {
        $middleware->alias([
            'admin' => EnsureUserIsAdmin::class,
        ]);
    })
    ->withExceptions(function (Exceptions $exceptions): void {
        //
    })->create();
```

Create middleware with `php artisan make:middleware EnsureUserIsAdmin`. Use it as `->middleware('admin')`.

## 9. Authentication and authorization (W6)

- Session A: manual auth with `Auth::attempt($credentials)`, `$request->session()->regenerate()`, `Auth::logout()`, `Hash::make()`, routes protected by `auth` and `guest` middleware.
- Gates in `App\Providers\AppServiceProvider::boot()`: `Gate::define('manage-posts', fn (User $user) => $user->role === 'admin');` then `@can('manage-posts')`, `Gate::authorize(...)`.
- Policies: `php artisan make:policy PostPolicy --model=Post`, auto-discovered; use `$this->authorize('update', $post)` or `can:update,post` middleware.
- Session B: `laravel new` with the Livewire starter kit, to compare with the manual version. Never Breeze.

## 10. API (W7-W8)

```powershell
php artisan install:api
```

This creates `routes/api.php`, installs Sanctum and registers the API routes (prefix `/api`).

```php
// routes/api.php
use App\Http\Controllers\Api\PostController;
use Illuminate\Support\Facades\Route;

Route::apiResource('posts', PostController::class)->only(['index', 'show']);

Route::middleware('auth:sanctum')->group(function () {
    Route::apiResource('posts', PostController::class)->except(['index', 'show']);
});
```

```php
namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class PostResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'title' => $this->title,
            'author' => $this->whenLoaded('user', fn () => $this->user->name),
            'created_at' => $this->created_at?->toIso8601String(),
        ];
    }
}
```

Sanctum tokens: add `use Laravel\Sanctum\HasApiTokens;` to `User`, issue with `$user->createToken('api')->plainTextToken`, send as `Authorization: Bearer <token>` with `Accept: application/json`. Test with Postman and with `curl.exe` on Windows (not the PowerShell `curl` alias).

## 11. Tests (Pest)

```php
use App\Models\User;

it('shows the home page', function () {
    $this->get('/')->assertOk();
});

it('lets an authenticated user create a post', function () {
    $user = User::factory()->create();

    $this->actingAs($user)
        ->post('/posts', ['title' => 'Hello', 'slug' => 'hello', 'body' => 'Text'])
        ->assertRedirect();

    $this->assertDatabaseHas('posts', ['slug' => 'hello']);
});
```

Use `RefreshDatabase` (configured in `tests/Pest.php`).

## 12. Forbidden or outdated patterns

- `app/Http/Kernel.php`, `$routeMiddleware`, `RouteServiceProvider` edits
- Laravel Breeze, Jetstream
- `'Controller@method'` string routes
- `protected $casts = [...]` in new code (use `casts()`)
- `$guarded = []` as a shortcut
- try/catch in every controller action
- `{!! !!}` without explanation
- `php artisan serve` as the only way to run (prefer `composer run dev`)
- Any emoji in generated content

## 13. Points to verify before teaching

- Installer prompts of `laravel new` after the frontend-stack question (testing framework, database, Laravel Boost, npm): confirm on a lab PC. The first two prompts were verified on 30 Sep 2026.
- Current php.new Windows command and the PHP version it installs.
- Livewire starter kit install flow for W6 Session B.
