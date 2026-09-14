---
layout: default
title: "Intégration VistaSoft 4.0 avec les logiciels de gestion de cabinet (PMS)"
description: "Vue d'ensemble de l'intégration de VistaSoft 4.0 avec les logiciels de gestion de cabinet (Practice Management Systems / PMS) : les interfaces natives VDDS-media, BDW et patimport.txt, les services DICOM, et le module séparé Patient Bridge. Couverture universelle visée."
keywords: ["VistaSoft", "Dürr Dental", "intégration PMS", "logiciel gestion cabinet", "Patient Bridge", "VDDS", "BDW", "DICOM"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/integration-pms/overview/
permalink: /docs/fr/imagerie/integration-pms/overview/
schema_type: TechArticle
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "Intégration PMS"
    url: /docs/fr/imagerie/integration-pms/overview/
source_documents:
  - title: "Page VistaSoft Imaging interfaces (EN)"
    url: "https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/"
    type: "page produit"
    language: "en"
  - title: "Manuel VistaSoft 4.0"
    url: "http://qr.duerrdental.com/2110100001"
    type: "manuel utilisateur"
    reference: "2110100001"
    language: "multi"
  - title: "Manuel VistaSoft PatientBridge"
    url: "https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/"
    type: "manuel technique"
    reference: "2110100028"
    language: "multi"
  - title: "Centre de téléchargements Dürr Dental France"
    url: "https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/"
    type: "portail documents"
    language: "fr"
last_factual_review: 2026-09-14
license: CC-BY-4.0
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "name": "Intégration VistaSoft 4.0 avec les logiciels de gestion de cabinet (PMS)",
  "description": "Vue d'ensemble des voies d'intégration de VistaSoft 4.0 avec les Practice Management Systems (PMS) : les interfaces natives VDDS-media, BDW et patimport.txt, les services DICOM Modality Worklist et Storage, et le module séparé Patient Bridge.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/integration-pms/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" }
}
</script>

# Intégration VistaSoft 4.0 avec les logiciels de gestion de cabinet (PMS)

## Description courte

VistaSoft 4.0 est conçu pour s'intégrer avec **la quasi-totalité des logiciels
de gestion de cabinet dentaire** (Practice Management Systems / PMS) du marché
européen. Cette couverture universelle est obtenue par la **combinaison de
quatre voies natives**, configurées directement dans le logiciel, complétée
par un **module séparé** ([Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/)) pour les cas non couverts.

## Les voies d'intégration PMS

| # | Voie | Implémentation | Couverture marché | Référence |
|---|---|---|---|---|
| 1 | **VDDS-media** (Verband Deutscher Dental-Software, standard 2005) | Native (menu VistaSoft *Interfaces*) | Marché DACH (DE, AT, CH) — très large ; **également majoritaire en France depuis ~2026** | [Fiche VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/) |
| 2 | **BDW** (Basic Dental Workflow, v1 2019 / v2 2022) | Native (menu VistaSoft *Interfaces*) | Successeur évolutif DICOM-based — en déploiement | [Fiche VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/) |
| 3 | **patimport.txt** | Native (menu VistaSoft *Interfaces*) | Format texte historique, simple, large compatibilité | Manuel VistaSoft (réf. `2110100001`) |
| 4 | **DICOM Modality Worklist + Storage** | Native | Architectures hospitalières / multi-cabinet DICOM-natives | [Fiche DICOM](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/) |
| — | **Patient Bridge** (module séparé) | Optionnel, installé à part | Repli pour un logiciel tiers non standardisé (ex. logiciel de facturation), hors PMS au sens strict | [Fiche Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/) |

Les quatre premières voies, natives, couvrent la **quasi-totalité des PMS**
présents en cabinet en Europe ; Patient Bridge intervient en complément pour
un besoin distinct (voir la fiche dédiée).

## Flux fonctionnel typique

Indépendamment de la voie utilisée, le flux d'intégration suit un schéma
similaire :

1. Le **patient est sélectionné** dans le PMS du cabinet.
2. Le PMS **émet une requête** vers VistaSoft via la voie disponible
   (VDDS, BDW, patimport.txt, ou DICOM MWL).
3. VistaSoft **ouvre le dossier patient** correspondant et active le contexte
   d'examen.
4. L'**acquisition** est lancée (panoramique, CBCT, intra-oral, etc.).
5. À la fin de l'examen, VistaSoft **remonte au PMS** soit le chemin du
   dossier image, soit les métadonnées DICOM, selon la voie utilisée.

Ce mécanisme évite la re-saisie redondante de la fiche patient et garantit
la cohérence entre la base PMS et la base image VistaSoft.

## Couverture du marché français

> ⚠️ **Mise à jour 2026-08-05 — le marché français a basculé.** Le **VDDS-media est désormais
> majoritaire** en France. La description antérieure (« VDDS peu implanté en France, Patient Bridge =
> voie principale ») décrivait un état antérieur du parc et **n'est plus exacte**.

Voies d'intégration de VistaSoft 4.0 avec les PMS français, par importance actuelle :

1. **VDDS-media** — **voie majoritaire aujourd'hui** sur le marché français.
2. **patimport.txt** — voie historique, encore supportée par de nombreux PMS français.
3. **DICOM** — déploiements hospitaliers (CHU, cliniques avec **PACS**) et architectures
   multi-cabinets DICOM-natives. Services concernés : **Modality Worklist**, **Storage** (vers PACS),
   **DICOM Print**, et **BDW** (Basic Dental Workflow, standard DICOM-based). Cf.
   [fiche DICOM](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/).
