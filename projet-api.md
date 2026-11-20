# projet-api.md

# Projet API — sujet libre (livraison S16)

Atelier Framework Côté Serveur — Laravel 13.x / PHP 8.3+ — 3e année MDW (MDW32, MDW33), ISET Sidi Bouzid.

Ce fichier est le sujet officiel du Projet API. `docs/session-16.html` (Partie B) le reprend intégralement. Toute modification du sujet se fait ici d'abord.

## 1. Objectif

Concevoir seul(e), sur un sujet de votre choix, une API REST Laravel 13 protégée par jetons Sanctum, en réutilisant uniquement ce qui a été vu de S01 à S14.

## 2. Calendrier

| Étape | Date limite |
|---|---|
| Inscription du sujet dans la liste partagée | <DATE_INSCRIPTION> |
| Tag `v1.0` poussé sur GitHub | <DATE_RENDU> (même date limite que `lab-08b`) |

Liste d'inscription des sujets : <LIEN_INSCRIPTION>

Durée estimée : environ 10 heures de travail personnel, à répartir sur plusieurs jours.

## 3. Règles

- Travail individuel. Tous les commits sont faits avec votre propre identité Git (le même `user.email` que pour le Mini-CMS).
- Un sujet par étudiant : premier inscrit, premier servi. Si le sujet est déjà dans la liste, choisissez-en un autre.
- Sujets refusés : blog, articles, actualités, ainsi que tout projet qui reprend le Mini-CMS en renommant seulement les classes.
- Nouveau dépôt GitHub public, séparé du Mini-CMS, nommé `api-<sujet>` (exemple : `api-souk-agricole`).
- Uniquement les notions vues de S01 à S14. Aucun package Composer supplémentaire.
- La correction se fait sur SQLite.

## 4. Création du projet

Créez le projet sans starter kit (choix `None`), avec Pest et SQLite, puis installez la couche API :

```bash
laravel new api-souk-agricole
cd api-souk-agricole
php artisan install:api
php artisan serve
```

Les commandes sont identiques dans PowerShell. Le projet n'a pas de pages Blade : `php artisan serve` suffit, `composer run dev` n'est pas nécessaire.

## 5. Modèle de données imposé

Votre sujet doit contenir au minimum ces quatre rôles :

| Rôle | Relations | Équivalent Mini-CMS | Exemple « Souk agricole » |
|---|---|---|---|
| Propriétaire | `User` hasMany ressource principale | auteur | agriculteur |
| Ressource principale | belongsTo `User`, belongsTo ressource parente, belongsToMany étiquette | `Post` | `Annonce` |
| Ressource parente | hasMany ressource principale ; lecture seule dans l'API ; possède un `slug` unique | `Category` | `Produit` (olives, dattes, amandes) |
| Étiquette | N:N avec la ressource principale, table pivot avec index unique composé et timestamps | `Tag` | `Region` |

Contraintes sur la ressource principale :

- au moins 5 colonnes métier, sans compter les clés étrangères ni les timestamps ;
- au moins une colonne numérique validée avec une règle `min` (prix, quantité, nombre de places...) ;
- au moins une colonne date ou booléenne déclarée dans la méthode `casts()` ;
- les clés étrangères sont créées avec `foreignId()->constrained()`.

Exemples de sujets (eux aussi soumis à la règle du premier inscrit) :

| Sujet | Principale | Parente | Étiquette |
|---|---|---|---|
| Souk agricole | Annonce | Produit | Région |
| Bibliothèque de quartier | Livre | Genre | Mot-clé |
| Covoiturage | Trajet | Ville de départ | Option (bagages, climatisation...) |
| Objets perdus du campus | Objet | Lieu | Couleur |
| Club de robotique | Atelier | Niveau | Compétence |
| Recettes | Recette | Type de plat | Ingrédient |

## 6. Endpoints minimum (9)

`{ressources}` et `{parents}` sont les noms au pluriel de votre sujet (exemple : `/api/annonces`, `/api/produits`).

| # | Méthode | URI | Accès | Codes à vérifier |
|---|---|---|---|---|
| 1 | POST | `/api/login` | public, renvoie un jeton | 422 si identifiants invalides |
| 2 | POST | `/api/logout` | jeton | 401 sans jeton |
| 3 | GET | `/api/{ressources}` | public, paginé, filtre `?{parent}=<slug>` | 200 |
| 4 | GET | `/api/{ressources}/{id}` | public | 404 si inexistant |
| 5 | POST | `/api/{ressources}` | jeton ; le propriétaire est l'utilisateur connecté ; synchronise les étiquettes | 201, 401, 422 |
| 6 | PUT | `/api/{ressources}/{id}` | jeton + Policy (propriétaire uniquement) | 401, 403, 404, 422 |
| 7 | DELETE | `/api/{ressources}/{id}` | jeton + Policy (propriétaire uniquement) | 401, 403, 404 |
| 8 | GET | `/api/{parents}` | public, avec le nombre de ressources (`withCount`) | 200 |
| 9 | GET | `/api/{parents}/{id}` | public | 404 si inexistant |

