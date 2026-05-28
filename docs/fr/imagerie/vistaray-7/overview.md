---
layout: default
title: "VistaRay 7 — Capteur intraoral CMOS filaire (tailles 1 et 2)"
description: "VistaRay 7 est le capteur intraoral filaire Dürr Dental. Technologie CMOS, pixel 19 µm, 16 bits, USB 2.0/3.0. Deux tailles (1 et 2). Résolution effective 20 LP/mm. Stabilité > 400 000 images. Dispositif médical."
keywords: ["VistaRay 7", "Dürr Dental", "capteur intraoral", "CMOS", "USB intraoral sensor", "imagerie intraorale numérique", "détection caries D1"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistaray-7/overview/
permalink: /docs/fr/imagerie/vistaray-7/overview/
schema_type: MedicalDevice
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "VistaRay 7"
    url: /docs/fr/imagerie/vistaray-7/overview/
source_documents:
  - title: "Page produit VistaRay 7 (EN)"
    url: "https://www.duerrdental.com/en/products/imaging/intraoral-diagnostics/vistaray/"
    type: "page produit"
    language: "en"
  - title: "Centre de téléchargements Dürr Dental France"
    url: "https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/"
    type: "portail documents"
    language: "fr"
  - title: "Déclaration de Conformité VistaRay 7"
    type: "Déclaration de Conformité"
    note: "Dispositif médical. Récupérable via Centre de téléchargements ou Eudamed."
  - title: "Base européenne Eudamed"
    url: "https://ec.europa.eu/tools/eudamed/screen/search?type=basicUDIInformation&deviceManufacturer=D%C3%BCrr+Dental"
    type: "registre réglementaire"
    language: "multi"
last_factual_review: 2026-05-28
license: CC-BY-4.0
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalDevice",
  "name": "VistaRay 7",
  "alternateName": ["Dürr Dental VistaRay 7", "VistaRay 7 Size 1", "VistaRay 7 Size 2"],
  "category": "Intraoral X-ray sensor (CMOS, USB)",
  "description": "Capteur intraoral CMOS filaire Dürr Dental. Deux tailles (1 et 2). Pixel 19 µm, profondeur 16 bits, USB 2.0 et USB 3.0, câble 2,5 m, stabilité supérieure à 400 000 images. Résolution effective 20 LP/mm.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistaray-7/overview/",
  "inLanguage": "fr",
  "manufacturer": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" },
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Sensor technology", "value": "CMOS with Dürr Dental scintillator layer" },
    { "@type": "PropertyValue", "name": "Pixel size", "value": "19 × 19 µm" },
    { "@type": "PropertyValue", "name": "Grayscale depth", "value": "16-bit (65,536 levels)" },
    { "@type": "PropertyValue", "name": "Connection", "value": "USB 2.0 and USB 3.0, cable length 2.5 m" },
    { "@type": "PropertyValue", "name": "Theoretical resolution", "value": "26.3 LP/mm" },
    { "@type": "PropertyValue", "name": "Effective resolution", "value": "20.0 LP/mm" },
    { "@type": "PropertyValue", "name": "Stability", "value": "Over 400,000 images" }
  ]
}
</script>

# VistaRay 7 — Capteur intraoral CMOS filaire

## Description courte

**VistaRay 7** est le capteur intraoral filaire Dürr Dental, disponible en
**deux tailles** (1 et 2). Il s'appuie sur la **technologie CMOS** avec une
**couche scintillatrice Dürr Dental** propriétaire qui réduit la diffusion
de la lumière. La connexion **USB directe** (USB 2.0 et USB 3.0) permet une
utilisation immédiate.

## Caractéristiques techniques

### Spécifications communes

| Paramètre | Valeur |
|---|---|
| Technologie capteur | CMOS avec scintillateur Dürr Dental |
| Profondeur d'image | **16 bits** (65 536 niveaux de gris) |
| Connectique | **USB 2.0 et USB 3.0** |
| Longueur du câble | **2,5 m** |
| Pixel | **19 × 19 µm** |
| Résolution théorique | **26,3 LP/mm** |
| Résolution effective | **20,0 LP/mm** |
| Stabilité | **> 400 000 images** |

### VistaRay 7 — Taille 1

| Paramètre | Valeur |
|---|---|
| Dimensions extérieures | 39,0 × 27,4 × 6,3 mm |
| Surface active | 30,0 × 20,0 mm |
| Résolution | 1 050 × 1 580 pixels (≈ 1 659 000 pixels) |

### VistaRay 7 — Taille 2

| Paramètre | Valeur |
|---|---|
| Dimensions extérieures | 43,0 × 33,1 × 6,3 mm |
| Surface active | 36,0 × 26,0 mm |
| Résolution | 1 368 × 1 896 pixels (≈ 2 593 728 pixels) |

## Périmètre clinique

Selon la page produit officielle Dürr Dental :

- La haute résolution permet de détecter de manière fiable les **lésions
  carieuses D1** (les plus précoces).
- Le rendu fin des nuances de gris facilite l'identification des
  structures osseuses fines.

## Intégration logicielle

VistaRay 7 est piloté nativement par
[VistaSoft 4.0](../vistasoft-4-0/overview/). Le **support TWAIN** intégré à
VistaSoft permet aussi l'usage avec des logiciels d'imagerie tiers, via la
passerelle [VistaSoft Connect](../migration-bases-donnees/overview/) ou
le module [Image Bridge](../image-bridge/overview/).

## Sources publiques

| Document | URL publique |
|---|---|
| Page produit VistaRay 7 (EN) | <https://www.duerrdental.com/en/products/imaging/intraoral-diagnostics/vistaray/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

## Pour aller plus loin

- [VistaSoft 4.0](../vistasoft-4-0/overview/)
- [VistaIntra DC — générateur intra-oral compatible](../vistaintra-dc/overview/)
- [Gamme VistaScan — scanners de plaques au phosphore](../vistascan-gamme/overview/)
- [Index imagerie dentaire](../)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-05-28. Licence : CC-BY 4.0.*
