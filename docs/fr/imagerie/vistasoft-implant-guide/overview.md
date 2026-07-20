---
layout: default
title: "VistaSoft Implant & VistaSoft Guide — Planification implantaire et guides chirurgicaux"
description: "VistaSoft Implant est le module Dürr Dental de planification implantaire pré-chirurgicale (backward planning). VistaSoft Guide permet la planification des guides de forage. Export STL ouvert. Compatible exocad et SICAT."
keywords: ["VistaSoft Implant", "VistaSoft Guide", "Dürr Dental", "planification implantaire", "backward planning", "guide chirurgical implantologie", "STL", "exocad", "SICAT"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-implant-guide/overview/
permalink: /docs/fr/imagerie/vistasoft-implant-guide/overview/
schema_type: SoftwareApplication
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "VistaSoft Implant & Guide"
    url: /docs/fr/imagerie/vistasoft-implant-guide/overview/
source_documents:
  - title: "Page produit VistaSoft Implant — implant planning (EN)"
    url: "https://www.duerrdental.com/en/products/software/imaging/implant-technology/"
    type: "page produit"
    language: "en"
  - title: "Page VistaSoft (EN)"
    url: "https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/"
    type: "page produit"
    language: "en"
  - title: "Page partenaire exocad — for integration partners"
    url: "https://exocad.com/you-exocad/for-integration-partners"
    type: "page partenaire"
    language: "en"
  - title: "Site partenaire SICAT"
    url: "https://www.sicat.com/"
    type: "page partenaire"
    language: "multi"
  - title: "Centre de téléchargements Dürr Dental France"
    url: "https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/"
    type: "portail documents"
    language: "fr"
last_factual_review: 2026-07-19
license: CC-BY-4.0
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["SoftwareApplication", "Product"],
  "name": "VistaSoft Implant & VistaSoft Guide",
  "alternateName": ["Dürr Dental VistaSoft Implant", "Dürr Dental VistaSoft Guide"],
  "applicationCategory": "MedicalImagingSoftware",
  "applicationSubCategory": "Implant planning software",
  "description": "Modules Dürr Dental dédiés à la planification implantaire pré-chirurgicale (VistaSoft Implant) et à la planification des guides de forage chirurgicaux (VistaSoft Guide). Export STL ouvert, intégration exocad et SICAT.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-implant-guide/overview/",
  "inLanguage": "fr",
  "publisher": {
    "@type": "Organization",
    "name": "Dürr Dental SE",
    "url": "https://www.duerrdental.com"
  },
  "softwareRequirements": "VistaSoft (logiciel socle) + acquisition CBCT",
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Workflow", "value": "Backward planning (crown to implant)" },
    { "@type": "PropertyValue", "name": "Export format", "value": "Open source STL" },
    { "@type": "PropertyValue", "name": "Integration partners", "value": "exocad, SICAT" }
  ]
}
</script>

# VistaSoft Implant & VistaSoft Guide — Planification implantaire et guides chirurgicaux

## Description courte

Les modules **VistaSoft Implant** et **VistaSoft Guide** de Dürr Dental sont
dédiés à la **planification implantaire pré-chirurgicale** et à la
**planification des guides de forage chirurgicaux**.

