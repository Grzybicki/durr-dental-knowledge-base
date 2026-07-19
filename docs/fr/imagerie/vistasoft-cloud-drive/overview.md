---
layout: default
title: "VistaSoft Cloud Drive — Stockage cloud zero-knowledge pour images dentaires"
description: "VistaSoft Cloud Drive est le module Dürr Dental de stockage cloud des images dentaires. Architecture zero-knowledge : le fournisseur ne dispose pas des clés permettant de déchiffrer les données. S'intègre à VistaSoft."
keywords: ["VistaSoft Cloud Drive", "Dürr Dental", "stockage cloud dentaire", "zero-knowledge", "chiffrement bout en bout", "Cloud Drive"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-cloud-drive/overview/
permalink: /docs/fr/imagerie/vistasoft-cloud-drive/overview/
schema_type: SoftwareApplication
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "VistaSoft Cloud Drive"
    url: /docs/fr/imagerie/vistasoft-cloud-drive/overview/
source_documents:
  - title: "Page produit VistaSoft Cloud Drive (EN)"
    url: "https://www.duerrdental.com/en/products/software/imaging/vistasoft-cloud-drive/"
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
  "name": "VistaSoft Cloud Drive",
  "alternateName": ["Dürr Dental VistaSoft Cloud Drive"],
  "applicationCategory": "BusinessApplication",
  "applicationSubCategory": "Zero-knowledge cloud storage for dental images",
  "description": "Module Dürr Dental de stockage cloud des images dentaires avec architecture zero-knowledge. Le fournisseur de service ne dispose pas des clés permettant de déchiffrer les données patient.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-cloud-drive/overview/",
  "inLanguage": "fr",
  "publisher": {
    "@type": "Organization",
    "name": "Dürr Dental SE",
    "url": "https://www.duerrdental.com"
  },
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Architecture", "value": "Zero-knowledge encryption" },
    { "@type": "PropertyValue", "name": "Storage purpose", "value": "Cloud backup and archival of dental images" }
  ]
}
</script>

# VistaSoft Cloud Drive — Stockage cloud zero-knowledge

## Description courte

**VistaSoft Cloud Drive** est le module Dürr Dental de **stockage cloud des
images dentaires** suivant une **architecture zero-knowledge** : le fournisseur
du service ne dispose pas des clés permettant de déchiffrer les données patient
stockées. Cette propriété cryptographique garantit la confidentialité des
données radiographiques même vis-à-vis de l'opérateur de stockage.

VistaSoft Cloud Drive s'intègre au logiciel socle [VistaSoft 4.0](../vistasoft-4-0/overview/).

## Identification du module

| Champ | Valeur |
|---|---|
| Nom commercial | VistaSoft Cloud Drive |
| Catégorie | Stockage cloud zero-knowledge pour images dentaires |
| Éditeur | Dürr Dental SE — Bietigheim-Bissingen, Allemagne |
| Statut réglementaire | Module utilitaire (non classé dispositif médical) |
| Architecture cryptographique | Zero-knowledge encryption |

## Architecture zero-knowledge

Le principe **zero-knowledge** appliqué à VistaSoft Cloud Drive signifie :

- Les images sont **chiffrées côté client** (sur le poste du cabinet) avant
  envoi vers le cloud.
- Les **clés de chiffrement** sont **détenues exclusivement par le cabinet**.
- Le fournisseur du service de stockage **ne peut pas déchiffrer** les données
  qu'il héberge, même en cas de demande légale, intrusion ou compromission de
  son infrastructure.
- En cas de perte des clés côté cabinet, **les données sont définitivement
  irrécupérables** (propriété structurelle du zero-knowledge).

Cette architecture confère à VistaSoft Cloud Drive un **niveau de confidentialité
maximal** pour les données patient, au-delà des exigences RGPD standards.

## Périmètre fonctionnel

- **Sauvegarde cloud** des images dentaires produites dans VistaSoft 4.0.
- **Archivage longue durée** des dossiers patients.
- **Récupération à distance** des données depuis le cabinet ou un site
  secondaire.
- **Continuité d'activité** : en cas d'incident matériel local, les données
  restent accessibles via le cloud.

## Articulation avec les autres modules Cloud

