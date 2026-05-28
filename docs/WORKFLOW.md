# Workflow éditorial — chaîne de validation pas-à-pas

Ce document décrit le **processus complet et déterministe** de rédaction et de publication
d'une fiche dans ce dépôt. L'objectif est un workflow **propre, sûr, fiable et non
contestable** : chaque étape produit une preuve numérique vérifiable.

## Principes

- **Aucune assertion sans source publique vérifiable** (URL directe obligatoire).
- **Aucune modification sans trace** (commit signé, CHANGELOG mis à jour, PR documentée).
- **Aucune publication sans validation déterministe** (pre-commit + CI bloquent les
  non-conformités).
- **Toute correction est elle-même tracée** (commit, CHANGELOG, release note).

## Pré-requis (une seule fois)

```bash
# Cloner le dépôt et installer les hooks
git clone https://github.com/Grzybicki/durr-dental-knowledge-base.git
cd durr-dental-knowledge-base

# Python 3.10+
python -m pip install pyyaml pre-commit

# Activer les hooks
pre-commit install

# (Optionnel mais recommandé) signature des commits via SSH
git config commit.gpgsign true
git config tag.gpgSign true
git config gpg.format ssh
git config user.signingkey ~/.ssh/id_ed25519_signing.pub
```

## Étape 1 — Collecte et qualification des sources

Avant toute rédaction, identifier au moins **3 sources publiques officielles** pour
chaque assertion factuelle de la future fiche :

| Catégorie de source | Origine | Niveau d'autorité |
|---|---|---|
| Notice utilisateur / installation publique | `qr.duerrdental.com/<code>` | Très haut |
| Brochure commerciale publique | Page produit FR/FR Dürr Dental | Haut |
| Déclaration de Conformité publique | Centre de téléchargements + Eudamed | Très haut |
| Page produit officielle | `duerrdental.com/fr/FR/produits/.../<produit>/` | Haut |
| Publication scientifique peer-reviewed | PubMed, BDJ Open, PMC | Très haut |
| Partenaire technologique officiel | audaxceph.com, exocad.com, sicat.com | Moyen-haut |
| Eudamed | `ec.europa.eu/tools/eudamed/` | Très haut (réglementaire) |
| FDA 510(k) | `accessdata.fda.gov/.../pmn.cfm` | Très haut (réglementaire) |

**Pour chaque source identifiée** :

1. Vérifier qu'elle est **publique** (accessible sans authentification).
2. Vérifier qu'elle n'est PAS marquée *Internal Use*, *Strictly Confidential*,
   *Sales Information interne* ou équivalent.
3. **Déclencher un archivage Wayback Machine** :
   ```
   curl -A "Mozilla/5.0" -s -o /dev/null -w "%{http_code}\n" \
     "https://web.archive.org/save/<URL_DE_LA_SOURCE>"
   ```
4. Noter l'URL canonique + l'URL `web.archive.org/web/2026*/<URL>` dans la liste
   des sources.

## Étape 2 — Rédaction

1. Copier le gabarit :
   ```bash
   cp _drafts/_template_fiche_produit.md docs/fr/<ligne-metier>/<produit>/overview.md
   ```
2. Renseigner le frontmatter complet (title, description, keywords, canonical_url,
   permalink, schema_type, breadcrumbs, source_documents, last_factual_review, license).
3. Rédiger chaque section en respectant la convention de style :
   - **Verbatim entre guillemets** pour les citations du manuel / de la brochure.
   - **Source explicite** à chaque chiffre ou affirmation : « selon la brochure
     publique référence P007-772/03-T01, page 11 ».
   - **Première occurrence d'un acronyme expansée** (« CBCT — Cone Beam Computed
     Tomography »).
   - **Tableaux** pour les caractéristiques techniques.
   - **Répéter le nom complet du produit** dans chaque section (robustesse chunking
     RAG).

## Étape 3 — Validation locale déterministe

Avant tout commit, lancer la validation :

```bash
python scripts/validate.py
```

Le script vérifie automatiquement :

