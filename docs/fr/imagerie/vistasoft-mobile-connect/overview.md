---
layout: default
title: "VistaSoft Mobile Connect — Consultation mobile sur iPad"
description: "VistaSoft Mobile Connect est le module Dürr Dental qui permet la consultation mobile des images dentaires (radiographies et caméras) sur iPad via l'application 'DÜRR DENTAL Imaging'. Compatible VistaSoft 2.0+ et DBSWin 5.4+."
keywords: ["VistaSoft Mobile Connect", "VistaSoft MobileConnect", "Dürr Dental Imaging App", "consultation iPad", "imagerie dentaire mobile", "iPadOS"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-mobile-connect/overview/
permalink: /docs/fr/imagerie/vistasoft-mobile-connect/overview/
schema_type: SoftwareApplication
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "VistaSoft Mobile Connect"
    url: /docs/fr/imagerie/vistasoft-mobile-connect/overview/
source_documents:
  - title: "Application iPad — DÜRR DENTAL Imaging (App Store)"
    url: "https://apps.apple.com/de/app/duerr-dental-imaging/id460076346"
    type: "application mobile officielle"
    reference: "App Store ID 460076346"
    language: "multi"
  - title: "Page VistaSoft (socle EN)"
    url: "https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/"
    type: "page produit"
    language: "en"
  - title: "Page VistaSoft Imaging interfaces (EN)"
    url: "https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/"
    type: "page produit"
    language: "en"
  - title: "Manuel utilisateur VistaSoft 4.0 (mentions Mobile Connect)"
    url: "http://qr.duerrdental.com/2110100001"
    type: "manuel utilisateur"
    reference: "2110100001"
    language: "multi"
  - title: "Brochure VistaPano S 2.0 — mention iPad / Imaging App / Mobile Connect"
    reference: "P007-772/03-T01"
    type: "brochure commerciale"
    language: "fr"
    note: "Téléchargeable depuis la page produit VistaPano S 2.0 (FR)"
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
  "@type": ["MobileApplication", "Product"],
  "name": "DÜRR DENTAL Imaging",
  "alternateName": ["VistaSoft Mobile Connect", "VistaSoft MobileConnect", "Dürr Dental Imaging App"],
  "applicationCategory": "MedicalApplication",
  "applicationSubCategory": "Mobile dental image consultation",
  "description": "Application iPad pour la consultation mobile des images dentaires (radiographies et caméras) gérées par VistaSoft ou DBSWin. Composant client mobile du système VistaSoft Mobile Connect.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-mobile-connect/overview/",
  "downloadUrl": "https://apps.apple.com/de/app/duerr-dental-imaging/id460076346",
  "operatingSystem": "iPadOS 13.0+",
  "inLanguage": "fr",
  "publisher": {
    "@type": "Organization",
    "name": "Dürr Dental SE",
    "url": "https://www.duerrdental.com"
  },
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "App Store identifier", "value": "id460076346" },
    { "@type": "PropertyValue", "name": "Required server software (option 1)", "value": "VistaSoft 2.0 or higher + Dürr Dental MobileConnect" },
    { "@type": "PropertyValue", "name": "Required server software (option 2)", "value": "DBSWin 5.4 or higher + Dürr Dental MobileConnect" },
    { "@type": "PropertyValue", "name": "Offline mode", "value": "Supported (offline database)" }
  ]
}
</script>

# VistaSoft Mobile Connect — Consultation mobile sur iPad

## Description courte

**VistaSoft Mobile Connect** est le module Dürr Dental qui permet la
**consultation mobile** des images dentaires (radiographies et clichés
caméras) gérées par VistaSoft ou DBSWin, depuis un **iPad** du cabinet ou
au fauteuil. Le composant client est l'application **« DÜRR DENTAL
Imaging »** publiée sur l'App Store officiel.

L'application est mentionnée dans la brochure publique VistaPano S 2.0
(réf. P007-772/03-T01) : *« Grâce à VistaSoft MobileConnect et l'Imaging
App en option, les données d'images sont consultables à tout moment sur
l'iPad »*.

## Identification du module

