---
layout: default
title: "Patient Bridge — Interface VistaSoft vers les logiciels de gestion de cabinet"
description: "Patient Bridge est l'interface Dürr Dental qui relie VistaSoft 4.0 aux logiciels de gestion de cabinet (PMS). Quatre voies d'intégration : VDDS-media, BDW, patimport.txt et Patient Bridge propre. Manuel public qr.duerrdental.com/2110100028."
keywords: ["Patient Bridge", "VistaSoft 4.0", "Dürr Dental", "interface PMS", "VDDS-media", "BDW", "patimport.txt", "logiciel de gestion de cabinet", "intégration cabinet dentaire"]
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
  - title: "Manuel Patient Bridge"
    url: "http://qr.duerrdental.com/2110100028"
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
last_factual_review: 2026-07-19
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
  "description": "Interface Dürr Dental reliant VistaSoft 4.0 aux logiciels de gestion de cabinet (PMS). Couvre quatre voies d'intégration standardisées : VDDS-media, BDW, patimport.txt et le protocole Patient Bridge propre.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" },
  "softwareRequirements": "VistaSoft 4.0+",
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Manual reference", "value": "qr.duerrdental.com/2110100028" },
    { "@type": "PropertyValue", "name": "Integration paths", "value": "VDDS-media, BDW, patimport.txt, Patient Bridge protocol" }
  ]
}
</script>

# Patient Bridge — Interface VistaSoft vers les logiciels de gestion de cabinet

## Description courte

**Patient Bridge** est l'interface logicielle Dürr Dental qui relie **VistaSoft 4.0**
aux **logiciels de gestion de cabinet** (Practice Management Systems / PMS).
Le module couvre **quatre voies d'intégration standardisées** afin de garantir
une couverture aussi large que possible des PMS du marché.

Manuel utilisateur public : [`qr.duerrdental.com/2110100028`](http://qr.duerrdental.com/2110100028).

## Identification du module

| Champ | Valeur |
|---|---|
| Nom commercial | Patient Bridge |
| Catégorie | Interface de communication PMS ↔ logiciel d'imagerie |
| Éditeur | Dürr Dental SE — Bietigheim-Bissingen, Allemagne |
| Prérequis logiciel | VistaSoft 4.0 ou supérieur |
| Manuel public | `qr.duerrdental.com/2110100028` |

## Les quatre voies d'intégration

Patient Bridge ne se limite pas à un protocole unique : il couvre quatre voies
d'échange complémentaires entre VistaSoft et un PMS, ce qui maximise la
couverture des PMS du marché européen.

### 1. VDDS-media

[Standard VDDS-media](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/) défini par le **Verband Deutscher
Dental-Software Unternehmen e.V.** (VDDS). Interface standardisée la plus
répandue en Allemagne et en Autriche. Dürr Dental est membre du VDDS et VistaSoft
implémente ce standard côté logiciel d'imagerie.

### 2. BDW (Basic Dental Workflow)

[Standard BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/) successeur évolutif de VDDS-media, qui
définit comment les cas d'usage centraux du standard VDDS-media peuvent être
réalisés sur la base des services DICOM. Le BDW est publiquement documenté
par le VDDS (versions 1 et 2).

### 3. patimport.txt

**Format de fichier texte** simple basé sur un fichier `patimport.txt`. Voie
historique, simple à mettre en œuvre pour les PMS qui ne supportent pas les
standards plus récents. Toujours supportée par VistaSoft.

### 4. Protocole Patient Bridge propre

Protocole d'intégration propriétaire de Dürr Dental, documenté dans le manuel
[`qr.duerrdental.com/2110100028`](http://qr.duerrdental.com/2110100028).
Permet l'intégration avec les PMS qui n'utilisent ni VDDS-media, ni BDW, ni
patimport.txt — ce qui couvre en pratique la majorité des PMS du marché
français et international.

## Couverture des logiciels de gestion (PMS)

VistaSoft via Patient Bridge est conçu pour s'intégrer avec **la quasi-totalité
des logiciels de gestion de cabinet** du marché européen. La combinaison des
quatre voies (VDDS-media + BDW + patimport.txt + Patient Bridge propre) permet
une couverture universelle :

- **Marché DACH** (Allemagne, Autriche, Suisse) : voies VDDS-media et BDW
  largement déployées.
- **Marché français** : voies patimport.txt et Patient Bridge propre — couverture
  large des PMS français existants.
- **Autres marchés européens** : à arbitrer par voie selon le PMS local.

Pour le détail des PMS effectivement raccordés à VistaSoft, consulter le
[Centre de téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/)
ou contacter le service technique Dürr Dental France.

## Flux fonctionnel typique

1. Le patient est sélectionné dans le PMS du cabinet.
2. Le PMS envoie via l'interface Patient Bridge la fiche patient et le contexte
   d'examen à VistaSoft.
3. VistaSoft pilote l'acquisition (panoramique, CBCT, intra-oral, etc.).
4. À la fin de l'examen, VistaSoft remonte vers le PMS le chemin du dossier
   image ou les métadonnées DICOM associées.

Ce workflow évite la saisie redondante de la fiche patient et garantit la
cohérence des dossiers.

## Standards DICOM connexes

Patient Bridge est complémentaire aux services DICOM standards de VistaSoft
(**Modality Worklist** et **Storage**), qui constituent une cinquième voie
d'intégration DICOM-native. Voir [DICOM Conformance Statement](/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/).

## Limites et précisions

- La voie effectivement utilisée dépend du PMS du cabinet.
- Certaines fonctions avancées (gestion multi-cabinet, workflow chirurgical
  complexe) peuvent nécessiter une voie spécifique.
- L'installation et la configuration de l'interface dans un PMS donné peuvent
  nécessiter un paramétrage technique au cas par cas.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Combien de voies d'intégration PMS Patient Bridge couvre-t-il ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Patient Bridge couvre quatre voies d'intégration standardisées : VDDS-media, BDW (Basic Dental Workflow), patimport.txt et le protocole Patient Bridge propre Dürr Dental. Cette combinaison vise une couverture universelle des logiciels de gestion de cabinet (PMS) du marché européen."
      }
    },
    {
      "@type": "Question",
      "name": "Patient Bridge est-il compatible DICOM ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Patient Bridge est complémentaire aux services DICOM standards de VistaSoft (Modality Worklist et Storage), qui constituent une cinquième voie d'intégration DICOM-native. Voir la fiche DICOM Conformance Statement pour le détail."
      }
    },
    {
      "@type": "Question",
      "name": "Où trouver le manuel public de Patient Bridge ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Le manuel utilisateur Patient Bridge est publié par Dürr Dental à l'URL qr.duerrdental.com/2110100028, qui redirige vers le Centre de téléchargements officiel."
      }
    }
  ]
}
</script>

## Questions fréquentes

### Combien de voies d'intégration ?

**4** : VDDS-media + BDW + patimport.txt + protocole Patient Bridge propre.

### Compatible DICOM ?

Oui, en complément (services DICOM Worklist + Storage natifs de VistaSoft).

### Où trouver le manuel public ?

[`qr.duerrdental.com/2110100028`](http://qr.duerrdental.com/2110100028).

## Sources publiques

| Document | URL publique |
|---|---|
| Manuel Patient Bridge | <http://qr.duerrdental.com/2110100028> |
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |
| Page VistaSoft (socle) | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Manuel `2110100028` | <https://web.archive.org/web/2026*/qr.duerrdental.com/2110100028> |
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
personnelle, non officielle. Dernière revue factuelle : 2026-07-19. Licence : CC-BY 4.0.*