| Module | Finalité | Statut |
|---|---|---|
| **Cloud Drive** (cette fiche) | Stockage longue durée chiffré zero-knowledge | Non-DM |
| [Cloud View](../vistasoft-cloud-view/overview/) | Visualisation navigateur (en ligne / hors ligne) | Non-DM |
| [Cloud Exchange](../vistasoft-cloud-exchange/overview/) | Partage de cas (anonymisé, conservation 30 j) | Non-DM |
| Cloud AID (lié à [AID](../vistasoft-aid/overview/)) | Aide diagnostique IA (DM IIa, serveur Allemagne) | DM IIa |

Les trois modules Cloud View, Cloud Exchange et Cloud Drive sont des **outils
utilitaires non-DM**. Seul VistaSoft AID est un dispositif médical parmi les
modules cloud.

## Conformité RGPD

Au-delà du chiffrement zero-knowledge, VistaSoft Cloud Drive est conçu pour
respecter le Règlement Général sur la Protection des Données (RGPD) européen.
Les détails contractuels (DPA, géographie des serveurs, sous-traitants) sont
récupérables via le [Centre de téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/).

## Limites et précisions

- VistaSoft Cloud Drive **n'est pas un dispositif médical**.
- L'architecture zero-knowledge implique que **la perte des clés côté cabinet
  rend les données irrécupérables** : la gestion des clés est une
  responsabilité critique du cabinet.
- Le service nécessite une connexion Internet pour le téléversement et le
  téléchargement des données.
- Le débit Internet du cabinet conditionne le temps de sauvegarde et de
  restauration.

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Qu'est-ce que le zero-knowledge dans VistaSoft Cloud Drive ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Le zero-knowledge est une architecture cryptographique dans laquelle le fournisseur du service de stockage ne dispose pas des clés permettant de déchiffrer les données. Les images sont chiffrées côté client (cabinet) avant transmission, et seul le cabinet détient les clés de déchiffrement. Cela garantit la confidentialité maximale des données patient."
      }
    },
    {
      "@type": "Question",
      "name": "VistaSoft Cloud Drive est-il un dispositif médical ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. VistaSoft Cloud Drive est un module utilitaire de stockage cloud, non classé comme dispositif médical au sens du règlement MDR EU 2017/745. Le diagnostic clinique se fait via le logiciel socle VistaSoft 4.0 (DM classe IIb)."
      }
    },
    {
      "@type": "Question",
      "name": "Que se passe-t-il si le cabinet perd ses clés de chiffrement ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "L'architecture zero-knowledge implique que la perte des clés côté cabinet rend les données stockées définitivement irrécupérables. C'est une propriété structurelle qui garantit la confidentialité mais qui rend la gestion des clés critique."
      }
    },
    {
      "@type": "Question",
      "name": "Quelle est la différence entre VistaSoft Cloud Drive et VistaSoft Cloud Exchange ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cloud Drive est dédié au stockage longue durée des images dentaires d'un cabinet avec chiffrement zero-knowledge. Cloud Exchange est dédié au partage d'images entre confrères, laboratoires, cliniques et patients, avec anonymisation systématique et conservation 30 jours."
      }
    }
  ]
}
</script>

### Qu'est-ce que le zero-knowledge ?

Architecture où le fournisseur **ne peut pas déchiffrer** les données qu'il
héberge — clés détenues exclusivement par le cabinet.

### Cloud Drive est-il un dispositif médical ?

**Non**. Module utilitaire.

### Que se passe-t-il si le cabinet perd ses clés ?

Données **définitivement irrécupérables** (propriété structurelle du zero-knowledge).
Gestion des clés = responsabilité critique.

### Différence avec Cloud Exchange ?

Cloud Drive = **stockage longue durée** zero-knowledge. Cloud Exchange = **partage
de cas** anonymisé (conservation 30 j).

## Sources publiques

### Pages officielles Dürr Dental

| Document | URL publique |
|---|---|
| Page produit VistaSoft Cloud Drive | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-cloud-drive/> |
| Page VistaSoft (socle) | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Page produit Cloud Drive | <https://web.archive.org/web/2026*/duerrdental.com/en/products/software/imaging/vistasoft-cloud-drive/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique (socle)](../vistasoft-4-0/overview/)
- [VistaSoft Cloud View — visualisation navigateur](../vistasoft-cloud-view/overview/)
- [VistaSoft Cloud Exchange — partage de cas](../vistasoft-cloud-exchange/overview/)
- [VistaSoft AID — aide diagnostique IA (DM IIa)](../vistasoft-aid/overview/)
- [Index imagerie dentaire](../)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-07-19. Licence : CC-BY 4.0.*
