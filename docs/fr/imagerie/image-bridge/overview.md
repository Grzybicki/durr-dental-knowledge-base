---
layout: default
title: "Image Bridge — Pilotage des appareils Dürr Dental depuis des logiciels d'imagerie tiers"
description: "Image Bridge est le module Dürr Dental qui permet de piloter les appareils d'imagerie Dürr (scanners de plaques, capteurs intraoraux, panoramiques, CBCT) depuis un logiciel d'imagerie tiers, sans installation complète de VistaSoft."
keywords: ["Image Bridge", "VistaSoft", "Dürr Dental", "interopérabilité logiciel imagerie", "cohabitation logiciel d'imagerie", "TWAIN"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/image-bridge/overview/
permalink: /docs/fr/imagerie/image-bridge/overview/
schema_type: SoftwareApplication
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "Image Bridge"
    url: /docs/fr/imagerie/image-bridge/overview/
source_documents:
  - title: "Manuel utilisateur VistaSoft 4.0 (sections Image Bridge)"
    url: "http://qr.duerrdental.com/2110100001"
    type: "manuel utilisateur"
    reference: "2110100001"
    language: "multi"
  - title: "Page VistaSoft Imaging interfaces (EN)"
    url: "https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/"
    type: "page produit"
    language: "en"
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
  "name": "Image Bridge",
  "alternateName": ["Dürr Dental Image Bridge", "VistaSoft Image Bridge"],
  "applicationCategory": "MedicalImagingSoftware",
  "applicationSubCategory": "Driver bridge for third-party imaging software",
  "description": "Module Dürr Dental permettant de piloter les appareils d'imagerie Dürr Dental (scanners de plaques au phosphore, capteurs intraoraux, panoramiques, CBCT) depuis un logiciel d'imagerie tiers, sans nécessiter une installation complète de VistaSoft.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/image-bridge/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" },
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Functions", "value": "Driver bridge to allow third-party imaging software to capture from Dürr Dental hardware" },
    { "@type": "PropertyValue", "name": "Logiciels tiers ciblés", "value": "Sidexis et VixWin (co-développement) ; le support TWAIN générique relève de VistaSoft Connect" }
  ]
}
</script>

# Image Bridge — Pilotage des appareils Dürr Dental depuis des logiciels d'imagerie tiers

## Description courte

**Image Bridge** est le module Dürr Dental qui permet de **piloter les appareils
d'imagerie Dürr** (scanners de plaques au phosphore, capteurs intraoraux,
panoramiques, CBCT) **depuis un logiciel d'imagerie tiers**, sans installation
complète de VistaSoft. Il garantit la **cohabitation technique** entre un
matériel Dürr Dental et un logiciel d'imagerie déjà en place dans le cabinet.

