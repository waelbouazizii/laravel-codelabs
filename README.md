# Atelier Framework Cote Serveur

Course site for **Atelier Framework Cote Serveur** (Laravel 13, 3e annee MDW,
ISET Sidi Bouzid, Prof. Wael Bouaziz). It is a static site with no build
step, published straight from this repository via GitHub Pages.

## Structure

- `docs/` - the published site (GitHub Pages serves `main` /docs). Contains
  `index.html` (course home page) and one `session-XX.html` per session.
- `templates/codelab-template.html` - the skeleton every session is copied
  from.
- `scripts/check.py` - validates every `docs/*.html` file (no emojis, no
  broken step links, no incomplete `...` code blocks).
- `CLAUDE.md` - the permanent rules for authoring sessions in this repo.

## Preview locally

```
python -m http.server -d docs 8000
```

Then open `http://localhost:8000` in a browser.

## Validate before committing

```
python scripts/check.py
```