| Champ | Valeur |
|---|---|
| Nom commercial (côté serveur) | VistaSoft Mobile Connect (anciennement VistaSoft MobileConnect) |
| Nom commercial (côté iPad) | DÜRR DENTAL Imaging |
| Catégorie | Consultation mobile d'images dentaires |
| Éditeur | Dürr Dental SE — Bietigheim-Bissingen, Allemagne |
| Plateforme client | **iPad uniquement** (iPadOS 13.0+) |
| App Store officiel | <https://apps.apple.com/de/app/duerr-dental-imaging/id460076346> |
| Identifiant App Store | `id460076346` |

## Architecture

Le système Mobile Connect repose sur deux composants distincts :

| Composant | Rôle | Localisation |
|---|---|---|
| **VistaSoft Mobile Connect** (module serveur) | Expose les images du logiciel principal à l'iPad via un protocole sécurisé | Installé sur le poste / serveur où tourne VistaSoft ou DBSWin |
| **DÜRR DENTAL Imaging** (app iPad) | Interface mobile de consultation et d'envoi de tâches | Téléchargée depuis l'App Store sur l'iPad |

Le module serveur doit être **installé séparément** ; l'application iPad
seule ne suffit pas. Le couplage entre les deux est ce qui permet à
l'iPad d'accéder aux dossiers patients du cabinet.

## Prérequis logiciels

L'application **DÜRR DENTAL Imaging** est compatible avec deux écosystèmes
serveur Dürr Dental :

| Logiciel serveur requis | Version minimale | Complément obligatoire |
|---|---|---|
| VistaSoft | **2.0** et supérieures | Module Dürr Dental MobileConnect installé |
| DBSWin | **5.4** et supérieures | Module Dürr Dental MobileConnect installé |

La version **VistaSoft 4.0** est pleinement supportée.

## Fonctionnalités

Selon les pages produit officielles et la description de l'application sur
l'App Store, l'application iPad permet :

- **Sélection patient** dans le carnet de cabinet.
- **Visualisation des clichés radiographiques** et des images caméra du
  patient.
- **Envoi de tâches d'acquisition** depuis l'iPad vers VistaSoft (tâche
  panoramique, intra-orale, etc.) — fonction conditionnée à VistaSoft.
- **Visualisation des layouts et groupes d'images** — fonction conditionnée
  à DBSWin.
- **Annotations à main levée** (freehand drawing) sur les images affichées.
- **Base de démonstration** intégrée avec des images d'exemple.
- **Base hors-ligne** : fonctionnement même sans connexion serveur active,
  utile au fauteuil ou en déplacement.

## Cas d'usage typiques