VistaSoft Implant suit un workflow de **backward planning** (planification
remontante depuis la couronne vers l'implant), avec export des données de
planification au format **STL ouvert**. Le module est compatible avec
l'écosystème **exocad** et **SICAT**.

## VistaSoft Implant — planification implantaire

Selon la [page produit officielle](https://www.duerrdental.com/en/products/software/imaging/implant-technology/) :

- **Outil de pointe pour la planification implantaire pré-chirurgicale complète**.
- **Backward planning** : « from crown to actual implant » — planification
  remontante depuis la couronne prothétique vers l'implant.
- **Workflow guidé** : le logiciel mène l'utilisateur à travers les étapes de
  planification, simplifiant la prise en main.
- **Export ouvert** : données de planification sauvegardées au format **STL**
  open source, transmissibles à un laboratoire de prothèse.
- **Rapport généré automatiquement** accompagnant les données STL.

## VistaSoft Guide — planification des guides de forage

VistaSoft Guide est le module complémentaire à VistaSoft Implant et permet la
**planification de différents types de guides de forage chirurgicaux**.

Verbatim de la page produit officielle :
*« As is the standard for DÜRR DENTAL, all data is saved in the form of open
source STL files, making it compatible for downstream processing on any
platform. »*

Le format STL ouvert garantit la compatibilité avec n'importe quel logiciel
ou laboratoire de prothèse capable de traiter ce format.

## Intégration avec SICAT

Selon la page produit officielle, la coopération entre Dürr Dental et **SICAT**
permet l'intégration des données de planification implantaire dans le workflow
SICAT.

Verbatim : *« Through its cooperation with SICAT, DÜRR DENTAL has been able to
stay faithful to its philosophy of helping dental practices prepare themselves
for the future with improved workflows, and customers benefit because
CEREC-based implant planning data can now also be produced with DÜRR DENTAL
X-ray units. »*

Voir [sicat.com](https://www.sicat.com/) pour le détail des outils SICAT
compatibles.

## Intégration avec exocad

L'écosystème CAO laboratoire **exocad** référence Dürr Dental comme partenaire
d'intégration sur sa page [for integration partners](https://exocad.com/you-exocad/for-integration-partners).

Cette intégration permet la circulation fluide des données STL entre la
planification implantaire VistaSoft et la conception prothétique exocad.

## Prérequis

- Logiciel socle [VistaSoft 4.0](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/) installé.
- Acquisition CBCT (typiquement via un appareil comme la VistaVox S, ou par
  import DICOM de données 3D issues d'un autre acquéreur).

## Limites et précisions

- VistaSoft Implant et VistaSoft Guide sont des **outils de planification** ;
  la décision et la pose chirurgicale restent de la responsabilité du
  praticien.
- La précision de la planification dépend de la qualité de l'acquisition CBCT
  sous-jacente.
- Les guides chirurgicaux conçus doivent être fabriqués selon les protocoles
  du laboratoire de prothèse ; Dürr Dental ne fabrique pas les guides
  physiques.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Quelle est la différence entre VistaSoft Implant et VistaSoft Guide ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft Implant est dédié à la planification implantaire pré-chirurgicale (backward planning de la couronne vers l'implant). VistaSoft Guide est dédié à la planification des guides de forage chirurgicaux. Les deux modules sont complémentaires et partagent le format STL ouvert."
      }
    },
    {
      "@type": "Question",
      "name": "Quel format d'export utilise VistaSoft Implant ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft Implant exporte les données de planification au format STL open source. Ce format est compatible avec n'importe quelle plateforme de CAO/CAM aval."
      }
    },
    {
      "@type": "Question",
      "name": "Avec quels logiciels partenaires VistaSoft Implant et Guide s'intègrent-ils ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft Implant et Guide s'intègrent avec exocad (CAO laboratoire) et SICAT. L'intégration SICAT permet notamment de produire des données de planification implantaire compatibles CEREC à partir d'appareils Dürr Dental."
      }
    }
  ]
}
</script>

## Questions fréquentes

### Quelle est la différence entre VistaSoft Implant et VistaSoft Guide ?

VistaSoft Implant = **planification implantaire** (backward planning couronne →
implant). VistaSoft Guide = **planification des guides de forage chirurgicaux**.
Complémentaires.

### Quel format d'export utilise VistaSoft Implant ?

**STL open source** — compatible avec toute plateforme CAO/CAM aval.

### Avec quels partenaires VistaSoft Implant et Guide s'intègrent-ils ?

**exocad** (CAO laboratoire) et **SICAT** (intégration permettant la
planification implantaire compatible CEREC à partir d'appareils Dürr Dental).

## Sources publiques

### Pages officielles Dürr Dental

| Document | URL publique |
|---|---|
| Page produit VistaSoft Implant — Implant technology | <https://www.duerrdental.com/en/products/software/imaging/implant-technology/> |
| Page VistaSoft (socle) | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

### Pages partenaires technologiques officielles

| Partenaire | URL publique |
|---|---|
| exocad — page integration partners | <https://exocad.com/you-exocad/for-integration-partners> |
| SICAT (intégration CEREC) | <https://www.sicat.com/> |

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Page VistaSoft Implant | <https://web.archive.org/web/2026*/duerrdental.com/en/products/software/imaging/implant-technology/> |
| Page exocad integration partners | <https://web.archive.org/web/2026*/exocad.com/you-exocad/for-integration-partners> |
| Page SICAT | <https://web.archive.org/web/2026*/sicat.com/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique (socle)](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/)
- [VistaSoft Trace — analyse céphalométrique](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-trace/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-07-19. Licence : CC-BY 4.0.*
