---
layout: default
title: "Patient Bridge — Interface VistaSoft vers les logiciels de gestion de cabinet"
description: "Patient Bridge est un module optionnel de VistaSoft 4.0 qui reprend les données patient d'un logiciel tiers (WinForms/WPF, ex. logiciel de facturation) par mapping de champs à l'écran. Distinct des interfaces natives VDDS-media, BDW et patimport.txt. Manuel public 2110100028."
keywords: ["Patient Bridge", "VistaSoft 4.0", "Dürr Dental", "reprise de données patient", "logiciel de facturation", "WinForms", "WPF", "logiciel de gestion de cabinet", "intégration cabinet dentaire"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/
permalink: /docs/fr/imagerie/patient-bridge/overview/
schema_type: SoftwareApplication
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "Patient Bridge"
    url: /docs/fr/imagerie/patient-bridge/overview/
source_documents:
  - title: "Manuel VistaSoft PatientBridge"
    url: "https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/"
    type: "manuel technique"
    reference: "2110100028"
    language: "multi"
  - title: "Page VistaSoft Imaging interfaces (EN)"
    url: "https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/"
    type: "page produit"
    language: "en"
  - title: "Page VistaSoft (socle EN)"
    url: "https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/"
    type: "page produit"
    language: "en"
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
  "@type": ["SoftwareApplication", "Product"],
  "name": "Patient Bridge",
  "alternateName": ["Dürr Dental Patient Bridge", "VistaSoft Patient Bridge"],
  "applicationCategory": "MedicalImagingSoftware",
  "applicationSubCategory": "PMS integration interface for dental imaging software",
  "description": "Module optionnel de VistaSoft 4.0 qui reprend les données patient d'un logiciel tiers (WinForms/WPF, par ex. un logiciel de facturation) en mappant les champs affichés à l'écran. Installé séparément, comme Image Bridge ; distinct des interfaces natives VDDS-media, BDW et patimport.txt.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" },
  "softwareRequirements": "VistaSoft 4.0+, logiciel tiers basé sur WinForms ou WPF",
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Manual reference", "value": "2110100028" },
    { "@type": "PropertyValue", "name": "Mechanism", "value": "Mapping de champs UI (screen scraping) sur logiciel tiers WinForms/WPF" }
  ]
}
</script>

# Patient Bridge — module de reprise de données patient depuis un logiciel tiers

## Description courte

**Patient Bridge** est un **module optionnel de VistaSoft 4.0**, installé et
distribué séparément (comme [Image Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/image-bridge/overview/)), qui permet de **reprendre les
données patient affichées dans un logiciel tiers** (typiquement un logiciel
de facturation/comptabilité de cabinet) **vers VistaSoft**, sans ressaisie.

Contrairement à ce qu'un nom proche pourrait laisser penser, Patient Bridge
n'est **pas** le module qui porte les standards
[VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/) ni le format `patimport.txt` :
ces trois voies sont **nativement intégrées à VistaSoft** (configurées
directement dans le menu *Interfaces* du logiciel). Patient Bridge est un
mécanisme technique différent, décrit ci-dessous.

Manuel utilisateur public (réf. `2110100028`), à retrouver via le
[Centre de téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/).

## Identification du module

| Champ | Valeur |
|---|---|
| Nom commercial | VistaSoft PatientBridge |
| Catégorie | Module optionnel de reprise de données patient (installation séparée) |
| Éditeur | Dürr Dental SE — Bietigheim-Bissingen, Allemagne |
| Prérequis logiciel | VistaSoft installé + logiciel tiers basé sur le framework **WinForms** ou **WPF** |
| Installation | Package `VistaSoft_*.iso\Tools\PatientBridge\VistaSoft PatientBridge.msi` |
| Manuel public | Réf. `2110100028`, supplément au manuel VistaSoft (réf. `2110100001`) |

## Fonctionnement — mapping de champs à l'écran

Patient Bridge ne dialogue avec aucun standard d'échange de données (pas de
fichier, pas de protocole réseau) : il **capture les champs affichés à
l'écran** du logiciel tiers (nom, prénom, date de naissance, identifiant
patient…) pour les reporter dans la fiche patient VistaSoft.

- Il est conçu pour les logiciels tiers **dont VistaSoft n'a pas d'interface
  standardisée** (ni VDDS-media, ni BDW, ni patimport.txt) — typiquement un
  logiciel de facturation/comptabilité de cabinet.
- Il ne fonctionne qu'avec des logiciels tiers construits sur les frameworks
  Windows **WinForms** ou **WPF** ; les autres ne sont pas pris en charge
  (message *« Window is not supported! »* à la création du profil).
- Un **profil** doit être créé par logiciel tiers : chaque champ de la fiche
  patient est associé, une fois, au champ correspondant à l'écran du
  logiciel tiers (clic sur le champ cible).
- Une fois le profil créé, la reprise se fait par un clic (ou un raccourci
  `PatientBridge.exe /start`) : les données du patient ouvert dans le
  logiciel tiers sont transférées et le patient est connecté automatiquement
  dans VistaSoft.

