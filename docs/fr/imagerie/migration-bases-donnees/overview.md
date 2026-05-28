---
layout: default
title: "Migration vers VistaSoft 4.0 — bases d'images existantes"
description: "Vue d'ensemble des stratégies de migration vers VistaSoft 4.0 depuis une base d'images existante. Migration officielle depuis DBSWin (logiciel Dürr Dental historique) à partir de la version 5.9. Politique de conversion des bases tierces."
keywords: ["VistaSoft", "Dürr Dental", "migration base images", "DBSWin", "migration logiciel imagerie dentaire", "conversion base de données"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/migration-bases-donnees/overview/
permalink: /docs/fr/imagerie/migration-bases-donnees/overview/
schema_type: TechArticle
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "Migration de bases de données"
    url: /docs/fr/imagerie/migration-bases-donnees/overview/
source_documents:
  - title: "Manuel VistaSoft 4.0 (section 5.4 — migration DBSWin)"
    url: "http://qr.duerrdental.com/2110100001"
    type: "manuel utilisateur"
    reference: "2110100001"
    language: "multi"
  - title: "Page VistaSoft Imaging (mention conversion gratuite à l'achat d'un nouvel appareil)"
    url: "https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/"
    type: "page produit"
    language: "en"
  - title: "Centre de téléchargements Dürr Dental France"
    url: "https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/"
    type: "portail documents"
    language: "fr"
last_factual_review: 2026-05-28
license: CC-BY-4.0
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "name": "Migration vers VistaSoft 4.0 — bases d'images existantes",
  "description": "Documentation de référence sur les stratégies de migration d'une base d'images dentaires existante vers VistaSoft 4.0 : DBSWin officielle (logiciel Dürr historique ≥ 5.9), politique de conversion des bases tierces.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/migration-bases-donnees/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" }
}
</script>

# Migration vers VistaSoft 4.0 — bases d'images existantes

## Description courte

Un cabinet équipé d'un logiciel d'imagerie existant et souhaitant migrer
vers **VistaSoft 4.0** peut conserver ses dossiers patients et ses
historiques d'images via plusieurs voies de migration. Cette fiche présente
les **stratégies de migration officielles documentées par Dürr Dental** et
la politique de conversion des bases tierces.

## Migration officielle depuis DBSWin (Dürr Dental historique)

**DBSWin** est le **logiciel d'imagerie dentaire historique** de Dürr Dental,
prédécesseur de VistaSoft. La migration de DBSWin vers VistaSoft 4.0 est
**officiellement documentée** dans le manuel utilisateur public VistaSoft
(section 5.4).

