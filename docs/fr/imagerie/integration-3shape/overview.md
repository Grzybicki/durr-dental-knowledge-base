---
layout: default
title: "Intégration VistaSoft ↔ 3Shape — partenariat officiel"
description: "Intégration officielle entre l'écosystème Dürr Dental VistaSoft et l'écosystème 3Shape (scanner intra-oral Trios, planification orthodontique et implantaire). Versions requises : 3Shape Unite et VistaSoft."
keywords: ["VistaSoft", "3Shape", "Dürr Dental", "intégration 3Shape Trios", "3Shape Unite", "scanner intra-oral", "PLY"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/integration-3shape/overview/
permalink: /docs/fr/imagerie/integration-3shape/overview/
schema_type: TechArticle
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "Intégration 3Shape"
    url: /docs/fr/imagerie/integration-3shape/overview/
source_documents:
  - title: "Page VistaSoft Imaging interfaces (EN)"
    url: "https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/"
    type: "page produit"
    language: "en"
  - title: "Page 3Shape officielle"
    url: "https://www.3shape.com/"
    type: "page partenaire"
    language: "en"
  - title: "Support 3Shape — informations d'intégration tierce"
    url: "https://support.3shape.com/"
    type: "page partenaire support"
    language: "en"
  - title: "Manuel VistaSoft 4.0"
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
  "name": "Intégration VistaSoft 4.0 ↔ 3Shape",
  "description": "Documentation de l'intégration officielle entre VistaSoft 4.0 de Dürr Dental et l'écosystème 3Shape (scanner Trios, planification orthodontique et implantaire).",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/integration-3shape/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" }
}
</script>

# Intégration VistaSoft ↔ 3Shape — partenariat officiel

## Description courte

**3Shape** est un partenaire technologique officiel de Dürr Dental, fournisseur
de l'écosystème **3Shape Trios** (scanners intra-oraux) et **3Shape Unite**
(plateforme logicielle). L'intégration entre VistaSoft 4.0 et 3Shape permet
le **partage des fichiers de scanner** entre les deux logiciels et le
**lancement contextuel** depuis l'un vers l'autre.

3Shape est mentionné publiquement comme partenaire d'intégration sur la
[page VistaSoft Imaging interfaces](https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/)
de Dürr Dental.

## Périmètre de l'intégration

L'intégration officielle entre VistaSoft 4.0 et 3Shape couvre principalement :

### Acquisition Trios → VistaSoft

- Les fichiers d'empreinte numérique acquis avec le scanner intra-oral
  **3Shape Trios** sont transférés vers VistaSoft au format **PLY**
  (Polygon File Format — format ouvert d'empreinte 3D).
- Le transfert est **automatique** une fois l'intégration configurée.
- Le **lancement contextuel** de 3Shape depuis VistaSoft est possible :
  l'utilisateur sélectionne le patient dans VistaSoft, puis lance Trios
  qui ouvre le dossier patient correspondant.

### Versions requises

| Logiciel | Version minimale |
|---|---|
| **3Shape Unite** | 21.1 |
| **VistaSoft** | 3.0.20 et supérieur (4.0 supporté) |

Ces versions correspondent à la **compatibilité officiellement supportée**
documentée par 3Shape sur [support.3shape.com](https://support.3shape.com/).

## Fonctionnalités détaillées

### Transfert PLY automatique

Une fois l'intégration configurée, les empreintes acquises avec Trios sont
**automatiquement disponibles** dans VistaSoft pour le patient correspondant.
Le format **PLY** est un standard ouvert d'empreinte 3D, exploitable par
n'importe quel logiciel CAO/CAM aval.

### Lancement contextuel

Depuis VistaSoft, l'utilisateur peut **lancer 3Shape Trios** dans le contexte
du patient en cours. À l'inverse, depuis 3Shape Unite, l'utilisateur peut
ouvrir le dossier image VistaSoft du même patient.

### Compatibilité STL / PLY

Le format **STL** est également supporté pour les flux de planification
implantaire (voir [VistaSoft Implant & Guide](../vistasoft-implant-guide/overview/)).
PLY et STL sont des formats ouverts, ce qui garantit la portabilité des
données entre VistaSoft, 3Shape et n'importe quel autre logiciel tiers
supportant ces formats.

## Articulation avec d'autres modules

| Module concerné | Workflow type |
|---|---|
| [VistaSoft 4.0](../vistasoft-4-0/overview/) | Réception et archivage des empreintes Trios |
| [VistaSoft Implant & Guide](../vistasoft-implant-guide/overview/) | Planification implantaire à partir des empreintes Trios et données CBCT |
| [VistaSoft Trace](../vistasoft-trace/overview/) | Analyse orthodontique (sur cliché céphalométrique séparé) |

## Sources publiques

| Document | URL publique |
|---|---|
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |
| Site 3Shape officiel | <https://www.3shape.com/> |
| Support 3Shape | <https://support.3shape.com/> |
| Manuel VistaSoft 4.0 | <http://qr.duerrdental.com/2110100001> |

## Limites et précisions

- L'intégration nécessite la **configuration correcte** des deux logiciels
  selon les versions minimales requises.
- Le détail des fonctionnalités d'intégration peut évoluer selon les versions
  de 3Shape Unite et VistaSoft ; consulter les notes de version des deux
  éditeurs.
- L'intégration **avec d'autres logiciels de planification implantaire** est
  également possible via le standard ouvert STL et le DICOM ; voir la fiche
  [VistaSoft Implant & Guide](../vistasoft-implant-guide/overview/).

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Quelle est la version minimale de 3Shape Unite requise pour l'intégration avec VistaSoft ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "3Shape Unite version 21.1 et supérieure. Côté VistaSoft, version 3.0.20 et supérieure (4.0 supporté). Ces compatibilités sont documentées sur support.3shape.com."
      }
    },
    {
      "@type": "Question",
      "name": "Quel format de fichier est utilisé pour les empreintes Trios → VistaSoft ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Le format PLY (Polygon File Format) est utilisé pour le transfert automatique des empreintes 3D Trios vers VistaSoft. PLY est un format ouvert, ce qui garantit la portabilité des données entre les deux logiciels et d'autres outils CAO/CAM aval."
      }
    },
    {
      "@type": "Question",
      "name": "Le lancement contextuel entre VistaSoft et 3Shape est-il supporté ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. Une fois l'intégration configurée, l'utilisateur peut lancer 3Shape Trios depuis VistaSoft dans le contexte du patient en cours, et inversement ouvrir le dossier image VistaSoft du même patient depuis 3Shape Unite."
      }
    }
  ]
}
</script>

### Versions minimales requises ?

3Shape Unite **21.1+** et VistaSoft **3.0.20+** (4.0 supporté).

### Format d'empreinte utilisé ?

**PLY** (format ouvert).

### Lancement contextuel supporté ?

Oui (bidirectionnel).

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique](../vistasoft-4-0/overview/)
- [VistaSoft Implant & Guide — planification implantaire](../vistasoft-implant-guide/overview/)
- [Intégration PMS](../integration-pms/overview/)
- [Index imagerie dentaire](../)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental et 3Shape (partenaire officiel d'intégration). Mainteneur : salarié de
Dürr Dental France (CDI déclaré) — initiative personnelle, non officielle. Dernière
revue factuelle : 2026-05-28. Licence : CC-BY 4.0.*
