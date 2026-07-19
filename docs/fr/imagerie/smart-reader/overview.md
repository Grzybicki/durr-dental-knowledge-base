---
layout: default
title: "VistaScan Smart Reader — Lecteur RFID USB pour attribution patient/plaque"
description: "VistaScan Smart Reader est le lecteur RFID USB Dürr Dental qui associe une plaque VistaScan IQ à un patient dans VistaSoft avant l'acquisition. Workflow automatisé, scan multi-patients dans n'importe quel ordre, attribution automatique."
keywords: ["VistaScan Smart Reader", "Dürr Dental", "lecteur RFID USB", "attribution plaque patient", "workflow VistaSoft IQ", "VistaScan IQ", "automation imagerie dentaire"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/smart-reader/overview/
permalink: /docs/fr/imagerie/smart-reader/overview/
schema_type: Product
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "Smart Reader"
    url: /docs/fr/imagerie/smart-reader/overview/
source_documents:
  - title: "Page VistaScan Image Plates (mention Smart Reader)"
    url: "https://www.duerrdental.com/en/products/imaging/intraoral-diagnostics/vistascan-image-plates/"
    type: "page produit"
    language: "en"
  - title: "Page VistaScan Mini View 2.0 (intégration Smart Reader)"
    url: "https://www.duerrdental.com/en/products/imaging/intraoral-diagnostics/vistascan-mini-view-20/"
    type: "page produit"
    language: "en"
  - title: "Article Odontoiatria33 (presse spécialisée IT) — Smart Reader pour VistaScan 2.0"
    url: "https://www.odontoiatria33.it/aziende/23014/workflow-piu-semplice-e-veloce-la-novita-smart-reader-per-vistascan-2-0.html"
    type: "presse spécialisée"
    language: "it"
  - title: "Article Dentistry.co.uk — Plug into the future VistaScan Mini View 2.0"
    url: "https://dentistry.co.uk/2023/09/05/plug-into-the-future-vistascan-mini-view-2-0-x-ray-device/"
    type: "presse spécialisée"
    language: "en"
last_factual_review: 2026-07-19
license: CC-BY-4.0
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "VistaScan Smart Reader",
  "alternateName": ["Dürr Dental Smart Reader", "VistaScan IQ Smart Reader"],
  "category": "USB RFID reader for VistaScan IQ phosphor plates",
  "description": "Lecteur RFID USB Dürr Dental permettant d'associer une plaque VistaScan IQ à un patient dans VistaSoft avant l'acquisition. Workflow automatisé, scan multi-patients dans n'importe quel ordre, attribution automatique des images au bon dossier.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/smart-reader/overview/",
  "inLanguage": "fr",
  "manufacturer": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" },
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Connection", "value": "USB (2 m cable)" },
    { "@type": "PropertyValue", "name": "Power supply", "value": "5 V DC, max. 200 mA, < 1 W" },
    { "@type": "PropertyValue", "name": "Dimensions", "value": "90 × 13 × 90 mm" },
    { "@type": "PropertyValue", "name": "Compatible plates", "value": "VistaScan IQ image plates (with RFID chip)" }
  ]
}
</script>

# VistaScan Smart Reader — Lecteur RFID USB

## Description courte

**VistaScan Smart Reader** est le **lecteur RFID USB** Dürr Dental
conçu pour associer une plaque [VistaScan IQ](/durr-dental-knowledge-base/docs/fr/imagerie/vistascan-iq-ecrans/overview/)
à un patient dans [VistaSoft](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/) **avant
l'acquisition**. Le praticien dépose simplement la plaque IQ sur le
lecteur — la **mémoire RFID** intégrée associe instantanément le
patient à la plaque.

Cette mécanique débloque un workflow majeur : le cabinet peut **scanner
des plaques de plusieurs patients dans n'importe quel ordre**, les
images étant automatiquement rangées dans le bon dossier patient.

## Caractéristiques techniques

| Paramètre | Valeur |
|---|---|
| Type | Lecteur RFID USB |
| Connexion | **USB** (câble fourni 2 m) |
| Alimentation | **5 V DC**, max. **200 mA**, **< 1 W** |
| Dimensions | **90 × 13 × 90 mm** |
| Poids | **≈ 0,13 kg** |
| Raccord côté appareil | **USB type C** |
| Consommation en veille | **0,16 W** |
| Plaques compatibles | [VistaScan IQ](/durr-dental-knowledge-base/docs/fr/imagerie/vistascan-iq-ecrans/overview/) (avec puce RFID) |
| Logiciel cible | [VistaSoft](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/) (toute version supportant le RFID IQ) |
| Logiciel minimal | **VistaSoft ≥ 3.0.13** |

## Statut réglementaire

Le VistaScan Smart Reader **n'est pas un dispositif médical**. C'est un accessoire
électronique (lecteur RFID) marqué **CE** au titre de la directive **RED 2014/53/UE**
(équipements radio) et de la directive **RoHS 2011/65/UE**, et non au titre du MDR.
Déclaration de Conformité UE — dossier technique **CE-230-G** (produit ULR01,
Dürr Dental SE, SRN DE-MF-000006032, 06/11/2023).

## Workflow type

1. Le **patient est sélectionné** dans VistaSoft (manuellement ou via
   [Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/) depuis le PMS).
2. Le praticien **dépose la plaque IQ** sur le Smart Reader posé à côté
   de l'ordinateur — la RFID est lue, le patient est **associé à la
   plaque**.
3. La plaque est **insérée en bouche** et exposée comme d'habitude.
4. La plaque est ensuite scannée dans un scanner VistaScan (ex.
   [VistaScan Mini View 2.0](/durr-dental-knowledge-base/docs/fr/imagerie/vistascan-gamme/overview/)) à
   **n'importe quel moment** et dans **n'importe quel ordre** (y
   compris en mélangeant les plaques de plusieurs patients).