## Positionnement par rapport aux interfaces natives

VistaSoft 4.0 couvre la grande majorité des logiciels de gestion de cabinet
(PMS) via **trois voies natives**, configurées directement dans VistaSoft
sans aucun module supplémentaire : [VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/), et
`patimport.txt`. Voir la fiche
[Intégration PMS](/durr-dental-knowledge-base/docs/fr/imagerie/integration-pms/overview/) pour la vue d'ensemble.

Patient Bridge intervient **en dehors de ce périmètre** : il ne s'adresse pas
aux PMS eux-mêmes mais à des **logiciels tiers non standardisés** (le plus
souvent un logiciel de facturation/comptabilité) dont VistaSoft ne peut pas
reprendre les données autrement. C'est un module de secours, au cas par cas,
pas une interface PMS au sens des standards VDDS/BDW/patimport.txt.

Pour le détail des logiciels tiers effectivement pris en charge, consulter le
[Centre de téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/)
ou contacter le service technique Dürr Dental France.

## Flux fonctionnel typique

1. Un **profil** est créé une fois pour le logiciel tiers concerné : chaque
   champ de la fiche patient VistaSoft est associé au champ correspondant à
   l'écran du logiciel tiers.
2. Le patient est ouvert dans le logiciel tiers.
3. L'utilisateur déclenche Patient Bridge (clic ou raccourci `/start`) : les
   champs mappés sont lus à l'écran et transférés à VistaSoft.
4. VistaSoft ouvre automatiquement la fiche patient correspondante et le
   contexte d'examen est prêt pour l'acquisition.

## Limites et précisions

- Ne fonctionne qu'avec des logiciels tiers basés sur les frameworks Windows
  **WinForms** ou **WPF** ; un logiciel non reconnu affiche *« Window is not
  supported! »* à la création du profil.
- Le mapping des champs est **manuel, par profil**, et doit être revu si la
  disposition de l'écran du logiciel tiers change (mise à jour, changement
  de version).
- N'est **pas** un mécanisme d'échange DICOM : les services DICOM natifs de
  VistaSoft (**Modality Worklist**, **Storage**) sont indépendants, voir le
  [DICOM Conformance Statement](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/).
- L'installation et le paramétrage des profils peuvent nécessiter une
  intervention du service technique au cas par cas.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Patient Bridge implémente-t-il les standards VDDS-media et BDW ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. VDDS-media et BDW sont des interfaces natives de VistaSoft 4.0, configurées directement dans le menu Interfaces du logiciel, tout comme patimport.txt. Patient Bridge est un module séparé qui reprend les données patient d'un logiciel tiers non standardisé (typiquement un logiciel de facturation) par mapping de champs à l'écran."
      }
    },
    {
      "@type": "Question",
      "name": "Patient Bridge est-il compatible DICOM ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Patient Bridge n'a pas de lien direct avec DICOM : c'est un mécanisme de reprise de champs à l'écran, indépendant des services DICOM natifs de VistaSoft (Modality Worklist et Storage). Voir la fiche DICOM Conformance Statement pour le détail de ces services."
      }
    },
    {
      "@type": "Question",
      "name": "Avec quels logiciels tiers Patient Bridge fonctionne-t-il ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Uniquement avec des logiciels tiers construits sur les frameworks Windows WinForms ou WPF. Un logiciel non reconnu affiche le message d'erreur « Window is not supported! » lors de la création du profil."
      }
    }
  ]
}
</script>

## Questions fréquentes

### Patient Bridge implémente-t-il VDDS-media et BDW ?

Non. Ce sont des interfaces **natives** de VistaSoft (menu *Interfaces*), au même titre que `patimport.txt`. Patient Bridge est un module séparé.

### Compatible DICOM ?

Pas de lien direct — Patient Bridge est un mécanisme de reprise de champs à l'écran, indépendant des services DICOM natifs de VistaSoft.

### Avec quels logiciels tiers fonctionne-t-il ?

Uniquement les logiciels basés sur les frameworks Windows **WinForms** ou **WPF**.

## Sources publiques

| Document | URL publique |
|---|---|
| Manuel VistaSoft PatientBridge (réf. `2110100028`) | via le [Centre de téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/) |
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |
| Page VistaSoft (socle) | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

> Le raccourci `qr.duerrdental.com/2110100028` (utilisé dans une version antérieure de cette fiche) est **hors service** (vérifié 2026-09-14, redirige vers une page générique du prestataire de QR codes). Le document reste identifiable par sa référence Dürr `2110100028` via le Centre de téléchargements.

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Page interfaces | <https://web.archive.org/web/2026*/duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique (socle)](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/)
- [Image Bridge — cohabitation avec d'autres logiciels d'imagerie](/durr-dental-knowledge-base/docs/fr/imagerie/image-bridge/overview/)
- [Standards VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/)
- [DICOM Conformance Statement](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/)
- [Intégration avec les logiciels de gestion (PMS)](/durr-dental-knowledge-base/docs/fr/imagerie/integration-pms/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-09-14. Licence : CC-BY 4.0.*
