---
layout: default
title: "Intégration VistaSoft 4.0 avec les logiciels de gestion de cabinet (PMS)"
description: "Vue d'ensemble de l'intégration de VistaSoft 4.0 avec les logiciels de gestion de cabinet (Practice Management Systems / PMS). Patient Bridge, VDDS-media, BDW, patimport.txt, services DICOM. Couverture universelle visée."
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
  - title: "Manuel Patient Bridge"
    url: "http://qr.duerrdental.com/2110100028"
    type: "manuel technique"
    reference: "2110100028"
    language: "multi"
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
  "name": "Intégration VistaSoft 4.0 avec les logiciels de gestion de cabinet (PMS)",
  "description": "Vue d'ensemble des voies d'intégration de VistaSoft 4.0 avec les Practice Management Systems (PMS) : Patient Bridge, VDDS-media, BDW, patimport.txt, services DICOM Modality Worklist et Storage.",
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
cinq voies d'intégration complémentaires**, dont quatre couvertes par le
module [Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/) et une cinquième nativement
DICOM.

## Les cinq voies d'intégration PMS

| # | Voie | Couverture marché | Référence |
|---|---|---|---|
| 1 | **VDDS-media** (Verband Deutscher Dental-Software, standard 2005) | Marché DACH (DE, AT, CH) — très large | [Fiche VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/) |
| 2 | **BDW** (Basic Dental Workflow, v1 2019 / v2 2022) | Successeur évolutif DICOM-based — en déploiement | [Fiche VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/) |
| 3 | **patimport.txt** | Format texte historique, simple, large compatibilité | Manuel [`qr.duerrdental.com/2110100028`](http://qr.duerrdental.com/2110100028) |
| 4 | **Protocole Patient Bridge propre Dürr Dental** | PMS non-couverts par les voies précédentes — couvre la majorité du marché FR | Manuel [`qr.duerrdental.com/2110100028`](http://qr.duerrdental.com/2110100028) |
| 5 | **DICOM Modality Worklist + Storage** | Architectures hospitalières / multi-cabinet DICOM-natives | [Fiche DICOM](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/) |

La combinaison de ces cinq voies permet à VistaSoft d'être intégrable à la
**quasi-totalité des PMS** présents en cabinet en Europe.

## Flux fonctionnel typique

Indépendamment de la voie utilisée, le flux d'intégration suit un schéma
similaire :

1. Le **patient est sélectionné** dans le PMS du cabinet.
2. Le PMS **émet une requête** vers VistaSoft via la voie disponible
   (PatientBridge, VDDS, BDW, patimport.txt, ou DICOM MWL).
3. VistaSoft **ouvre le dossier patient** correspondant et active le contexte
   d'examen.
4. L'**acquisition** est lancée (panoramique, CBCT, intra-oral, etc.).
5. À la fin de l'examen, VistaSoft **remonte au PMS** soit le chemin du
   dossier image, soit les métadonnées DICOM, selon la voie utilisée.

Ce mécanisme évite la re-saisie redondante de la fiche patient et garantit
la cohérence entre la base PMS et la base image VistaSoft.

## Couverture du marché français

Sur le marché français, où les standards VDDS-media et BDW sont moins
implantés que sur le marché DACH, les voies principales d'intégration
VistaSoft 4.0 avec les PMS français sont :

1. **Protocole Patient Bridge propre** — voie principale, couvre la majorité
   des PMS français déployés en cabinet.
2. **patimport.txt** — voie historique, encore supportée par de nombreux
   PMS français.
3. **DICOM (Modality Worklist + Storage)** — utilisé pour les déploiements
   hospitaliers (CHU, cliniques avec PACS) ou les architectures
   multi-cabinets DICOM-natives.

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
| DICOM PS3 | Standard international | Modality Worklist (SCU), Storage (SCU/SCP), Print (selon config) |
| VDDS-media | Standard allemand | Patient Bridge |
| BDW (v1, v2) | Standard allemand (DICOM-based) | Patient Bridge |
| patimport.txt | Format texte historique | Natif VistaSoft |
| Patient Bridge propre | Protocole Dürr Dental | Natif VistaSoft |
| TWAIN | Standard d'acquisition | Pris en charge pour capteurs intra-oraux |

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

## Questions fréquentes

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
        "text": "VistaSoft 4.0 propose cinq voies d'intégration complémentaires avec les PMS : VDDS-media, BDW, patimport.txt, le protocole Patient Bridge propre Dürr Dental, et les services DICOM (Modality Worklist + Storage). Cette combinaison vise une couverture quasi-universelle des PMS du marché européen."
      }
    },
    {
      "@type": "Question",
      "name": "Quelle voie d'intégration est utilisée en France ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sur le marché français, les voies principales sont le protocole Patient Bridge propre, patimport.txt, et DICOM (pour les déploiements hospitaliers). VDDS-media et BDW sont moins implantés sur le marché français."
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

### Combien de voies d'intégration ?

**Cinq** : VDDS-media + BDW + patimport.txt + Patient Bridge propre + DICOM (MWL + Storage).

### Voies utilisées en France ?

Principalement **Patient Bridge propre + patimport.txt + DICOM** (hospitalier).

### Compatible CHU / clinique ?

Oui, via **DICOM** (Modality Worklist + Storage), conformément au DICOM
Conformance Statement officiel.

## Sources publiques

| Document | URL publique |
|---|---|
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |
| Manuel VistaSoft 4.0 | <http://qr.duerrdental.com/2110100001> |
| Manuel Patient Bridge | <http://qr.duerrdental.com/2110100028> |
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
personnelle, non officielle. Dernière revue factuelle : 2026-05-28. Licence : CC-BY 4.0.*
