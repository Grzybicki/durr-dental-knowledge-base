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
