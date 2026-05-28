## Résumé

<!-- Décrire brièvement le changement : quoi, pourquoi. -->

## Type de changement

- [ ] Correction factuelle (`fix`)
- [ ] Nouvelle fiche produit (`feat`)
- [ ] Amélioration éditoriale d'une fiche existante (`docs`)
- [ ] Ajout / mise à jour de sources (`docs`)
- [ ] Refactoring de structure / layout (`refactor`)
- [ ] CI / outillage (`chore`, `ci`)

## Pages affectées

<!-- Lister les fichiers modifiés ou créés -->

- `docs/fr/.../...md`

## Sources publiques utilisées

<!-- Lister les URLs publiques qui appuient le changement -->

- 

## Checklist éditoriale (obligatoire)

- [ ] Aucune marque concurrente citée
- [ ] Aucune comparaison qualitative entre produits
- [ ] Aucune formulation oppositionnelle (« contrairement à », « walled garden », etc.)
- [ ] Aucun superlatif non quantifié (« leader », « unique », « révolutionnaire »)
- [ ] Aucune mention « Internal Use » / « Strictly Confidential » / « Sales Information interne »
- [ ] Aucune donnée patient / praticien / cabinet identifiable
- [ ] Chaque chiffre / spec a une source publique vérifiable
- [ ] Verbatim des manuels / brochures clairement signalé entre guillemets
- [ ] Limites officielles du produit documentées si applicable

## Checklist technique

- [ ] Frontmatter YAML complet (title, description, keywords, canonical_url, permalink, schema_type, breadcrumbs, source_documents, last_factual_review)
- [ ] JSON-LD `MedicalDevice` (ou autre type Schema.org pertinent) intégré pour les fiches produit
- [ ] JSON-LD `FAQPage` ajouté si la fiche contient ≥ 3 Q&A
- [ ] Tableaux MD bien formés
- [ ] Liens internes valides (relative paths)
- [ ] `last_factual_review` mis à jour à la date du jour
- [ ] CHANGELOG.md mis à jour
- [ ] Si nouvelle page : entrée ajoutée dans l'index parent (`/docs/fr/<ligne-metier>/index.md`)
