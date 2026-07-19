---
layout: default
title: "VistaSoft Inspect — Contrôle qualité radiographique (DIN 6868-157)"
description: "VistaSoft Inspect est le module Dürr Dental de contrôle qualité radiographique. Couvre les contrôles d'acceptation, de constance et la surveillance des moniteurs selon la norme DIN 6868-157."
keywords: ["VistaSoft Inspect", "Dürr Dental", "contrôle qualité radiographique", "DIN 6868-157", "contrôle d'acceptation", "contrôle de constance", "phantom radiographique"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-inspect/overview/
permalink: /docs/fr/imagerie/vistasoft-inspect/overview/
schema_type: SoftwareApplication
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "VistaSoft Inspect"
    url: /docs/fr/imagerie/vistasoft-inspect/overview/
source_documents:
  - title: "Manuel VistaSoft 4.0 (sections 56-63 — VistaSoft Inspect)"
    url: "http://qr.duerrdental.com/2110100001"
    type: "manuel utilisateur"
    reference: "2110100001"
    language: "multi"
  - title: "Page VistaSoft Imaging (EN)"
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
  "name": "VistaSoft Inspect",
  "alternateName": ["Dürr Dental VistaSoft Inspect"],
  "applicationCategory": "MedicalImagingSoftware",
  "applicationSubCategory": "Radiographic quality control",
  "description": "Module Dürr Dental de contrôle qualité radiographique selon la norme allemande DIN 6868-157. Couvre les contrôles d'acceptation, de constance et la surveillance des moniteurs.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-inspect/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" },
  "softwareRequirements": "VistaSoft 4.0+",
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "Standard", "value": "DIN 6868-157" },
    { "@type": "PropertyValue", "name": "Coverage", "value": "Acceptance test, constancy test, monitor quality control" }
  ]
}
</script>

# VistaSoft Inspect — Contrôle qualité radiographique

## Description courte

**VistaSoft Inspect** est le module Dürr Dental de **contrôle qualité
radiographique** intégré à VistaSoft 4.0. Il couvre les **contrôles
d'acceptation**, les **contrôles de constance** et la **surveillance des
moniteurs** d'affichage selon la norme allemande **DIN 6868-157**.

