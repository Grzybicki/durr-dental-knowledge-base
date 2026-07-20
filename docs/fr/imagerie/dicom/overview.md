---
layout: default
title: "DICOM dans VistaSoft 4.0 — Conformance Statement, Modality Worklist, Storage, Print"
description: "Vue d'ensemble des services DICOM supportés par VistaSoft 4.0 de Dürr Dental : DICOM Conformance Statement, Modality Worklist (MWL), DICOM Storage, DICOM Print. Conforme au standard DICOM PS3."
keywords: ["DICOM Conformance Statement", "VistaSoft 4.0", "Dürr Dental", "DICOM Modality Worklist", "DICOM Storage", "DICOM Print", "imagerie médicale standard", "SOP Class"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/
permalink: /docs/fr/imagerie/dicom/overview/
schema_type: TechArticle
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "DICOM dans VistaSoft 4.0"
    url: /docs/fr/imagerie/dicom/overview/
source_documents:
  - title: "Manuel utilisateur VistaSoft 4.0 (sections DICOM)"
    url: "http://qr.duerrdental.com/2110100001"
    type: "manuel utilisateur"
    reference: "2110100001"
    language: "multi"
  - title: "Page VistaSoft Imaging interfaces (EN)"
    url: "https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/"
    type: "page produit"
    language: "en"
  - title: "DICOM Conformance Statement VistaSoft 4.0"
    type: "document technique constructeur"
    note: "Document de conformance DICOM publié par Dürr Dental — récupérable via le Centre de téléchargements Dürr Dental France. Description complète des SOP Classes, Transfer Syntaxes et services réseau supportés."
  - title: "Standard DICOM officiel (NEMA / DICOM Standards Committee)"
    url: "https://www.dicomstandard.org/"
    type: "standard international"
    language: "en"
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
  "name": "DICOM dans VistaSoft 4.0 — Conformance Statement et services",
  "description": "Document de référence sur les services DICOM (Conformance Statement, Modality Worklist, Storage, Print) supportés par VistaSoft 4.0 de Dürr Dental.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/dicom/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" },
  "about": {
    "@type": "Thing",
    "name": "DICOM (Digital Imaging and Communications in Medicine)",
    "url": "https://www.dicomstandard.org/"
  }
}
</script>

# DICOM dans VistaSoft 4.0

## Description courte

**VistaSoft 4.0** implémente le standard **DICOM** (Digital Imaging and
Communications in Medicine) pour l'interopérabilité avec les systèmes
d'imagerie médicale. Le logiciel supporte plusieurs services DICOM clés :
**Modality Worklist (MWL)** pour la réception des ordres d'examen, **DICOM
Storage** pour la transmission des images, et **DICOM Print** dans certaines
configurations.

Le document technique de référence est le **DICOM Conformance Statement
VistaSoft** publié par Dürr Dental, récupérable via le [Centre de
téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/).

## Qu'est-ce qu'un DICOM Conformance Statement ?

Un **DICOM Conformance Statement** est un document technique normalisé que
chaque éditeur de dispositif ou logiciel revendiquant la conformité DICOM
doit publier. Il décrit en détail :

- Les **SOP Classes** supportées (Service-Object Pair Classes — définissent
  les opérations possibles : C-STORE, C-FIND, N-CREATE, etc.).
- Les **Transfer Syntaxes** supportées (encodages des données).
- Les services réseau implémentés (associations DIMSE, attributs réseau).
- Les rôles SCP (Service Class Provider) et SCU (Service Class User) du
  logiciel pour chaque SOP Class.
- Les conformances de protocole et les éventuelles extensions propriétaires.

Cette publication permet à un autre dispositif DICOM d'évaluer **avant
intégration** s'il peut communiquer avec VistaSoft pour un cas d'usage donné.

## Services DICOM supportés par VistaSoft 4.0

### DICOM Modality Worklist (MWL)

VistaSoft 4.0 supporte la **Modality Worklist** en tant que **SCU**. Cela
permet à VistaSoft de **recevoir les ordres d'examen** depuis un système
RIS / PMS conforme DICOM avant l'acquisition. Bénéfice : pas de re-saisie
de la fiche patient au moment de l'examen.

### DICOM Storage

