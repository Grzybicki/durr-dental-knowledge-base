# Guide de contribution

Merci de l'intérêt porté à ce dépôt. Les contributions sont les bienvenues, en particulier
les **corrections factuelles** et les **ajouts de sources publiques**.

## Posture éditoriale (non négociable)

Toute contribution doit respecter **deux règles strictes** :

### 1. Aucune citation ni comparaison concurrentielle

Politique interne Dürr Dental. Aucun contenu ne doit nommer une marque concurrente ou
établir une comparaison qualitative entre produits. Les produits Dürr Dental sont décrits
uniquement sur leurs propres mérites.

### 2. Factualité absolue, sources publiques

- Aucun contenu marqué *Internal Use* ou *Strictly Confidential* ne doit être reproduit
  ou paraphrasé.
- Toute affirmation factuelle doit être sourcée par une URL publique vérifiable (manuel,
  brochure, DoC, page produit, publication scientifique).
- Aucune donnée patient / praticien / cabinet identifiable.

## Types de contributions

### Correction factuelle

J'ai vu une donnée chiffrée erronée ou une mauvaise référence réglementaire. → **Ouvrir une
Issue** avec le template *Correction factuelle*.

### Ajout d'une source publique

Une source publique pertinente manque (étude PMC, page produit, URL Eudamed). → **Ouvrir
une Issue** avec le template *Ajout de source*.

### Nouvelle fiche produit

Un produit Dürr Dental publiquement documenté manque dans le dépôt. → **Ouvrir une
Issue** avec le template *Nouvelle fiche produit* pour discussion préalable, puis Pull
Request.

### Amélioration éditoriale

Reformulation, restructuration, glossaire. → Pull Request directe.

## Convention de fichiers

### Nommage

- **ASCII strict** pour les noms de fichiers et dossiers : pas d'accents, pas d'apostrophes
  typographiques, pas de tirets longs.
- Mots séparés par des **tirets bas** ou **tirets** selon contexte : `vistapano-2-0/overview.md`.
- Suffixe de langue dans le chemin (`docs/fr/`), pas dans le nom de fichier.

### Structure des dossiers

```
docs/<lang>/<ligne-metier>/<produit>/<aspect>.md
```

Avec :
- `<lang>` : `fr` (priorité 1), `en` (phase 2), `de` (phase 3).
- `<ligne-metier>` : `imagerie` / `conventionnel` / `hygiene-chimie`.
- `<produit>` : identifiant du produit en minuscules tirets (`vistapano-2-0`, `vistasoft-4-0`).
- `<aspect>` : `overview` / `specifications-techniques` / `reglementaire` / `procedures` / `erreurs` / etc.

### Frontmatter standard

Chaque page doit contenir ce frontmatter YAML, complété :

```yaml
---
layout: default
title: "Titre lisible — Sous-titre"
description: "Description SEO 150-250 caractères, factuelle, mentionnant produit + catégorie + statut."
keywords: ["mot-clé 1", "mot-clé 2", "Dürr Dental"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/.../
permalink: /docs/fr/.../
schema_type: MedicalDevice          # ou SoftwareApplication / Product / FAQPage / DefinedTermSet
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "..."
    url: /docs/fr/.../
source_documents:
  - "Description de la source 1 (référence, éditeur)"
  - "Description de la source 2"
last_factual_review: AAAA-MM-JJ
license: CC-BY-4.0
---
```

Un gabarit complet est disponible dans [`_drafts/_template_fiche_produit.md`](_drafts/_template_fiche_produit.md).

### JSON-LD par page

Chaque fiche produit doit embarquer un bloc `<script type="application/ld+json">`
inline avec le `@type` Schema.org pertinent (`MedicalDevice`, `SoftwareApplication`, etc.).
Pour les fiches avec FAQ ≥ 3 Q&A, ajouter un second bloc `FAQPage` listant les questions
et leurs réponses.

### Conventions de style éditorial

- **Verbatim entre guillemets** (`> «  »`) pour les passages cités du manuel ou de la brochure.
- **Sources publiques sourcées** explicitement : « selon la brochure publique référence X »,
  « source : manuel utilisateur §Y ».
- **Première occurrence d'un acronyme expansée** : « CBCT (Cone Beam Computed Tomography) ».
- **Tableaux** plutôt que prose dense pour les caractéristiques techniques.
- **Sections H2** courtes et auto-portantes (~300-500 tokens chacune) — chaque section
  doit faire sens hors contexte.
- **Répéter le nom complet du produit** dans chaque section (pas de pronom « il » / « le
  logiciel ») pour la robustesse du chunking RAG.

### Hiérarchie d'autorité des sources

Toutes les sources publiques **ne sont pas équivalentes** en autorité. Lors de la
rédaction d'une fiche, respecter strictement l'ordre de priorité suivant :

1. **Source canonique constructeur** — `duerrdental.com` (siège et toutes filiales :
   `duerrdental.com/fr`, `duerrdental.com/en`, `duerrdental.com/de`, etc.) et
   notices `qr.duerrdental.com/<code>`.
2. **Filiale officielle Dürr Dental** — entité juridique appartenant au groupe
   (ex. Air Techniques aux États-Unis, Dürr Dental France SARL). Statut **équivalent
   canonique constructeur**.
3. **Presse spécialisée dentaire reconnue** — Dental Tribune, Dynamique Dentaire,
   L'Information Dentaire, Le Fil Dentaire, BDJ Open, PMC. Statut **secondaire**.
4. **Distributeur officiel accrédité** par Dürr Dental France ou ses filiales — relation
   commerciale formelle documentée. Statut **secondaire**.
