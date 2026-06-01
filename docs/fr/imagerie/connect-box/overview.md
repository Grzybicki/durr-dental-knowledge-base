---
layout: default
title: "Connect Box — Passerelle d'intégration des équipements vers VistaSoft Monitor"
description: "Connect Box est l'appareil Dürr Dental qui permet d'intégrer dans VistaSoft Monitor des équipements dentaires existants (compresseurs, aspiration, autres) sans interface réseau native. Connexion LAN ou WLAN. Compatible cross-fabricant."
keywords: ["Connect Box", "Dürr Dental", "VistaSoft Monitor IoT", "intégration équipement", "passerelle réseau", "LAN WLAN", "rétrofit IoT cabinet dentaire"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/connect-box/overview/
permalink: /docs/fr/imagerie/connect-box/overview/
schema_type: Product
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "Connect Box"
    url: /docs/fr/imagerie/connect-box/overview/
source_documents:
  - title: "Page Connect Box (EN)"
    url: "https://www.duerrdental.com/en/solutions/networking/connect-box/"
    type: "page produit"
    language: "en"
  - title: "Page VistaSoft Monitor — solution IoT (EN)"
    url: "https://www.duerrdental.com/en/solutions/networking/vistasoft-monitor/"
    type: "page produit"
    language: "en"
  - title: "Portail VistaSoft Monitor (help)"
    url: "https://help.vsmonitor.com/dd/www.duerrdental.com/en/vistasoftmonitor/"
    type: "portail aide officiel"
    language: "en"
  - title: "Application iOS VistaSoft Monitor"
    url: "https://apps.apple.com/in/app/vistasoft-monitor/id966166778"
    type: "application mobile officielle"
    language: "en"
  - title: "Application Android VistaSoft Monitor"
    url: "https://play.google.com/store/apps/details?id=com.duerrdental.vistasoftmonitor"
    type: "application mobile officielle"
    language: "en"
last_factual_review: 2026-05-29
license: CC-BY-4.0
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Connect Box",
  "alternateName": ["Dürr Dental Connect Box", "VistaSoft Monitor Connect Box"],
  "category": "IoT gateway for retrofitting dental equipment to VistaSoft Monitor",
  "description": "Passerelle d'intégration Dürr Dental qui permet à des équipements dentaires existants sans interface réseau native d'être intégrés dans le tableau de bord VistaSoft Monitor. Connexion LAN ou WLAN. Compatibilité cross-fabricant.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/connect-box/overview/",
  "inLanguage": "fr",
  "manufacturer": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" },
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Connectivity", "value": "LAN (wired) and WLAN (wireless)" },
    { "@type": "PropertyValue", "name": "Compatibility", "value": "Cross-manufacturer — works with dental equipment from various manufacturers" },
    { "@type": "PropertyValue", "name": "Use case", "value": "Retrofit older or non-networked dental equipment into VistaSoft Monitor" }
  ]
}
</script>

# Connect Box — Passerelle d'intégration vers VistaSoft Monitor

## Description courte

**Connect Box** est l'appareil Dürr Dental qui permet d'**intégrer dans
le tableau de bord [VistaSoft Monitor](../vistasoft-monitor/overview/)
des équipements dentaires existants** (compresseurs, aspiration, autres
équipements techniques) **sans interface réseau native**. Elle constitue
la **passerelle IoT** entre les équipements traditionnels et la
plateforme de surveillance temps réel Dürr Dental.

## Cas d'usage principal — Rétrofit IoT

Verbatim de la page produit officielle :

> *« Devices without a network interface can be integrated into VistaSoft
> Monitor via the Connect Box. (…) The Connect Box is able to integrate
> devices into VistaSoft Monitor that are already in use and not
> compatible for networking, meaning that even practice supply equipment
> that is several years old can become part of a digitally networked
> practice. »*

Concrètement, la Connect Box permet à un cabinet équipé d'un compresseur
ou d'un système d'aspiration de **plusieurs années** (et donc sans
interface réseau d'origine) de bénéficier de la **surveillance IoT
temps réel** de VistaSoft Monitor — sans avoir à remplacer son
équipement.

## Connectivité

| Option | Description |
|---|---|
| **LAN** (filaire) | Connexion Ethernet standard au réseau du cabinet |
| **WLAN** (sans fil) | Connexion Wi-Fi pour les configurations où le câblage est complexe |

Le choix entre LAN et WLAN se fait selon l'**infrastructure réseau** du
cabinet et les **contraintes d'installation** (distance au switch,
qualité du signal Wi-Fi).

## Compatibilité cross-fabricant

Verbatim de la page produit officielle :

> *« With a Connect Box, you can add devices from other manufacturers or
> equipment that is not network-capable to your VistaSoft Monitor
> account for basic monitoring of the most important operating
> parameters. Additionally, the technology is compatible across
> manufacturers, so all devices can reap the benefits of VistaSoft
> Monitor. »*

Cette **interopérabilité** permet une **mise en réseau homogène** des
équipements du cabinet, y compris ceux d'autres fabricants, dans une
**vue unifiée**.

## Paramètres surveillés