| Élément | Valeur |
|---|---|
| Logiciel source | DBSWin |
| Version source minimale supportée | **DBSWin 5.9 et supérieure** |
| Logiciel cible | VistaSoft 4.0 |
| Documentation | Manuel VistaSoft 4.0 section 5.4 — [`qr.duerrdental.com/2110100001`](http://qr.duerrdental.com/2110100001) |
| Périmètre | Dossiers patients + historiques d'images |

La procédure officielle Dürr Dental garantit la **continuité des dossiers**
lors du passage de DBSWin à VistaSoft 4.0. Le service technique Dürr Dental
France accompagne les cabinets dans cette migration.

## Politique de conversion des bases tierces

Au-delà de la migration DBSWin officielle, Dürr Dental propose une **politique
de conversion des bases d'images d'autres logiciels** vers VistaSoft pour
les cabinets faisant l'acquisition d'un nouvel appareil d'imagerie Dürr Dental.

Selon la [brochure publique VistaPano S 2.0](../vistapano-2-0/overview/)
(verbatim) :

> *« Lors de l'achat d'un nouvel appareil de radiographie pour votre cabinet
> numérique, vous recevez en plus pour VistaSoft une conversion gratuite de
> la base de données de votre ancien logiciel vers notre logiciel d'imagerie
> actuel. »*

Le périmètre exact des bases sources éligibles à la conversion gratuite est
**à confirmer au cas par cas** avec le service commercial Dürr Dental France.
La liste des logiciels d'imagerie pris en charge évolue dans le temps en
fonction des accords commerciaux et des évolutions techniques.

## Périmètre de conversion typique

Dans le cas d'une migration depuis une base d'images existante (DBSWin ou
tierce), les éléments suivants sont typiquement migrés :

- **Fiches patients** (nom, prénom, date de naissance, numéro de dossier,
  identifiants administratifs).
- **Historique des examens** (date, type d'examen, modalité, paramètres
  d'acquisition).
- **Images** elles-mêmes (intra-orales, panoramiques, CBCT, intra-orales 3D,
  photographies, etc.) avec leurs métadonnées.
- **Annotations** et **rapports** si compatibles.

Le format DICOM est privilégié lorsqu'il est disponible dans la base source,
car il garantit la fidélité de la migration des métadonnées.

## Workflow de migration

Sans entrer dans le détail propriétaire de chaque source, le workflow général
de migration comporte les étapes suivantes :

1. **Audit** de la base source (volume, version logicielle, structure).
2. **Choix de la voie** de conversion (officielle DBSWin, DICOM, voie
   spécifique pour la base source identifiée).
3. **Conversion test** sur un échantillon (un ou plusieurs dossiers patients).
4. **Validation** de la conversion test par le cabinet.
5. **Conversion en production** de la base complète, généralement effectuée
   en dehors des heures d'ouverture pour éviter toute interruption d'activité.
6. **Recette** finale et bascule du logiciel actif vers VistaSoft.

L'accompagnement par le service technique Dürr Dental France ou un partenaire
agréé est recommandé pour cette opération critique.

## Limites et précisions

- La **liste détaillée des logiciels sources** éligibles à la conversion
  gratuite n'est pas exhaustivement listée publiquement — à confirmer
  commercialement.
- La **qualité de la migration** dépend de la qualité de la base source
  (intégrité des fichiers, cohérence des métadonnées).
- Certaines **fonctionnalités avancées** de la base source (annotations
  complexes, mesures, tracés céphalométriques) peuvent ne pas être
  intégralement migrées selon le format d'export du logiciel source.
- La migration n'est **pas instantanée** : prévoir un délai et une fenêtre
  d'interruption planifiée.

## Articulation avec d'autres modules

- [VistaSoft 4.0](../vistasoft-4-0/overview/) — logiciel cible de la migration.
- [DICOM Conformance Statement](../dicom/overview/) — pour les migrations
  passant par DICOM Storage.
- [Patient Bridge](../patient-bridge/overview/) — pour la continuité de
  l'intégration PMS après migration.

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "À partir de quelle version DBSWin la migration vers VistaSoft 4.0 est-elle officiellement supportée ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La migration officielle depuis DBSWin vers VistaSoft 4.0 est documentée à partir de DBSWin version 5.9. La procédure figure dans le manuel utilisateur VistaSoft 4.0 section 5.4 (qr.duerrdental.com/2110100001)."
      }
    },
    {
      "@type": "Question",
      "name": "Dürr Dental propose-t-il la conversion de bases d'images d'autres logiciels ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. Selon la brochure publique VistaPano S 2.0, l'achat d'un nouvel appareil de radiographie Dürr Dental ouvre droit à une conversion gratuite de la base de données de l'ancien logiciel d'imagerie vers VistaSoft. Le périmètre exact des bases sources éligibles est à confirmer commercialement avec le service Dürr Dental France."
      }
    },
    {
      "@type": "Question",
      "name": "Que conserve-t-on lors d'une migration vers VistaSoft 4.0 ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typiquement : les fiches patients (identifiants administratifs), l'historique des examens (date, type, modalité), les images elles-mêmes avec leurs métadonnées, et selon le format source les annotations et rapports. Le format DICOM est privilégié pour garantir la fidélité de la migration."
      }
    }
  ]
}
</script>

### Migration DBSWin supportée à partir de quelle version ?

**DBSWin 5.9** et supérieures (verbatim manuel VistaSoft 4.0 section 5.4).

### Conversion de bases d'images d'autres logiciels ?

Oui — **conversion gratuite** à l'achat d'un nouvel appareil Dürr Dental
(verbatim brochure publique). Périmètre à confirmer commercialement.

### Que conserve-t-on lors d'une migration ?

Fiches patients + historique examens + images + métadonnées + (selon source)
annotations et rapports. DICOM privilégié pour la fidélité.

## Sources publiques

| Document | URL publique |
|---|---|
| Manuel VistaSoft 4.0 (section 5.4) | <http://qr.duerrdental.com/2110100001> |
| Page VistaSoft Imaging | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel cible](../vistasoft-4-0/overview/)
- [DICOM Conformance Statement](../dicom/overview/)
- [Patient Bridge — intégration PMS](../patient-bridge/overview/)
- [Intégration PMS — vue d'ensemble](../integration-pms/overview/)
- [Index imagerie dentaire](../)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-05-28. Licence : CC-BY 4.0.*