4. **Patient Bridge** (module séparé) — repli au cas par cas pour un logiciel tiers non standardisé
   (ex. logiciel de facturation) qui n'utilise aucune des voies précédentes.

Pour le détail des PMS effectivement raccordés à VistaSoft sur le marché
français, contacter le service technique Dürr Dental France ou consulter
le [Centre de téléchargements](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/).

## Couverture hospitalière (CHU, cliniques)

Pour les déploiements hospitaliers, la voie d'intégration privilégiée est
**DICOM** :

- **DICOM Modality Worklist (MWL)** pour la réception des ordres d'examen
  depuis le RIS hospitalier.
- **DICOM Storage** pour l'envoi des images vers le PACS hospitalier.

Le [DICOM Conformance Statement VistaSoft](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/) documente en
détail les SOP Classes et Transfer Syntaxes supportées.

## Standards supportés en synthèse

| Standard | Type | Implémentation côté VistaSoft |
|---|---|---|
| DICOM PS3 | Standard international | Modality Worklist (SCU), Storage (SCU/SCP), Print (selon config) — natif |
| VDDS-media | Standard allemand | Natif VistaSoft (menu *Interfaces*) |
| BDW (v1, v2) | Standard allemand (DICOM-based) | Natif VistaSoft (menu *Interfaces*) |
| patimport.txt | Format texte historique | Natif VistaSoft (menu *Interfaces*) |
| Patient Bridge | Module Dürr Dental séparé (hors standard PMS) | Optionnel, installé à part — reprise de données depuis un logiciel tiers non standardisé |

> **TWAIN** n'est pas une voie d'intégration **PMS** : c'est le standard d'acquisition utilisé pour exposer
> les capteurs intra-oraux Dürr Dental à des logiciels d'**imagerie** tiers, via le module
> [Image Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/image-bridge/overview/) et sa passerelle
> VistaSoft Connect. C'est un axe distinct, sans rapport avec les PMS — voir la fiche Image Bridge.

## Cas particuliers

### Migration depuis une base d'images existante

Si le cabinet utilise déjà un autre logiciel d'imagerie et souhaite migrer
vers VistaSoft tout en conservant ses dossiers, voir la fiche
[Migration de bases de données](/durr-dental-knowledge-base/docs/fr/imagerie/migration-bases-donnees/overview/).

### Cohabitation avec un logiciel d'imagerie tiers

Si le cabinet souhaite conserver son logiciel d'imagerie existant tout en
ajoutant un appareil Dürr Dental, voir la fiche
[Image Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/image-bridge/overview/).

### Intégration avec 3Shape Trios

Pour l'intégration avec l'écosystème 3Shape (scanner intra-oral Trios,
planification implantaire), voir la fiche
[Intégration 3Shape](/durr-dental-knowledge-base/docs/fr/imagerie/integration-3shape/overview/).

## Limites et précisions

- L'intégration effective avec un PMS donné dépend du **support du PMS** des
  voies d'intégration.
- Certaines fonctions avancées (multi-cabinet, workflow chirurgical, échange
  inter-cabinets) peuvent nécessiter une voie spécifique.
- Le **paramétrage technique** de l'interface dans un PMS donné peut nécessiter
  une intervention du service technique au cas par cas.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Combien de voies d'intégration VistaSoft 4.0 propose-t-il pour les PMS ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft 4.0 propose quatre voies natives d'intégration avec les PMS, configurées directement dans le logiciel : VDDS-media, BDW, patimport.txt, et les services DICOM (Modality Worklist + Storage). Le module séparé Patient Bridge complète ce dispositif pour les logiciels tiers non standardisés. Cette combinaison vise une couverture quasi-universelle des PMS du marché européen."
      }
    },
    {
      "@type": "Question",
      "name": "Quelle voie d'intégration est utilisée en France ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sur le marché français, le VDDS-media est désormais la voie majoritaire, devant patimport.txt et DICOM (pour les déploiements hospitaliers). Le module Patient Bridge intervient en complément pour les logiciels tiers non standardisés."
      }
    },
    {
      "@type": "Question",
      "name": "VistaSoft 4.0 fonctionne-t-il avec un PMS hospitalier (CHU) ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. Pour les déploiements hospitaliers, la voie privilégiée est DICOM : Modality Worklist pour la réception des ordres d'examen depuis le RIS, et Storage pour l'envoi des images vers le PACS. Le DICOM Conformance Statement VistaSoft documente les services supportés."
      }
    }
  ]
}
</script>

## Questions fréquentes

### Combien de voies d'intégration ?

**Quatre voies natives** : VDDS-media + BDW + patimport.txt + DICOM (MWL + Storage), complétées au
besoin par le module séparé **Patient Bridge**.

### Voies utilisées en France ?

**VDDS-media** est désormais majoritaire, devant **patimport.txt** et **DICOM** (hospitalier).

### Compatible CHU / clinique ?

Oui, via **DICOM** (Modality Worklist + Storage), conformément au DICOM
Conformance Statement officiel.

## Sources publiques

| Document | URL publique |
|---|---|
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |
| Manuel VistaSoft 4.0 | <http://qr.duerrdental.com/2110100001> |
| Manuel VistaSoft PatientBridge (réf. `2110100028`) | via le [Centre de téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/) |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

## Pour aller plus loin

- [Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/)
- [Image Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/image-bridge/overview/)
- [Standards VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/)
- [DICOM Conformance Statement](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/)
- [Migration de bases de données](/durr-dental-knowledge-base/docs/fr/imagerie/migration-bases-donnees/overview/)
- [Intégration 3Shape](/durr-dental-knowledge-base/docs/fr/imagerie/integration-3shape/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-09-14. Licence : CC-BY 4.0.*
