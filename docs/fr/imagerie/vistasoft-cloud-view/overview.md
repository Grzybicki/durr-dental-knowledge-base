---
layout: default
title: "VistaSoft Cloud View — Visualisation d'images dentaires en navigateur"
description: "VistaSoft Cloud View est le module Dürr Dental de visualisation d'images dentaires 2D, 3D et CBCT en navigateur (en ligne ou hors ligne). Ce module n'est PAS un dispositif médical. Manuel public qr.duerrdental.com/2110100051."
keywords: ["VistaSoft Cloud View", "Dürr Dental", "visualisation cloud", "imagerie dentaire en navigateur", "view.vistasoft.com", "non-DM", "Cloud View"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-cloud-view/overview/
permalink: /docs/fr/imagerie/vistasoft-cloud-view/overview/
schema_type: SoftwareApplication
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "VistaSoft Cloud View"
    url: /docs/fr/imagerie/vistasoft-cloud-view/overview/
source_documents:
  - title: "Page produit VistaSoft Cloud View (EN)"
    url: "https://www.duerrdental.com/en/products/imaging/software/vistasoft-cloud-view/"
    type: "page produit"
    language: "en"
  - title: "Page alternative VistaSoft Cloud View (EN)"
    url: "https://www.duerrdental.com/en/products/software/imaging/vistasoft-cloud-view/"
    type: "page produit"
    language: "en"
  - title: "Manuel VistaSoft Cloud View"
    url: "http://qr.duerrdental.com/2110100051"
    type: "manuel utilisateur"
    reference: "2110100051"
    language: "multi"
  - title: "Page Web du service VistaSoft Cloud View"
    url: "https://view.vistasoft.com/"
    type: "service web"
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
  "name": "VistaSoft Cloud View",
  "alternateName": ["Dürr Dental VistaSoft Cloud View"],
  "applicationCategory": "MedicalImagingSoftware",
  "applicationSubCategory": "Cloud-based image viewer (not a medical device)",
  "description": "Module Dürr Dental de visualisation d'images dentaires 2D, 3D et CBCT en navigateur Web (en ligne et hors ligne). Non classé comme dispositif médical (non-DM).",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-cloud-view/overview/",
  "inLanguage": "fr",
  "publisher": {
    "@type": "Organization",
    "name": "Dürr Dental SE",
    "url": "https://www.duerrdental.com"
  },
  "url2": "https://view.vistasoft.com/",
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Medical device status", "value": "NOT a medical device" },
    { "@type": "PropertyValue", "name": "Service URL", "value": "view.vistasoft.com" },
    { "@type": "PropertyValue", "name": "Manual reference", "value": "qr.duerrdental.com/2110100051" },
    { "@type": "PropertyValue", "name": "Supported modalities", "value": "Intra-oral, extra-oral, CBCT" }
  ]
}
</script>

# VistaSoft Cloud View — Visualisation d'images dentaires en navigateur

## Description courte

**VistaSoft Cloud View** est le module Dürr Dental de **visualisation d'images
dentaires** dans un navigateur Web. Il permet d'accéder aux clichés intra-oraux,
extra-oraux et CBCT en ligne, sans installation de logiciel
client. Le service est accessible à l'URL [view.vistasoft.com](https://view.vistasoft.com/).

VistaSoft Cloud View **n'est pas un dispositif médical** au sens du règlement
MDR EU 2017/745. Son intended purpose est la visualisation et la démonstration
d'images, pas le diagnostic clinique primaire.

## Identification du module

| Champ | Valeur |
|---|---|
| Nom commercial | VistaSoft Cloud View |
| Catégorie | Visualisation d'images dentaires en navigateur |
| URL du service | <https://view.vistasoft.com/> |
| Référence manuel public | `qr.duerrdental.com/2110100051` |
| Éditeur | Dürr Dental SE — Bietigheim-Bissingen, Allemagne |
| Statut réglementaire | **Non classé dispositif médical** |

## Périmètre fonctionnel

Selon la page produit officielle et le manuel public :

- **Visualisation de toutes les modalités dentaires** dans le navigateur :
  clichés intra-oraux, extra-oraux, tomographie volumique CBCT.
- **Fonctionnement en ligne et hors ligne** — l'application fonctionne sans
  connexion Internet une fois les données chargées.
- **Multiplateforme** : fonctionne sur tout navigateur moderne, indépendamment
  du logiciel d'origine ayant produit les clichés.