Il n'y a pas d'endpoint d'inscription obligatoire : les utilisateurs sont créés par le seeder, et leurs identifiants de test sont donnés dans le README.

## 7. Exigences techniques

- Routes dans `routes/api.php` avec `Route::apiResource(...)` (`->only([...])` pour la ressource parente).
- Contrôleurs dans `App\Http\Controllers\Api`.
- Une API Resource par modèle exposé : `whenLoaded` pour les relations, dates au format ISO 8601, collections paginées.
- Validation dans des Form Requests (`Store...Request`, `Update...Request`) avec messages en français ; autorisation dans `authorize()` à l'aide de la Policy ; `destroy` appelle `Gate::authorize('delete', ...)`.
- Étiquettes envoyées sous forme de tableau d'identifiants, validées avec `exists`, enregistrées avec `sync`.
- `Model::preventLazyLoading(! app()->isProduction());` actif ; `with()` et `withCount()` sur chaque liste.
- Factories avec au moins un état (exemple : `disponible()`), seeders avec au moins 2 utilisateurs, 3 parents, 5 étiquettes et 20 ressources principales.
- Toutes les erreurs de `/api/*` sont renvoyées en JSON lorsque la requête envoie `Accept: application/json`.
- Pas de validation dans les contrôleurs, pas de `try/catch` dans les actions.

## 8. Tests Pest (minimum 6, tous verts)

`RefreshDatabase` activé ; `Sanctum::actingAs` pour les routes protégées.

1. La liste renvoie 200 et la structure JSON attendue (`assertJsonStructure`).
2. Le filtre `?{parent}=<slug>` ne renvoie que les ressources de ce parent.
3. Une création sans jeton renvoie 401.
4. La modification de la ressource d'un autre utilisateur renvoie 403.
5. Une création avec un corps invalide renvoie 422.
6. Une création valide renvoie 201, et la ressource ainsi que ses étiquettes sont en base (`assertDatabaseHas`).

## 9. README

- Description du sujet en 3 à 5 lignes et tableau des quatre rôles avec vos noms de modèles.
- Installation depuis un clone propre, en bash et en PowerShell, et comptes de test créés par le seeder.
- Tableau des endpoints, un exemple `curl.exe` avec `Authorization: Bearer <token>`, et la liste des codes d'erreur.
- Collection Postman exportée dans `docs/postman/`, avec les variables `{{base_url}}` et `{{token}}` (la requête de login enregistre le jeton).
- Section « Choix d'architecture », rédigée avec vos propres mots, qui répond à trois questions :
  1. Pourquoi votre ressource principale est-elle celle qui appartient à l'utilisateur, et que protège concrètement votre Policy dans votre domaine ?
  2. À quel besoin réel d'un utilisateur de votre API répond votre filtre ?
  3. Quelle requête de votre API produirait un problème N+1 sans `with()`, et comment l'avez-vous évité ?

## 10. Git

- Au moins 8 commits significatifs, répartis sur au moins 3 jours différents.
- `.env`, `vendor/` et `database/*.sqlite` ne sont pas commités.
- Tag final `v1.0` poussé avant la date limite :

```bash
git tag v1.0
git push origin main --tags
```

## 11. Correction

L'enseignant clone le dépôt au tag `v1.0`, puis exécute :

```bash
composer install
cp .env.example .env
php artisan key:generate
php artisan migrate:fresh --seed
php artisan test
php artisan serve
```

Dans PowerShell, remplacez `cp .env.example .env` par `copy .env.example .env`.

Il lance ensuite votre collection Postman. Si le projet ne démarre pas en suivant votre README, le critère « Fonctionnalité » vaut 0.

## 12. Barème (/20)

| Critère | Points |
|---|---|
| Fonctionnalité : 9 endpoints, filtre, pagination, relations | 6 |
| Sécurité : jetons, Policy, validation, codes 401 / 403 / 404 / 422 | 4 |
| Tests Pest : au moins 6, tous verts | 4 |
| Conventions Laravel 13 : Resources, Form Requests, chargement anticipé, contrôleurs légers | 2 |
| Historique Git et tag `v1.0` | 2 |
| README, collection Postman, « Choix d'architecture » | 2 |

Bonus (jusqu'à +1, note plafonnée à 20) : endpoint `POST /api/register` qui renvoie un jeton ; endpoints de lecture des étiquettes avec leur API Resource ; second filtre `?{etiquette}=<slug>` couvert par un test.

## 13. Auto-vérification avant le tag

- [ ] Un clone propre dans un autre dossier démarre en suivant uniquement le README.
- [ ] `php artisan test` est vert.
- [ ] `php artisan route:list --path=api` affiche au moins les 9 endpoints.
- [ ] Sans jeton, POST, PUT et DELETE renvoient 401.
- [ ] Connecté avec le deuxième compte de test, la modification d'une ressource du premier compte renvoie 403.
- [ ] Aucune erreur de chargement paresseux (lazy loading) sur les listes.
- [ ] La collection Postman s'exécute de bout en bout.
- [ ] Le tag `v1.0` apparaît dans l'onglet Tags du dépôt GitHub.