VistaSoft 4.0 supporte les services **DICOM Storage** en tant que **SCU**
(envoi) et selon configuration en tant que **SCP** (réception). Cela permet
à VistaSoft :

- D'**envoyer** les images acquises (panoramique, CBCT, intra-oral, etc.)
  vers un PACS conforme DICOM ;
- Selon configuration, de **recevoir** des images depuis un autre dispositif
  DICOM (consultation d'examens externes).

### DICOM Print (selon configuration)

Selon la configuration et la version, VistaSoft 4.0 peut supporter le service
**DICOM Print** pour l'impression d'images sur des imprimantes DICOM (films,
papier photo). Le détail des SOP Classes Print effectivement supportées
figure dans le DICOM Conformance Statement officiel.

### Autres services DICOM courants

Selon la version du DICOM Conformance Statement, VistaSoft peut supporter
d'autres services tels que **Modality Performed Procedure Step (MPPS)**,
**Storage Commitment**, ou la prise en charge d'images 3D (CBCT) au format
DICOM Volume / Multi-Frame. Pour la liste exacte et à jour, **se référer au
DICOM Conformance Statement officiel**.

## Modalités supportées

VistaSoft 4.0 gère les modalités d'imagerie dentaire suivantes au format
DICOM :

| Modalité DICOM | Périmètre |
|---|---|
| **IO** | Image intra-orale |
| **PX** | Panoramique X-Ray |
| **CR** | Computed Radiography (scanner de plaques au phosphore) |
| **DX** | Digital X-Ray |
| **CT** | Cone Beam CT (CBCT) |
| **OT** | Other (caméras intraorales, vidéo) |

Le DICOM Conformance Statement officiel VistaSoft (ProFile `4492706`) distingue
**deux jeux de SOP Classes** — il ne faut pas les confondre :

**À l'import** (lecture de fichiers / DICOMDIR, rôle *File-Set Reader*), VistaSoft
accepte un **large éventail** de SOP Classes :

| SOP Class (import) | UID |
|---|---|
| Computed Radiography Image Storage | `1.2.840.10008.5.1.4.1.1.1` |
| Digital X-Ray Image Storage — For Presentation / For Processing | `…1.1.1.1` / `…1.1.1.1.1` |
| Digital Intra-Oral X-Ray Image Storage — For Presentation / For Processing | `…1.1.1.3` / `…1.1.1.3.1` |
| CT / Enhanced CT Image Storage | `…1.1.2` / `…1.1.2.1` |
| Secondary Capture Image Storage | `1.2.840.10008.5.1.4.1.1.7` |

**En gestion interne et à l'envoi vers un PACS** (rôle *Storage SCU*), VistaSoft
**mappe** ses images vers un jeu **restreint** (table « Mapping of VistaSoft image
types to SOP Classes ») :

| Type d'image VistaSoft | SOP Class émise |
|---|---|
| Rétro-alvéolaire / panoramique / céphalométrique | **Computed Radiography Image Storage** |
| CBCT | **Enhanced CT / CT Image Storage** |
| Photos / vidéo / proof | **Secondary Capture Image Storage** |

L'attribut **Modality** (0008,0060) vaut alors **IO** (rétro-alvéolaire), **PX**
(panoramique), **DX** (céphalométrique) ou **CT** (CBCT). VistaSoft agit en
**Storage SCU uniquement** (il envoie vers un PACS mais n'accepte pas d'associations
entrantes ; la réception d'images externes se fait par **import de fichiers**).

## Articulation avec le standard officiel

Le standard DICOM officiel est publié par le **DICOM Standards Committee**
hébergé par NEMA : [dicomstandard.org](https://www.dicomstandard.org/). Le
DICOM Conformance Statement VistaSoft décrit la conformité à la révision
**PS3** du standard.

Toute interrogation sur la conformité DICOM de VistaSoft pour un cas d'usage
donné doit s'appuyer sur :

1. Le DICOM Conformance Statement VistaSoft (document Dürr Dental).
2. Le DICOM Conformance Statement du dispositif partenaire (PACS, RIS, etc.).
3. La compatibilité croisée des SOP Classes et Transfer Syntaxes.

## Récupération du DICOM Conformance Statement VistaSoft

Le document n'est pas exposé en URL directe sur duerrdental.com. Pour le
récupérer :

1. Accéder au [Centre de téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/).
2. Rechercher « DICOM Conformance Statement » et « VistaSoft ».
3. Télécharger la version correspondant à la version installée de VistaSoft.

À défaut, contacter le service technique Dürr Dental France pour
récupération directe.

## Limites et précisions

- La conformité DICOM **dépend de la version VistaSoft** installée — toujours
  se référer à la version du Conformance Statement correspondant à la
  version logicielle déployée.
- Certains services DICOM peuvent nécessiter une **configuration spécifique**
  ou une **licence complémentaire**.
- La **compatibilité bidirectionnelle** avec un PACS ou RIS dépend autant
  de la conformité de VistaSoft que de celle du système partenaire.

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Qu'est-ce qu'un DICOM Conformance Statement ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Un DICOM Conformance Statement est un document technique normalisé publié par chaque éditeur revendiquant la conformité DICOM. Il décrit en détail les SOP Classes supportées, les Transfer Syntaxes, les services réseau implémentés, et les rôles SCP/SCU du logiciel pour chaque service."
      }
    },
    {
      "@type": "Question",
      "name": "Quels services DICOM VistaSoft 4.0 supporte-t-il ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft 4.0 supporte au minimum DICOM Modality Worklist (réception des ordres d'examen), DICOM Storage (envoi et selon configuration réception des images), et selon configuration DICOM Print. La liste exhaustive figure dans le DICOM Conformance Statement officiel publié par Dürr Dental."
      }
    },
    {
      "@type": "Question",
      "name": "Où trouver le DICOM Conformance Statement VistaSoft ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Le DICOM Conformance Statement VistaSoft est récupérable via le Centre de téléchargements Dürr Dental France (duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/) en recherchant « DICOM Conformance Statement » et la version VistaSoft installée."
      }
    },
    {
      "@type": "Question",
      "name": "VistaSoft est-il compatible avec n'importe quel PACS ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft est compatible avec les systèmes conformes DICOM PS3. La compatibilité effective dépend de la couverture croisée des SOP Classes et Transfer Syntaxes entre VistaSoft et le PACS partenaire — à vérifier en croisant les deux DICOM Conformance Statements."
      }
    }
  ]
}
</script>

