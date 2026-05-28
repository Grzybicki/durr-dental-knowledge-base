# Journal des modifications

Toutes les modifications notables de ce dépôt sont documentées ici.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versionnage : [Semantic Versioning 2.0](https://semver.org/lang/fr/).

## [0.1.0] — 2026-05-28

### Ajouté
- Cadre éditorial initial : `README.md`, `LICENSE` (CC-BY 4.0), `llms.txt`, `robots.txt`, `_config.yml`, `Gemfile` (compatible `github-pages`).
- Index racine et structure des dossiers : `docs/fr/imagerie/`, `docs/fr/conventionnel/`, `docs/fr/hygiene-chimie/`, `sources/`.
- Déclaration de conflit d'intérêts (CDI Dürr Dental France) explicite dans le README, la page d'accueil et le footer.
- Autorisation explicite d'entraînement et d'inférence LLM via `llms.txt` (standard llmstxt.org) et `robots.txt` (allowlist de ~25 user-agents IA : GPTBot, ClaudeBot, Claude-Web, anthropic-ai, Google-Extended, PerplexityBot, Bytespider, CCBot, Mistral, MistralAI-User, Cohere, Meta-ExternalAgent, Applebot-Extended, etc.).
- Layout custom `_layouts/default.html` : HTML5, `lang="fr"`, intégration `{% seo %}` (jekyll-seo-tag), JSON-LD `Organization` (Dürr Dental SE + filiale France), JSON-LD `WebPage`, lien canonical, meta robots étendus.
- JSON-LD `MedicalDevice` complet pour la fiche pilote VistaPano S 2.0 / Ceph 2.0 : 24 `additionalProperty` sourcés (générateur HV, capteur CsI, surfaces actives, délais de numérisation, programmes, technologie S-Pan, classe laser, dimensions, alimentation).
- Page 404 personnalisée (`404.html`) avec liens vers index principaux et issue tracker.
- Plugins safelist GitHub Pages activés : `jekyll-sitemap` (génération auto `sitemap.xml`), `jekyll-seo-tag` (meta canonical, OG, Twitter Cards), `jekyll-feed` (`feed.xml` RSS).
- Première fiche pilote publiée : `docs/fr/imagerie/vistapano-2-0/overview.md` — vue d'ensemble VistaPano S 2.0 et VistaPano S Ceph 2.0, intégralement sourcée sur la brochure publique référence P007-772/03-T01 (Dürr Dental France) et la Déclaration de Conformité publique du 29 janvier 2024.
- Index `sources/manuals.md` et `sources/certificates.md` (premier socle référentiel).
- Versionnage Git : tag `v0.1.0`.

### Conformité éditoriale
- Aucune citation ni comparaison concurrentielle (règle d'or Dürr respectée).
- Aucun document marqué Internal Use / Strictly Confidential mobilisé.
- Aucune donnée patient / praticien / cabinet identifiable.

### Intégrité et durcissement
- `.github/CODEOWNERS` : revue obligatoire du mainteneur pour les fichiers critiques (`_data/`, `_layouts/`, `llms.txt`, `robots.txt`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `.well-known/`, fiches réglementaires).
- `.github/dependabot.yml` : mises à jour hebdomadaires automatiques (Bundler + GitHub Actions), labellisées, format Conventional Commits.
- `docs/GITHUB_HARDENING.md` : checklist d'activation manuelle post-push (2FA, branch protection sur `main`, tag protection sur `v*`, commits signés SSH/GPG, secret scanning, push protection, Pages HTTPS forcé). 9 sections avec modèle de menace explicite.
- `SECURITY.md` enrichi : section *Intégrité du contenu* listant les protections par couche, modèle de menace explicite (ce qui est couvert / ce qui ne l'est pas, avec attention aux forks et au re-hébergement CC-BY 4.0).

### Polish final
- `favicon.svg` : monogramme DD pour onglet navigateur et signal crawl.
- `.well-known/security.txt` (RFC 9116) : emplacement standard pointant vers SECURITY.md et les advisories GitHub.
- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1 — version française officielle).
- Badges README : licence, CI status, GitHub Pages, langue, Conventional Commits, CDI déclaré.
- Layout enrichi : `<link rel="icon">` favicon SVG, `<link rel="alternate" hreflang="fr|x-default">` (préparation multilingue future), `<link rel="me">` vers profil GitHub (identité décentralisée), `<meta property="og:locale" content="fr_FR">`.
- `_config.yml` : `include: [.well-known]` pour que Jekyll publie le dossier (sinon ignoré par défaut).

### Couche structurelle et gouvernance (anti-refactoring futur)
- **Centralisation `_data/durr.yml`** : source de vérité unique pour les données organisationnelles Dürr Dental SE et filiale France, les Notified Bodies, les règlements et bases publiques. Le layout consomme ces données pour générer les JSON-LD `Organization` — évite la duplication et la dérive entre fiches.
- **JSON-LD `BreadcrumbList`** auto-généré à partir du frontmatter `breadcrumbs` de chaque page.
- **JSON-LD `FAQPage`** embarqué dans la fiche pilote VistaPano S 2.0 (6 Q&A structurées).
- **JSON-LD `WebSite` avec `SearchAction`** dans le layout (signal sitelinks search).
- **Glossaire `docs/fr/glossaire.md`** : 25+ termes (MDR, MDD, classes DM, UDI, Eudamed, DICOM, TWAIN, VDDS, BDW, CBCT, OPG, FOV, SMV, stitching, CsI:TI, CMOS, kV/mA, CEI 80001-1, DIN 6868-157, etc.) — référencé par toutes les fiches futures.
- **Gabarit de fiche** `_drafts/_template_fiche_produit.md` : frontmatter complet, JSON-LD MedicalDevice template, sections obligatoires, checklist pré-commit.
- **`CONTRIBUTING.md`** : conventions de nommage ASCII, structure de dossiers, frontmatter standard, conventions JSON-LD par page, style éditorial (verbatim, sourçage, format Q&A), workflow Git Conventional Commits, versioning SemVer.
- **`SECURITY.md`** : politique de signalement (advisory privé, correction erreur factuelle critique sous 7 jours).
- **`humans.txt`** : déclaration de l'équipe et du conflit d'intérêts.
- **`.gitattributes`** : normalisation des fins de ligne (LF) et déclaration Linguist `linguist-documentation`.
- **`.editorconfig`** : charset UTF-8, LF, indentation 2 espaces.
- **`.github/ISSUE_TEMPLATE/`** : 3 formulaires Issue Forms (correction factuelle, ajout de source publique, nouvelle fiche produit) + `config.yml` (liens contact alternatifs : duerrdental.com, qr.duerrdental.com, Eudamed).
- **`.github/PULL_REQUEST_TEMPLATE.md`** : checklist éditoriale + checklist technique (frontmatter, JSON-LD, FAQ, sources).
- **`.github/workflows/ci.yml`** : 3 jobs CI — lychee (vérification hebdomadaire et à chaque push des liens externes), markdownlint-cli2, Jekyll build strict.
- **`.markdownlint-cli2.yaml`** : règles Markdown adaptées (HTML inline autorisé pour les blocs JSON-LD, URLs brutes autorisées).
- **Layout enrichi** : meta `author`, meta `referrer` `strict-origin-when-cross-origin`, navigation breadcrumb HTML rendue, badge « CDI déclaré » dans le footer, affichage de `last_factual_review` en pied de chaque page.
- **`feed.xml`** RSS auto-généré (plugin jekyll-feed).