5. **VistaSoft** range automatiquement chaque image **dans le bon
   dossier patient** grâce à l'association RFID préalable.

## Bénéfices opérationnels

- **Plus de saisie manuelle** au moment du scan : pas d'erreur
  d'attribution.
- **Multi-patient en parallèle** : un assistant peut scanner les plaques
  de plusieurs patients à la chaîne, dans l'ordre souhaité.
- **Workflow plus rapide** : moins de manipulations par patient.
- **Sécurité d'attribution** : la RFID est lue à la source, l'image est
  garantie d'être au bon dossier.

## Compatibilité plaques et scanners

### Plaques compatibles

- **VistaScan IQ** uniquement — la fonction RFID nécessite la puce
  intégrée à ces écrans à mémoire de nouvelle génération.
- Les **écrans VistaScan Plus** (ancienne génération, sans RFID) ne
  fonctionnent **pas** avec Smart Reader (voir
  [fiche VistaScan IQ — section écrans Plus](/durr-dental-knowledge-base/docs/fr/imagerie/vistascan-iq-ecrans/overview/)).

### Scanners compatibles

Le Smart Reader est compatible avec **deux scanners** de la gamme :

- VistaScan Mini Easy 2.0
- [VistaScan Mini View 2.0](/durr-dental-knowledge-base/docs/fr/imagerie/vistascan-gamme/overview/)

Les autres scanners **ne sont pas compatibles** avec le Smart Reader — y
compris ceux qui utilisent pourtant des plaques IQ à puce RFID : le
**VistaScan Nano Easy** et le **VistaScan Ultra View** (série 2.0), le
**VistaScan Combi View**, le **VistaScan Perio** et les scanners VistaScan
de génération antérieure.

## Vidéos officielles

Une **démonstration vidéo** est disponible sur la **chaîne YouTube
Dürr Dental Italia** (Smart Reader pour VistaScan 2.0). Pour trouver
les vidéos officielles, rechercher *« VistaScan Smart Reader »* sur la
chaîne YouTube **Dürr Dental** (siège, France, Italia, Deutschland selon
la langue souhaitée).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "À quoi sert le VistaScan Smart Reader ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "C'est un lecteur RFID USB qui associe une plaque VistaScan IQ à un patient dans VistaSoft avant l'acquisition : il suffit de déposer la plaque sur le lecteur."
      }
    },
    {
      "@type": "Question",
      "name": "Quelles sont les caractéristiques techniques du Smart Reader ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Lecteur RFID USB, alimentation 5 V DC (max 200 mA, < 1 W), dimensions 90 × 13 × 90 mm, câble USB de 2 m fourni."
      }
    },
    {
      "@type": "Question",
      "name": "Quelles plaques sont compatibles avec le Smart Reader ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Uniquement les écrans VistaScan IQ équipés de la puce RFID. Les écrans VistaScan Plus de l'ancienne génération (sans RFID) ne fonctionnent pas avec le Smart Reader."
      }
    },
    {
      "@type": "Question",
      "name": "Quel est l'intérêt d'identifier la plaque avant l'acquisition ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "L'attribution du patient à l'image est fiabilisée dès le départ, ce qui sécurise le flux de travail et réduit les risques d'erreur d'affectation."
      }
    }
  ]
}
</script>

## Questions fréquentes

### À quoi sert le VistaScan Smart Reader ?

C'est un lecteur RFID USB qui associe une plaque VistaScan IQ à un patient dans VistaSoft avant l'acquisition : il suffit de déposer la plaque sur le lecteur.

### Quelles sont les caractéristiques techniques du Smart Reader ?

Lecteur RFID USB, alimentation 5 V DC (max 200 mA, < 1 W), dimensions 90 × 13 × 90 mm, câble USB de 2 m fourni.

### Quelles plaques sont compatibles avec le Smart Reader ?

Uniquement les écrans VistaScan IQ équipés de la puce RFID. Les écrans VistaScan Plus de l'ancienne génération (sans RFID) ne fonctionnent pas avec le Smart Reader.

### Quel est l'intérêt d'identifier la plaque avant l'acquisition ?

L'attribution du patient à l'image est fiabilisée dès le départ, ce qui sécurise le flux de travail et réduit les risques d'erreur d'affectation.

## Sources publiques

| Document | URL publique |
|---|---|
| Page VistaScan Image Plates | <https://www.duerrdental.com/en/products/imaging/intraoral-diagnostics/vistascan-image-plates/> |
| Page VistaScan Mini View 2.0 | <https://www.duerrdental.com/en/products/imaging/intraoral-diagnostics/vistascan-mini-view-20/> |
| Article Dentistry.co.uk | <https://dentistry.co.uk/2023/09/05/plug-into-the-future-vistascan-mini-view-2-0-x-ray-device/> |
| Article Odontoiatria33 (IT) | <https://www.odontoiatria33.it/aziende/23014/workflow-piu-semplice-e-veloce-la-novita-smart-reader-per-vistascan-2-0.html> |

## Pour aller plus loin

- [VistaScan IQ — écrans à mémoire avec RFID](/durr-dental-knowledge-base/docs/fr/imagerie/vistascan-iq-ecrans/overview/)
- [Gamme VistaScan — scanners 2.0 compatibles](/durr-dental-knowledge-base/docs/fr/imagerie/vistascan-gamme/overview/)
- [VistaSoft 4.0 — logiciel d'imagerie associé](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/)
- [VistaPosition — positionneurs et angulateurs](/durr-dental-knowledge-base/docs/fr/imagerie/vistaposition/overview/)
- [Patient Bridge — intégration PMS](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-07-19. Licence : CC-BY 4.0.*