1. **Présentation du plan de traitement au patient** : consultation des
   clichés sur iPad au fauteuil, ce qui facilite l'explication
   pédagogique au patient (visualisation à hauteur d'oeil).
2. **Mobilité au sein du cabinet** : consultation des images depuis
   n'importe quelle salle, sans poste fixe dédié.
3. **Préparation d'examen** : déclenchement d'une tâche d'acquisition
   depuis l'iPad pour la modalité concernée (panoramique, intra-orale).
4. **Démonstration / formation** : utilisation de la base démo intégrée
   pour montrer les fonctions sans toucher aux dossiers patients réels.

## Limites et précisions

- L'application **DÜRR DENTAL Imaging est limitée à iPadOS** (Apple iPad).
  Aucune version Android n'est documentée publiquement par Dürr Dental.
- Le fonctionnement complet **suppose l'installation du module serveur**
  Dürr Dental MobileConnect côté VistaSoft ou DBSWin — sans ce composant,
  l'application iPad reste limitée à la base de démonstration.
- VistaSoft Mobile Connect **n'est pas un dispositif médical** de
  diagnostic primaire ; il s'agit d'un outil de consultation et de
  présentation au patient. Le diagnostic radiologique reste posé via le
  logiciel principal VistaSoft 4.0 (DM IIb).
- L'**envoi de tâches d'acquisition** depuis l'iPad nécessite VistaSoft
  côté serveur ; la fonctionnalité n'est pas disponible avec DBSWin.

## Articulation avec les autres modules

- [VistaSoft 4.0](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/) — logiciel socle d'imagerie
  diagnostique côté serveur.
- [VistaSoft Cloud View](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-cloud-view/overview/) — alternative
  pour la consultation des images dans le navigateur Web (sans application
  native, multi-plateforme), notamment hors du cabinet.
- [Patient Bridge](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/) — interface qui assure la
  cohérence des fiches patients entre VistaSoft et le PMS du cabinet.

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Sur quelle plateforme fonctionne VistaSoft Mobile Connect ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "L'application DÜRR DENTAL Imaging, qui constitue le composant client de VistaSoft Mobile Connect, fonctionne uniquement sur iPad (iPadOS 13.0 et supérieur). Elle est téléchargeable sur l'App Store officiel Apple."
      }
    },
    {
      "@type": "Question",
      "name": "Quels sont les prérequis logiciels côté serveur ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Côté serveur, deux options sont supportées : VistaSoft 2.0 ou supérieur, ou DBSWin 5.4 ou supérieur. Dans les deux cas, le module Dürr Dental MobileConnect doit également être installé sur le poste serveur."
      }
    },
    {
      "@type": "Question",
      "name": "VistaSoft Mobile Connect est-il un dispositif médical ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. VistaSoft Mobile Connect est un outil de consultation et de présentation au patient. Le diagnostic radiologique primaire reste posé via le logiciel socle VistaSoft 4.0 (dispositif médical de classe IIb)."
      }
    },
    {
      "@type": "Question",
      "name": "L'application fonctionne-t-elle hors-ligne ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. L'application DÜRR DENTAL Imaging intègre une base hors-ligne qui permet de fonctionner même sans connexion active au serveur du cabinet — utile au fauteuil ou en déplacement."
      }
    },
    {
      "@type": "Question",
      "name": "Peut-on envoyer une tâche d'acquisition depuis l'iPad ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui, à condition que le serveur soit équipé de VistaSoft (et non de DBSWin). L'application iPad permet alors d'envoyer directement à VistaSoft une demande d'acquisition pour la modalité concernée (panoramique, intra-orale, etc.)."
      }
    }
  ]
}
</script>

### Sur quelle plateforme ?

**iPad uniquement** (iPadOS 13.0+). Pas de version Android publique.

### Prérequis serveur ?

VistaSoft **2.0+** ou DBSWin **5.4+**, avec le module **Dürr Dental
MobileConnect** installé.

### Dispositif médical ?

**Non**. Outil de consultation. Diagnostic radiologique primaire reste sur
[VistaSoft 4.0 (DM IIb)](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/).

### Fonctionne hors-ligne ?

Oui — base hors-ligne intégrée.

### Envoi de tâche d'acquisition depuis l'iPad ?

Oui avec VistaSoft (pas avec DBSWin).

## Sources publiques

### App Store officiel

| Document | URL publique |
|---|---|
| Application DÜRR DENTAL Imaging (App Store, ID 460076346) | <https://apps.apple.com/de/app/duerr-dental-imaging/id460076346> |

### Pages officielles Dürr Dental

| Document | URL publique |
|---|---|
| Page VistaSoft (socle) | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/> |
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |
| Manuel VistaSoft 4.0 | <http://qr.duerrdental.com/2110100001> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

### Brochure publique mentionnant Mobile Connect

| Document | Référence |
|---|---|
| Brochure FR VistaPano S 2.0 / Ceph 2.0 (mention iPad + Imaging App + MobileConnect) | `P007-772/03-T01` — téléchargeable depuis la [page produit VistaPano S 2.0](/durr-dental-knowledge-base/docs/fr/imagerie/vistapano-2-0/overview/) |

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Page App Store | <https://web.archive.org/web/2026*/apps.apple.com/de/app/duerr-dental-imaging/id460076346> |
| Page VistaSoft interfaces | <https://web.archive.org/web/2026*/duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique (socle serveur)](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/)
- [VistaSoft Cloud View — consultation navigateur Web](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-cloud-view/overview/)
- [Patient Bridge — interface PMS](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental (page produit, App Store, brochure publique). Mainteneur : salarié de
Dürr Dental France (CDI déclaré) — initiative personnelle, non officielle. Dernière
revue factuelle : 2026-07-19. Licence : CC-BY 4.0.*