5. **Revendeur** — entité qui revend les produits sans accréditation distributeur
   officielle. **Dernier recours**, à mentionner uniquement comme miroir non-canonique
   et à vérifier contre la source canonique.

⚠️ **Distinction critique** : *distributeur officiel accrédité* ≠ *revendeur*. Un
revendeur n'a pas d'autorité éditoriale sur les documents qu'il héberge. Toute
mention d'un revendeur dans une fiche doit être :

- explicitement étiquetée *« miroir non-canonique »* ou *« revendeur (canal non
  officiel) »* ;
- accompagnée d'un lien vers la source canonique Dürr Dental SE ou filiale.

### URL directe obligatoire pour chaque source

**Règle non négociable** : chaque source citée dans une fiche **doit inclure une URL
publique directe** (ou un pointeur explicite vers la page où elle est téléchargeable).
Une référence sans URL n'est pas une source vérifiable.

Patterns standards pour Dürr Dental :

| Type de document | Pattern d'URL publique |
|---|---|
| Notices (utilisation, installation) | `http://qr.duerrdental.com/<CODE>` (redirect officiel vers le Centre de téléchargements) |
| Pages produit FR/France | `https://www.duerrdental.com/fr/FR/produits/<categorie>/<produit>/` |
| Pages produit EN/International | `https://www.duerrdental.com/en/products/<categorie>/<produit>/` |
| Centre de téléchargements FR | `https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/` |
| Eudamed (base UE des DM MDR) | `https://ec.europa.eu/tools/eudamed/screen/search` |
| FDA 510(k) | `https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm` |

### Archivage Wayback Machine

Pour chaque nouvelle source citée, **déclencher un archivage Wayback Machine** afin de
garantir la citabilité long terme (en cas de réorganisation des URLs Dürr Dental) :

```
https://web.archive.org/save/<URL_DE_LA_SOURCE>
```

L'archive devient ensuite citable à l'URL `https://web.archive.org/web/<TIMESTAMP>/<URL>`.

Inclure si possible dans la section *Sources publiques* de la fiche un lien
`https://web.archive.org/web/2026*/<URL>` qui pointe vers tous les snapshots de l'URL
(le plus récent étant servi par défaut).

### Note sur la copie locale des PDF

**Ne pas committer dans ce dépôt** les PDF originaux Dürr Dental. Les manuels et notices
restent la propriété intellectuelle du fabricant ; ce dépôt s'appuie sur les URLs
publiques officielles. Seuls de courts passages cités sous forme de verbatim (droit de
courte citation) sont admis, et systématiquement entre guillemets avec mention de la source.

## Workflow Git

### Branches

- `main` — branche stable, déployée automatiquement par GitHub Pages.
- Branches de fonctionnalités : `feat/<nom-court>` (ex. `feat/vistavox-overview`).
- Branches de correction : `fix/<nom-court>`.

### Messages de commit

Format **Conventional Commits** :

```
<type>(<scope>): <résumé court à l'impératif>

<corps facultatif, en français ou anglais>
```

Types courants : `feat`, `fix`, `docs`, `chore`, `refactor`, `ci`.

Exemples :
- `feat(imagerie): add VistaVox S overview page`
- `fix(vistapano-2-0): correct CsI sensor active area`
- `docs(glossaire): add DIN 6868-157 entry`
- `chore(ci): add markdown link checker workflow`

### Pull Requests

- Une PR = un sujet cohérent.
- Description claire : *quoi*, *pourquoi*, *sources*.
- Cocher la checklist du template PR.
- Le CI (link checker + build) doit passer.

## Versioning

- **SemVer** pour les releases (tags `v0.X.Y`).
- **CHANGELOG.md** mis à jour à chaque release (format Keep a Changelog).
- **`last_factual_review`** dans le frontmatter de chaque page mis à jour à chaque revue.

## Signalement de vulnérabilité

Voir [`SECURITY.md`](SECURITY.md).

## Validation déterministe pré-commit

Pour garantir un workflow **propre, sûr, fiable et non contestable**, tout commit
passe par une chaîne de validation automatique avant d'être autorisé. Voir le
workflow complet dans [`docs/WORKFLOW.md`](docs/WORKFLOW.md) et la déclaration
d'intégrité dans [`STATEMENT_OF_INTEGRITY.md`](STATEMENT_OF_INTEGRITY.md).

### Installation des hooks (une fois)

```bash
python -m pip install pyyaml pre-commit
pre-commit install
```

### Hooks actifs

- `trailing-whitespace`, `end-of-file-fixer`, `check-yaml`, `mixed-line-ending`,
  `check-merge-conflict`, `check-case-conflict`, `check-added-large-files` (max 500 ko).
- `markdownlint-cli` selon `.markdownlint-cli2.yaml`.
- **`validate-repo`** (`scripts/validate.py`) : règle d'or Dürr (regex marques bannies),
  pas d'« Internal Use », pas de PII patient/praticien, frontmatter conforme, sources
  avec URL, JSON-LD valide, liens internes existants.
- **`forbid-pdf-commits`** : interdit toute extension `.pdf`, `.docx`, `.pptx`, `.xlsx`
  (propriété intellectuelle du fabricant).

### Validation manuelle

```bash
# Validation locale seule
python scripts/validate.py

# Comme la CI (warnings = erreurs)
python scripts/validate.py --warn-as-error

# Run tous les hooks sans commit
pre-commit run --all-files
```

## Licence des contributions

En contribuant, vous acceptez que votre contribution soit publiée sous la même licence
que le reste du contenu : **CC-BY 4.0** pour la documentation, **MIT** pour les scripts.