- ✅ Frontmatter YAML conforme (champs obligatoires présents, `schema_type` connu).
- ✅ Aucune mention de marque concurrente (règle d'or Dürr).
- ✅ Aucune mention « Internal Use » / « Strictly Confidential ».
- ✅ Aucune donnée patient / praticien / cabinet identifiable.
- ✅ Chaque entrée `source_documents` a une URL ou une note explicite.
- ✅ Tous les blocs JSON-LD inline sont du JSON valide.
- ✅ Aucun lien interne cassé.

**Code de retour 0** = aucune erreur, commit autorisé.
**Code de retour 1** = erreurs bloquantes, corriger avant commit.

## Étape 4 — Commit (signé)

```bash
git add docs/fr/<ligne-metier>/<produit>/overview.md
git add CHANGELOG.md  # toujours mis à jour
git commit -S -m "feat(<ligne-metier>): add <produit> overview page"
```

Les pre-commit hooks s'exécutent automatiquement et **rejettent le commit** si :

- `validate.py` retourne un code 1.
- `markdownlint` détecte des problèmes de format.
- Un PDF / DOCX / PPTX est inclus dans le commit (propriété intellectuelle).
- Le frontmatter YAML est syntaxiquement invalide.
- La taille d'un fichier dépasse 500 ko.

## Étape 5 — Pull Request

Pour les modifications non triviales (toute nouvelle fiche, toute correction
réglementaire, toute modification du layout) :

```bash
git checkout -b feat/<produit>-overview
git push origin feat/<produit>-overview
gh pr create
```

Le template PR contient :

- Checklist éditoriale (règle d'or, sources publiques, pas de PII).
- Checklist technique (frontmatter, JSON-LD, FAQ, sources, CHANGELOG).
- Liste des sources publiques utilisées.

## Étape 6 — Vérification CI

Trois jobs CI doivent passer avant merge :

| Job | Vérification |
|---|---|
| `validate-repo` | Exécute `scripts/validate.py --warn-as-error` |
| `lychee` | Vérifie tous les liens externes (200, 301, 302) |
| `markdownlint` | Style Markdown conforme à `.markdownlint-cli2.yaml` |
| `jekyll-build` | Build Jekyll strict (`--strict_front_matter`) |

## Étape 7 — Code review (CODEOWNERS)

Pour les fichiers critiques (`_data/`, `_layouts/`, `llms.txt`, `robots.txt`,
`LICENSE`, `SECURITY.md`, fiches réglementaires), une approbation de
`@Grzybicki` (mainteneur) est obligatoire — gérée par `.github/CODEOWNERS`.

## Étape 8 — Merge et déploiement

- Merge en **squash + commit signé**, message Conventional Commits.
- GitHub Pages déploie automatiquement depuis `main`.
- Vérification post-déploiement :
  ```bash
  curl -I https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/<...>/
  ```

## Étape 9 — Release et tag

Pour une release versionnée :

```bash
# Mettre à jour CHANGELOG.md (section [X.Y.Z] dated)
git add CHANGELOG.md
git commit -S -m "chore(release): vX.Y.Z"
git tag -s vX.Y.Z -m "vX.Y.Z — <résumé>"
git push origin main --tags
```

Le tag est **signé GPG/SSH** et **immuable** (tag protection sur `v*`).

## Étape 10 — Correction d'erreur (procédure ouverte)

Si une erreur factuelle est signalée (Issue avec label `factual-correction`) :

1. **Sous 48 h** : reproduction du problème, recherche de la source authoritative.
2. **Sous 7 j** : commit de correction signé, mise à jour du CHANGELOG, mention
   explicite dans une release note publique.
3. **Sous 15 j** (max engagé) : réponse écrite à l'Issue avec lien vers le commit
   correctif et l'archive Wayback de la nouvelle source.

## Garanties procédurales (résumé)

| Propriété | Garantie technique |
|---|---|
| **Traçabilité** | Git log + commits signés (GPG/SSH) + CODEOWNERS |
| **Vérifiabilité** | URL publique directe par source + archive Wayback |
| **Non-contestation** | Pre-commit + CI = aucun commit non-conforme dans l'historique |
| **Pas de PII** | Regex automatique détecte Dr/Dre/Pr + Nom propre |
| **Pas d'interne** | Regex automatique détecte « Internal Use » / « Strictly Confidential » |
| **Pas de concurrence** | Regex automatique détecte les marques bannies |
| **Reproductibilité** | Gemfile + plugins safelisted + Jekyll strict build |
| **Immuabilité des releases** | Tag protection `v*` + commits signés |
| **Intégrité du dépôt** | Branch protection `main` + 2FA + secret scanning |
| **Récupération** | Mirror Codeberg/GitLab recommandé (cf. SECURITY.md) |

## Liens

- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — conventions détaillées.
- [`SECURITY.md`](../SECURITY.md) — politique de signalement.
- [`STATEMENT_OF_INTEGRITY.md`](../STATEMENT_OF_INTEGRITY.md) — engagements
  procéduraux du mainteneur.
- [`GITHUB_HARDENING.md`](GITHUB_HARDENING.md) — réglages GitHub à activer.
- [`.pre-commit-config.yaml`](../.pre-commit-config.yaml) — hooks pre-commit.
- [`scripts/validate.py`](../scripts/validate.py) — script de validation.
- [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) — workflow CI.