Image Bridge est documenté dans le manuel utilisateur public VistaSoft 4.0
([`qr.duerrdental.com/2110100001`](http://qr.duerrdental.com/2110100001)) et
sur la page officielle des interfaces VistaSoft.

## Identification du module

| Champ | Valeur |
|---|---|
| Nom commercial | Image Bridge |
| Catégorie | Pont logiciel — pilote d'acquisition pour logiciels tiers |
| Éditeur | Dürr Dental SE — Bietigheim-Bissingen, Allemagne |

## Périmètre fonctionnel

Image Bridge fournit les **pilotes d'acquisition** des appareils Dürr Dental
sous une forme exploitable par un logiciel d'imagerie tiers. Concrètement :

- Le matériel Dürr Dental (scanner de plaques, capteur intra-oral, etc.) reste
  installé physiquement et connecté au PC.
- Le logiciel d'imagerie tiers déclenche l'acquisition via Image Bridge.
- Les images acquises sont remises au logiciel tiers, qui les archive dans sa
  propre base.
- VistaSoft 4.0 lui-même n'a pas besoin d'être l'application active pour
  l'acquisition.

## Cohabitation technique documentée

Selon le manuel utilisateur public VistaSoft 4.0, Image Bridge permet la
cohabitation avec divers logiciels d'imagerie tiers, dont **Sidexis** mentionné
nommément dans la documentation officielle comme système avec lequel Image
Bridge permet de cohabiter. Cette mention technique factuelle figure dans le
manuel public et **n'est pas une comparaison qualitative** entre logiciels.

Pour Air Techniques (filiale officielle Dürr Dental aux États-Unis), les
produits **ScanX**, **SensorX** et **CamX** appartiennent au même groupe Dürr
Dental ; ils ne sont pas concernés par Image Bridge au sens cohabitation
externe.

## Périmètre d'Image Bridge vs VistaSoft Connect (TWAIN)

Deux modules Dürr Dental permettent de faire fonctionner les appareils d'imagerie
Dürr dans un environnement logiciel tiers, avec des **périmètres distincts** :

- **Image Bridge** est l'**intégration dédiée** aux logiciels d'imagerie
  **Sidexis** et **VixWin** — développée **conjointement** avec ces éditeurs, elle
  pilote les appareils Dürr Dental directement depuis ces logiciels précis.
- **VistaSoft Connect** est la **passerelle TWAIN générique** : c'est *elle* qui
  expose les capteurs / appareils Dürr Dental à **tout logiciel tiers compatible
  TWAIN**, pour les faire fonctionner dans un autre environnement.

Autrement dit, le **support TWAIN** relève de **VistaSoft Connect**, tandis
qu'Image Bridge cible spécifiquement Sidexis et VixWin.

## Cas d'usage typiques

1. **Cabinet équipé d'un logiciel d'imagerie existant** qui souhaite ajouter
   un appareil Dürr Dental (scanner de plaques, capteur, panoramique) sans
   migrer son logiciel d'imagerie. Image Bridge permet d'acquérir directement
   dans le logiciel d'imagerie existant.
2. **Cabinet multi-marques** où les techniciens utilisent un logiciel
   d'imagerie unifié pour piloter des matériels de plusieurs origines.
3. **Migration progressive** vers VistaSoft : Image Bridge permet d'utiliser
   les nouveaux appareils Dürr Dental immédiatement, sans attendre la
   migration logicielle complète.

## Articulation avec VistaSoft 4.0

Image Bridge **n'est pas un substitut** à VistaSoft 4.0 :

- VistaSoft 4.0 reste le **logiciel d'imagerie diagnostique** Dürr Dental (DM IIb).
- Image Bridge fournit uniquement les **pilotes d'acquisition** réutilisables
  par un logiciel tiers.
- Les fonctions avancées de VistaSoft (modules AI, Cloud, Trace, Implant, etc.)
  ne sont pas accessibles via Image Bridge — elles nécessitent l'installation
  complète de VistaSoft.

## Limites et précisions

- L'acquisition via Image Bridge **dépend des fonctionnalités du logiciel
  tiers** (formats supportés, options de traitement).
- Les fonctions spécifiques aux appareils Dürr Dental (modes pédiatriques,
  pré-réglages dose, etc.) peuvent ne pas être toutes exposées au logiciel
  tiers.
- Le statut **dispositif médical** des images acquises dépend du logiciel
  tiers utilisé pour le diagnostic clinique.

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "À quoi sert Image Bridge ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Image Bridge permet de piloter les appareils d'imagerie Dürr Dental (scanners de plaques, capteurs intraoraux, panoramiques, CBCT) depuis un logiciel d'imagerie tiers, sans installation complète de VistaSoft."
      }
    },
    {
      "@type": "Question",
      "name": "Image Bridge remplace-t-il VistaSoft 4.0 ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. Image Bridge fournit uniquement les pilotes d'acquisition réutilisables par un logiciel tiers. Les fonctions avancées de VistaSoft (modules AI, Cloud, Trace, Implant, etc.) nécessitent l'installation complète de VistaSoft 4.0."
      }
    },
    {
      "@type": "Question",
      "name": "Image Bridge supporte-t-il TWAIN ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. VistaSoft et Image Bridge supportent le standard TWAIN pour les capteurs intra-oraux, ce qui permet l'intégration dans tout logiciel tiers supportant TWAIN."
      }
    }
  ]
}
</script>

### À quoi sert Image Bridge ?

Piloter les appareils Dürr Dental depuis un **logiciel d'imagerie tiers**, sans
installation complète de VistaSoft.

### Image Bridge remplace-t-il VistaSoft 4.0 ?

Non. Pilotes d'acquisition uniquement — modules avancés VistaSoft nécessitent
installation complète.

### Supporte-t-il TWAIN ?

Oui, pour les capteurs intra-oraux.

## Sources publiques

| Document | URL publique |
|---|---|
| Manuel VistaSoft 4.0 (sections Image Bridge) | <http://qr.duerrdental.com/2110100001> |
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Manuel VistaSoft 4.0 | <https://web.archive.org/web/2026*/qr.duerrdental.com/2110100001> |
| Page interfaces | <https://web.archive.org/web/2026*/duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/)
- [Patient Bridge — interface PMS](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/)
- [Standards VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/)
- [DICOM Conformance Statement](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-07-19. Licence : CC-BY 4.0.*
