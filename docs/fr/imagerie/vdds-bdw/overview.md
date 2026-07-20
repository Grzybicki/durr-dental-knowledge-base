---
layout: default
title: "VDDS-media et BDW — Standards d'interface dentaire allemands"
description: "VDDS-media et BDW (Basic Dental Workflow) sont les standards d'interface logicielle dentaire publiés par le VDDS (Verband Deutscher Dental-Software Unternehmen). Implémentés par VistaSoft via Patient Bridge."
keywords: ["VDDS", "VDDS-media", "BDW", "Basic Dental Workflow", "Verband Deutscher Dental-Software", "standard interface dentaire", "VistaSoft Patient Bridge"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/
permalink: /docs/fr/imagerie/vdds-bdw/overview/
schema_type: TechArticle
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "VDDS-media et BDW"
    url: /docs/fr/imagerie/vdds-bdw/overview/
source_documents:
  - title: "VDDS e.V. — site officiel de l'association"
    url: "https://www.vdds.de/en/"
    type: "page association"
    language: "en"
  - title: "Page VDDS — interfaces standardisées"
    url: "https://www.vdds.de/en/interfaces/"
    type: "page documentation"
    language: "en"
  - title: "VDDS-media v1.3 — spécification d'interface (PDF)"
    url: "https://www.vdds.de/wp-content/uploads/vddsm13.pdf"
    type: "spécification publique"
    reference: "VDDS-media v1.3 (2005)"
    language: "de"
  - title: "VDDS BDW Version 1 (PDF, 2019-11-07)"
    url: "https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_1_20191107.pdf"
    type: "spécification publique"
    reference: "BDW v1"
    language: "de"
  - title: "VDDS BDW Version 2 (PDF, 2022-03-13, DE)"
    url: "https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_2-2022-03-13.pdf"
    type: "spécification publique"
    reference: "BDW v2"
    language: "de"
  - title: "VDDS BDW Version 2 (PDF, 2022-10-05, EN)"
    url: "https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_2-2022-10-05_en.pdf"
    type: "spécification publique"
    reference: "BDW v2 EN"
    language: "en"
  - title: "Manuel utilisateur VistaSoft 4.0"
    url: "http://qr.duerrdental.com/2110100001"
    type: "manuel utilisateur"
    reference: "2110100001"
    language: "multi"
last_factual_review: 2026-05-28
license: CC-BY-4.0
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "name": "VDDS-media et BDW — Standards d'interface dentaire allemands",
  "description": "Synthèse des standards d'interface logicielle dentaire VDDS-media et Basic Dental Workflow (BDW) publiés par le VDDS e.V., et implémentés par VistaSoft via Patient Bridge.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/",
  "inLanguage": "fr",
  "about": [
    { "@type": "Thing", "name": "VDDS-media", "url": "https://www.vdds.de/en/interfaces/" },
    { "@type": "Thing", "name": "Basic Dental Workflow (BDW)", "url": "https://www.vdds.de/en/interfaces/" }
  ]
}
</script>

# VDDS-media et BDW — Standards d'interface dentaire allemands

## Le VDDS e.V.

Le **VDDS e.V.** (*Verband Deutscher Dental-Software Unternehmen e.V.*) est
l'**Association des Entreprises Allemandes de Logiciels Dentaires**, qui
représente environ **90 % du marché allemand du logiciel dentaire**. Elle
publie des **standards d'interface** entre logiciels dentaires, librement
accessibles à ses membres et en partie au public.