Le module est documenté dans le manuel utilisateur VistaSoft 4.0
([`qr.duerrdental.com/2110100001`](http://qr.duerrdental.com/2110100001),
sections 56-63).

## Identification du module

| Champ | Valeur |
|---|---|
| Nom commercial | VistaSoft Inspect |
| Catégorie | Contrôle qualité radiographique |
| Éditeur | Dürr Dental SE — Bietigheim-Bissingen, Allemagne |
| Prérequis logiciel | VistaSoft 4.0 et supérieur |
| Norme de référence | **DIN 6868-157** |
| Documentation | Manuel VistaSoft §56-63 |

## DIN 6868-157 — la norme de référence

**DIN 6868-157** est la norme allemande qui définit les **exigences de
contrôle qualité** pour les dispositifs d'imagerie radiographique en
contexte médical et dentaire. Elle couvre :

- Le **contrôle d'acceptation** (Abnahmeprüfung) effectué à la mise en
  service d'un nouvel appareil.
- Le **contrôle de constance** (Konstanzprüfung) effectué périodiquement
  pour s'assurer du maintien des performances.
- Les **contrôles de moniteur** (Bildwiedergabesystem) pour les écrans de
  diagnostic radiologique.

## Périmètre fonctionnel de VistaSoft Inspect

### Contrôle d'acceptation (Abnahmeprüfung)

VistaSoft Inspect guide le technicien dans la réalisation du contrôle
d'acceptation à la mise en service d'un nouvel appareil radiographique
Dürr Dental. Les paramètres mesurés et les seuils d'acceptation sont
conformes à DIN 6868-157.

### Contrôle de constance (Konstanzprüfung)

VistaSoft Inspect organise les **contrôles périodiques** réguliers (en
général mensuels ou trimestriels selon le type d'appareil et la
réglementation locale) pour vérifier que les performances de l'appareil
n'ont pas dérivé.

### Surveillance des moniteurs

VistaSoft Inspect prend également en charge la **vérification qualité des
moniteurs** utilisés pour le diagnostic radiologique :

- Test de luminance.
- Test de calibrage.
- Test d'uniformité.
- Vérification des seuils de conformité DIN 6868-157.

### Archivage des contrôles

Les résultats des contrôles sont **archivés et horodatés** dans la base
VistaSoft, permettant la traçabilité complète des opérations de contrôle
qualité et la production de rapports pour les autorités de
radioprotection.

## Articulation avec la réglementation française

En France, le contrôle qualité des dispositifs d'imagerie radiographique
relève de la **réglementation de radioprotection** (Code de la santé
publique, IRSN, ASN). Bien que la norme française de contrôle qualité
diffère de DIN 6868-157 dans le détail, la **méthode et les paramètres
mesurés** sont largement comparables.

Pour les cabinets français, l'utilisation de VistaSoft Inspect peut
servir de **base technique** pour les contrôles qualité, en adaptant les
seuils aux exigences françaises spécifiques. La conformité aux exigences
réglementaires françaises reste **de la responsabilité du cabinet** et de
son personnel compétent en radioprotection (PCR).

## Limites et précisions

- VistaSoft Inspect implémente **la norme DIN 6868-157** ; les exigences
  réglementaires françaises ou d'autres pays peuvent nécessiter des
  contrôles complémentaires.
- L'utilisation du module **suppose la disponibilité des phantoms**
  appropriés (corps d'épreuve standardisés) pour réaliser les tests.
- L'**interprétation des résultats** et la prise de décision en cas
  d'écart aux seuils restent de la responsabilité du personnel compétent.

## Articulation avec d'autres modules

- [VistaSoft 4.0](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/) — socle logiciel.
- [VistaPano S 2.0 / Ceph 2.0](/durr-dental-knowledge-base/docs/fr/imagerie/vistapano-2-0/overview/) — exemple
  d'appareil concerné par les contrôles d'acceptation et de constance.

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "À quoi sert VistaSoft Inspect ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft Inspect est le module de contrôle qualité radiographique intégré à VistaSoft 4.0. Il couvre les contrôles d'acceptation, les contrôles de constance et la surveillance des moniteurs selon la norme allemande DIN 6868-157."
      }
    },
    {
      "@type": "Question",
      "name": "Quelle norme implémente VistaSoft Inspect ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft Inspect implémente la norme allemande DIN 6868-157, qui définit les exigences de contrôle qualité pour les dispositifs d'imagerie radiographique médicale et dentaire."
      }
    },
    {
      "@type": "Question",
      "name": "VistaSoft Inspect est-il adapté à la réglementation française ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "VistaSoft Inspect implémente DIN 6868-157 ; les exigences réglementaires françaises de radioprotection (Code de la santé publique, IRSN, ASN) sont largement comparables sur la méthode et les paramètres mesurés. La conformité aux exigences françaises reste de la responsabilité du cabinet et de son PCR (personne compétente en radioprotection)."
      }
    }
  ]
}
</script>

### À quoi sert VistaSoft Inspect ?

Contrôle qualité radiographique : **acceptation + constance + moniteurs**
selon **DIN 6868-157**.

### Quelle norme ?

**DIN 6868-157** (Allemagne).

### Adapté à la France ?

DIN 6868-157 est largement comparable aux exigences françaises sur la
méthode. Conformité réglementaire FR reste responsabilité du cabinet et
de son PCR.

## Sources publiques

| Document | URL publique |
|---|---|
| Manuel VistaSoft 4.0 (sections 56-63) | <http://qr.duerrdental.com/2110100001> |
| Page VistaSoft Imaging | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/> |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel d'imagerie diagnostique (socle)](/durr-dental-knowledge-base/docs/fr/imagerie/vistasoft-4-0/overview/)
- [VistaPano S 2.0 / Ceph 2.0 — appareil concerné par les contrôles qualité](/durr-dental-knowledge-base/docs/fr/imagerie/vistapano-2-0/overview/)
- [Index imagerie dentaire](/durr-dental-knowledge-base/docs/fr/imagerie/)
- [Glossaire — entrée DIN 6868-157](/durr-dental-knowledge-base/docs/fr/glossaire/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-07-19. Licence : CC-BY 4.0.*
