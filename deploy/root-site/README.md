# Bundle dépôt racine `grzybicki.github.io` (GEO — audit A1)

## Pourquoi

Ce projet est un **project site** GitHub Pages, servi sous
`https://grzybicki.github.io/durr-dental-knowledge-base/`. Or les crawlers
(GPTBot, ClaudeBot, PerplexityBot, Googlebot…) **ne lisent `robots.txt`,
`llms.txt` et `.well-known/security.txt` qu'à la racine de l'hôte** :
`https://grzybicki.github.io/robots.txt`.

Tant qu'aucun dépôt ne sert la racine `grzybicki.github.io`, tout le travail
de `robots.txt` (autorisations bots IA) et de `llms.txt` reste **sans effet**.

## Solution

Créer un **dépôt utilisateur** `Grzybicki/grzybicki.github.io` (nom exact
obligatoire) qui sert la racine, portant les 3 fichiers de ce dossier.

### Étapes

```bash
cd D:/kDrive/GitHub
git init grzybicki.github.io
cd grzybicki.github.io
# copier robots.txt, llms.txt et .well-known/ depuis ce dossier deploy/root-site/
cp -r "../durr-dental-knowledge-base/deploy/root-site/"{robots.txt,llms.txt,.well-known} .
# une page d'accueil minimale renvoyant vers la KB (optionnel mais recommandé)
git add -A && git commit -m "root site: robots.txt + llms.txt + security.txt"
git branch -M main
gh repo create Grzybicki/grzybicki.github.io --public --source=. --push
```

Puis, dans les **Settings → Pages** du nouveau dépôt, activer GitHub Pages
sur la branche `main`.

### Vérification

Après déploiement (~1 min), vérifier :

- `https://grzybicki.github.io/robots.txt` → doit renvoyer le robots.txt ci-dessous
- `https://grzybicki.github.io/llms.txt` → doit renvoyer le pointeur vers la KB
- `https://grzybicki.github.io/.well-known/security.txt`

### Alternative

Un **domaine personnalisé** (ex. `durr-kb.fr`) sur le dépôt de la KB rendrait
aussi robots.txt/llms.txt visibles à la racine, sans dépôt séparé.

## Contenu du bundle

- `robots.txt` — copie du robots.txt de la KB (couverture bots IA + `Sitemap:`
  pointant vers le sitemap de la KB sous `/durr-dental-knowledge-base/`).
- `llms.txt` — pointeur racine renvoyant vers le `llms.txt` complet et le
  `llms-full.txt` de la KB.
- `.well-known/security.txt` — contact sécurité (RFC 9116).