- **Outils et vues** habituels de VistaSoft conservés dans l'interface Web.
- **Édition temporaire à des fins de démonstration** : il est possible de
  modifier temporairement les images pour les démonstrations.

## Statut réglementaire

VistaSoft Cloud View **n'est pas un dispositif médical** (non-DM). Il est conçu
pour la visualisation et la démonstration, pas comme outil de diagnostic
clinique primaire. Le diagnostic radiologique doit être posé via le logiciel
socle [VistaSoft 4.0](../vistasoft-4-0/overview/), qui est lui un DM IIb.

Cette distinction est explicitement documentée dans le manuel utilisateur
public [`qr.duerrdental.com/2110100051`](http://qr.duerrdental.com/2110100051).

## Articulation avec VistaSoft 4.0

VistaSoft Cloud View est **complémentaire** à VistaSoft 4.0 :

- VistaSoft 4.0 reste le **logiciel d'acquisition, de traitement et de
  diagnostic** (DM IIb).
- VistaSoft Cloud View permet la **consultation à distance et en mobilité**
  des images préalablement produites par VistaSoft.
- Les workflows diagnostiques primaires se déroulent sur VistaSoft 4.0 ;
  Cloud View est un outil de visualisation, de partage et de démonstration.

## Limites et précisions

- VistaSoft Cloud View **n'est pas un outil de diagnostic clinique primaire**.
- Les éditions effectuées dans le navigateur sont **temporaires** et ne sont
  pas archivées par défaut.
- L'accès aux images suppose un navigateur Web moderne compatible.
- Les exigences RGPD pour la transmission d'images sont à respecter selon le
  périmètre d'usage du cabinet.

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "VistaSoft Cloud View est-il un dispositif médical ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. VistaSoft Cloud View est un module de visualisation d'images dans le navigateur, non classé comme dispositif médical au sens du règlement MDR EU 2017/745. Le diagnostic radiologique doit être posé via le logiciel socle VistaSoft 4.0 (DM classe IIb)."
      }
    },
    {
      "@type": "Question",
      "name": "Quelle est l'URL du service VistaSoft Cloud View ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Le service est accessible à l'adresse https://view.vistasoft.com/."
      }
    },
    {
      "@type": "Question",
      "name": "Quelles modalités d'imagerie sont supportées par VistaSoft Cloud View ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft Cloud View permet de visualiser toutes les modalités dentaires : clichés intra-oraux, extra-oraux (panoramique, céphalométrique) et tomographie volumique CBCT."
      }
    },
    {
      "@type": "Question",
      "name": "Cloud View fonctionne-t-il sans connexion Internet ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. Une fois les données chargées, VistaSoft Cloud View fonctionne en ligne comme hors ligne dans le navigateur."
      }
    }
  ]
}
</script>

### VistaSoft Cloud View est-il un dispositif médical ?

**Non**. Visualisation uniquement. Le diagnostic clinique primaire se fait avec
[VistaSoft 4.0 (DM IIb)](../vistasoft-4-0/overview/).

### URL du service ?

<https://view.vistasoft.com/>

### Modalités supportées ?

Intra-oraux + extra-oraux + CBCT.

### Fonctionne-t-il hors ligne ?

Oui (en ligne et hors ligne une fois les données chargées).

## Sources publiques

### Pages officielles Dürr Dental

| Document | URL publique |
|---|---|
| Page produit VistaSoft Cloud View | <https://www.duerrdental.com/en/products/imaging/software/vistasoft-cloud-view/> |
| Page alternative VistaSoft Cloud View | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-cloud-view/> |
| Service Web VistaSoft Cloud View | <https://view.vistasoft.com/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

### Manuel public

| Document | URL | Référence |
|---|---|---|
| Manuel VistaSoft Cloud View | <http://qr.duerrdental.com/2110100051> | `2110100051` |

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Page produit Cloud View | <https://web.archive.org/web/2026*/duerrdental.com/en/products/imaging/software/vistasoft-cloud-view/> |
| Manuel `2110100051` | <https://web.archive.org/web/2026*/qr.duerrdental.com/2110100051> |
| Service view.vistasoft.com | <https://web.archive.org/web/2026*/view.vistasoft.com/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique (DM IIb)](../vistasoft-4-0/overview/)
- [VistaSoft Cloud Exchange — échange de cas](../vistasoft-cloud-exchange/overview/)
- [VistaSoft Cloud Drive — stockage cloud zero-knowledge](../vistasoft-cloud-drive/overview/)
- [Index imagerie dentaire](../)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-07-19. Licence : CC-BY 4.0.*