### Qu'est-ce qu'un DICOM Conformance Statement ?

Document technique normalisé décrivant les **SOP Classes**, **Transfer
Syntaxes**, **services réseau** et **rôles SCP/SCU** d'un logiciel ou
dispositif DICOM.

### Quels services DICOM VistaSoft 4.0 supporte-t-il ?

Au minimum : **Modality Worklist**, **Storage**, et selon configuration
**DICOM Print**. Détail dans le Conformance Statement officiel.

### Où trouver le Conformance Statement ?

[Centre de téléchargements Dürr Dental France](https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/),
recherche « DICOM Conformance Statement ».

### Compatible avec n'importe quel PACS ?

Avec les systèmes conformes **DICOM PS3**. Vérifier les SOP Classes et
Transfer Syntaxes croisées.

## Sources publiques

| Document | URL publique |
|---|---|
| Manuel VistaSoft 4.0 (sections DICOM) | <http://qr.duerrdental.com/2110100001> |
| Page VistaSoft Imaging interfaces | <https://www.duerrdental.com/en/products/software/learning-and-integration-solutions/interfaces/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |
| Standard DICOM officiel (NEMA) | <https://www.dicomstandard.org/> |

### Pérennité — archive Wayback Machine

| Source | URL Wayback |
|---|---|
| Manuel VistaSoft 4.0 | <https://web.archive.org/web/2026*/qr.duerrdental.com/2110100001> |
| Page DICOM standard | <https://web.archive.org/web/2026*/dicomstandard.org/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/)
- [Patient Bridge — interface PMS](/durr-dental-knowledge-base/docs/fr/imagerie/patient-bridge/overview/)
- [Standards VDDS-media et BDW](/durr-dental-knowledge-base/docs/fr/imagerie/vdds-bdw/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)
- [Glossaire — entrée DICOM](/durr-dental-knowledge-base/docs/fr/glossaire/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental et le standard DICOM. Mainteneur : salarié de Dürr Dental France
(CDI déclaré) — initiative personnelle, non officielle. Dernière revue factuelle :
2026-05-28. Licence : CC-BY 4.0.*