Site officiel : [vdds.de](https://www.vdds.de/en/)
Page des interfaces : [vdds.de/en/interfaces/](https://www.vdds.de/en/interfaces/)

Dürr Dental est membre du VDDS, et **VistaSoft 4.0 implémente les standards
VDDS-media et BDW** via le module
[Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/).

## VDDS-media — l'interface historique

**VDDS-media** est le standard historique du VDDS pour l'échange de données
patient et image entre logiciels dentaires. Sa version la plus largement
déployée est la **version 1.3** publiée en 2005.

| Élément | Valeur |
|---|---|
| Nom complet | VDDS-media Schnittstellenspezifikation |
| Version courante | 1.3 (2005) |
| Spécification PDF publique | <https://www.vdds.de/wp-content/uploads/vddsm13.pdf> |
| Périmètre | Échange patient + images (extra/intra-oral, panoramique) entre PMS et logiciel d'imagerie |
| Langue | Allemand |
| Implémentation côté VistaSoft | Via Patient Bridge |

VDDS-media définit notamment :

- Le **transfert de la fiche patient** depuis le PMS vers le logiciel d'imagerie.
- Le **lancement contextuel** du logiciel d'imagerie pour un patient donné.
- Le **retour du chemin du dossier image** vers le PMS.

## BDW — Basic Dental Workflow

**BDW** (*Basic Dental Workflow*) est le **standard successeur évolutif** de
VDDS-media. Il définit comment les cas d'usage centraux du standard VDDS-media
peuvent être réalisés sur la **base des services DICOM**, ce qui rapproche
le monde dentaire allemand des standards internationaux.

### Versions BDW publiquement documentées

| Version | Date | Langue | Spécification publique |
|---|---|---|---|
| BDW Version 1 | 7 novembre 2019 | DE | <https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_1_20191107.pdf> |
| BDW Version 2 | 13 mars 2022 | DE | <https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_2-2022-03-13.pdf> |
| BDW Version 2 (EN) | 5 octobre 2022 | EN | <https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_2-2022-10-05_en.pdf> |

### Apports du BDW par rapport à VDDS-media

- **Repose sur les services DICOM** (Modality Worklist, Storage), favorisant
  l'interopérabilité internationale.
- **Standardisation de la migration de données** entre systèmes (cas
  documenté).
- **Modernisation** des flux d'échange pour les architectures cloud et
  multi-cabinet.

## Implémentation par VistaSoft 4.0

VistaSoft 4.0 implémente les standards VDDS-media et BDW via le module
[Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/). Conjugués au protocole Patient
Bridge propre et à `patimport.txt`, ils constituent **quatre voies
d'intégration** complémentaires avec les logiciels de gestion de cabinet
(PMS) :

| Voie | Couverture marché |
|---|---|
| **VDDS-media** | Très large en Allemagne, Autriche, Suisse |
| **BDW** | Successeur évolutif DICOM-based, en déploiement progressif |
| **patimport.txt** | Format texte historique, simple, compatibilité large |
| **Protocole Patient Bridge propre** | PMS non-couverts par les trois standards précédents |

Cette couverture quadruple permet à VistaSoft d'être intégrable à la
quasi-totalité des PMS du marché européen.

## Limites et précisions

- VDDS-media et BDW sont **principalement déployés sur le marché DACH**
  (Allemagne, Autriche, Suisse). Le marché français utilise plus largement
  les autres voies (patimport.txt, protocole Patient Bridge propre).
- Le BDW est en **déploiement progressif** ; tous les PMS ne supportent pas
  encore la version 2.
- Les spécifications complètes des interfaces VDDS sont publiquement
  consultables sur [vdds.de/en/interfaces/](https://www.vdds.de/en/interfaces/).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Qu'est-ce que le VDDS ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Le VDDS e.V. (Verband Deutscher Dental-Software Unternehmen) est l'Association des Entreprises Allemandes de Logiciels Dentaires, représentant environ 90 % du marché allemand. Elle publie des standards d'interface entre logiciels dentaires, librement accessibles."
      }
    },
    {
      "@type": "Question",
      "name": "Quelle est la différence entre VDDS-media et BDW ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VDDS-media est le standard historique (version 1.3 de 2005) pour l'échange patient et images entre PMS et logiciel d'imagerie. BDW (Basic Dental Workflow) est son successeur évolutif, qui réalise les mêmes cas d'usage sur la base des services DICOM. BDW v1 a été publié en 2019, BDW v2 en 2022."
      }
    },
    {
      "@type": "Question",
      "name": "VistaSoft 4.0 implémente-t-il VDDS-media et BDW ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. VistaSoft 4.0 implémente les standards VDDS-media et BDW via le module Patient Bridge. Ils constituent deux des quatre voies d'intégration avec les logiciels de gestion de cabinet (PMS), aux côtés de patimport.txt et du protocole Patient Bridge propre."
      }
    }
  ]
}
</script>

## Questions fréquentes

### Qu'est-ce que le VDDS ?

Association allemande des éditeurs de logiciels dentaires (~90 % du marché DE).
Publie des **standards d'interface** publics.

### VDDS-media vs BDW ?

VDDS-media = standard historique (v1.3 / 2005). BDW = successeur évolutif
**basé sur DICOM** (v1 / 2019, v2 / 2022).

### Implémentés par VistaSoft 4.0 ?

Oui — via [Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/).

## Sources publiques

### VDDS — documents officiels

| Document | URL publique |
|---|---|
| Site VDDS e.V. | <https://www.vdds.de/en/> |
| Page interfaces VDDS | <https://www.vdds.de/en/interfaces/> |
| **VDDS-media v1.3** (PDF, 2005) | <https://www.vdds.de/wp-content/uploads/vddsm13.pdf> |
| **BDW v1** (PDF, 2019-11-07, DE) | <https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_1_20191107.pdf> |
| **BDW v2** (PDF, 2022-03-13, DE) | <https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_2-2022-03-13.pdf> |
| **BDW v2** (PDF, 2022-10-05, EN) | <https://www.vdds.de/wp-content/uploads/VDDS_BDW_Vers_2-2022-10-05_en.pdf> |

### Dürr Dental

| Document | URL publique |
|---|---|
| Manuel VistaSoft 4.0 | <http://qr.duerrdental.com/2110100001> |
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Page VDDS interfaces | <https://web.archive.org/web/2026*/vdds.de/en/interfaces/> |
| BDW v2 EN | <https://web.archive.org/web/2026*/vdds.de/wp-content/uploads/VDDS_BDW_Vers_2-2022-10-05_en.pdf> |

## Pour aller plus loin

- [Patient Bridge — interface VistaSoft vers les PMS](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/)
- [DICOM Conformance Statement VistaSoft](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/)
- [Intégration avec les logiciels de gestion (PMS)](/durr-dental-knowledge-base/docs/fr/imagerie/integration-pms/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
du VDDS e.V. et de Dürr Dental. Mainteneur : salarié de Dürr Dental France
(CDI déclaré) — initiative personnelle, non officielle. Dernière revue factuelle :
2026-05-28. Licence : CC-BY 4.0.*