D'après la page produit officielle, la Connect Box mesure **tous les
paramètres pertinents** de l'équipement connecté et les transmet
automatiquement à VistaSoft Monitor. Les paramètres typiques incluent
(selon le type d'équipement) :

- **État de fonctionnement** (marche / arrêt / dégradé).
- **Pression**, **débit**, **température** selon l'équipement.
- **Alertes** sur surcharges et défaillances.
- **Historique d'utilisation**.

Les **risques surveillés** mentionnés sur la page officielle :
**surchauffe**, **défaillance d'unité**, **surcharges et surtensions**.

## Équipements Dürr Dental compatibles VistaSoft Monitor

La Connect Box permet aussi d'intégrer les équipements Dürr Dental **plus
anciens** ou ceux dont l'**interface réseau native** n'est pas
disponible. Les équipements concernés incluent :

| Catégorie | Lien fiche |
|---|---|
| Compresseurs Silver Airline | [Fiche](/docs/fr/conventionnel/silver-airline/overview/) |
| Compresseurs Tornado | [Fiche](/docs/fr/conventionnel/tornado/overview/) |
| Power Tower (Silence + View) | [Fiche](/docs/fr/conventionnel/power-tower/overview/) |
| Compresseurs CAD/CAM | [Fiche](/docs/fr/conventionnel/cad-cam-compresseurs/overview/) |
| Aspiration Tyscor (humide + sec) | [Fiche](/docs/fr/conventionnel/tyscor-aspiration/overview/) |
| Récupérateurs d'amalgame | [Fiche](/docs/fr/conventionnel/recuperateurs-amalgame/overview/) |
| VC 65 — aspiration chirurgicale | [Fiche](/docs/fr/conventionnel/aspiration-chirurgicale/overview/) |
| Hygoclave 40 / 50 / 90 (stérilisateurs) | [Fiche](/docs/fr/hygiene-chimie/hygoclave-hygopure/overview/) |
| Hygowater (traitement eau fauteuils) | [Fiche](/docs/fr/hygiene-chimie/hygowater-traitement-eau/overview/) |

## Applications mobiles VistaSoft Monitor

Une fois les équipements intégrés via Connect Box, le suivi s'effectue
via le portail Web ou les applications mobiles :

| Plateforme | URL d'installation |
|---|---|
| **iOS (iPad, iPhone)** | <https://apps.apple.com/in/app/vistasoft-monitor/id966166778> |
| **Android (smartphone, tablette)** | <https://play.google.com/store/apps/details?id=com.duerrdental.vistasoftmonitor> |
| **Portail Web aide** | <https://help.vsmonitor.com/dd/www.duerrdental.com/en/vistasoftmonitor/> |

## Profils utilisateurs

VistaSoft Monitor distingue **trois profils** d'accès aux données via la
Connect Box :

| Profil | Page officielle |
|---|---|
| **Praticiens / exploitants du cabinet** | <https://www.duerrdental.com/en/products/software/networking-for-dental-practices/vistasoft-monitor/vistasoft-monitor-for-practice-operators/> |
| **Techniciens de service** | <https://www.duerrdental.com/en/products/software/networking-for-dental-practices/vistasoft-monitor/vistasoft-monitor-for-service-technicians/> |
| **Gestionnaires de dépôt** | <https://www.duerrdental.com/en/products/software/networking-for-dental-practices/vistasoft-monitor/vistasoft-monitor-for-depot-service-managers/> |

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "À quoi sert la Connect Box ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "À intégrer dans le tableau de bord VistaSoft Monitor des équipements dentaires (compresseurs, aspiration, etc.) dépourvus d'interface réseau native. Elle joue le rôle de passerelle IoT."
      }
    },
    {
      "@type": "Question",
      "name": "Quel est le cas d'usage principal de la Connect Box ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Le rétrofit IoT : connecter des appareils déjà en service et non compatibles réseau à VistaSoft Monitor, y compris des équipements techniques du cabinet."
      }
    },
    {
      "@type": "Question",
      "name": "Quelle connectivité propose la Connect Box ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Une connexion LAN filaire (Ethernet) ou WLAN sans fil (Wi-Fi), selon l'infrastructure réseau et les contraintes d'installation du cabinet."
      }
    },
    {
      "@type": "Question",
      "name": "En quoi diffère-t-elle d'une intégration native ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Les générations récentes d'équipements se connectent nativement à VistaSoft Monitor ; la Connect Box permet d'y raccorder les générations antérieures sans interface réseau."
      }
    }
  ]
}
</script>

## Questions fréquentes

### À quoi sert la Connect Box ?

À intégrer dans le tableau de bord VistaSoft Monitor des équipements dentaires (compresseurs, aspiration, etc.) dépourvus d'interface réseau native. Elle joue le rôle de passerelle IoT.

### Quel est le cas d'usage principal de la Connect Box ?

Le rétrofit IoT : connecter des appareils déjà en service et non compatibles réseau à VistaSoft Monitor, y compris des équipements techniques du cabinet.

### Quelle connectivité propose la Connect Box ?

Une connexion LAN filaire (Ethernet) ou WLAN sans fil (Wi-Fi), selon l'infrastructure réseau et les contraintes d'installation du cabinet.

### En quoi diffère-t-elle d'une intégration native ?

Les générations récentes d'équipements se connectent nativement à VistaSoft Monitor ; la Connect Box permet d'y raccorder les générations antérieures sans interface réseau.

## Sources publiques

| Document | URL publique |
|---|---|
| Page Connect Box | <https://www.duerrdental.com/en/solutions/networking/connect-box/> |
| Page VistaSoft Monitor solution | <https://www.duerrdental.com/en/solutions/networking/vistasoft-monitor/> |
| Portail aide VistaSoft Monitor | <https://help.vsmonitor.com/dd/www.duerrdental.com/en/vistasoftmonitor/> |
| App Store iOS | <https://apps.apple.com/in/app/vistasoft-monitor/id966166778> |
| Google Play Android | <https://play.google.com/store/apps/details?id=com.duerrdental.vistasoftmonitor> |

## Pour aller plus loin

- [VistaSoft Monitor — solution IoT cabinet](../vistasoft-monitor/overview/)
- [Index imagerie dentaire](../)
- [Index conventionnel (compresseurs et aspiration connectables)](/docs/fr/conventionnel/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-05-29. Licence : CC-BY 4.0.*
