---
layout: default
title: "NOM PRODUIT — Vue d'ensemble"
description: "Description SEO de 150-250 caractères, en français, factuelle, qui mentionne le nom du produit, la catégorie et le statut réglementaire (ex. classe MDR)."
keywords: ["NomProduit", "Dürr Dental", "catégorie technique", "mot-clé métier", "termes de recherche pertinents"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/CATEGORIE/SOUS-DOSSIER/PAGE/
permalink: /docs/fr/CATEGORIE/SOUS-DOSSIER/PAGE/
schema_type: MedicalDevice         # ou SoftwareApplication / Product selon le cas
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "CATEGORIE"
    url: /docs/fr/CATEGORIE/
  - name: "NOM PRODUIT"
    url: /docs/fr/CATEGORIE/SOUS-DOSSIER/PAGE/
source_documents:
  # IMPORTANT : chaque source DOIT inclure une URL publique directe.
  # Si l'URL n'est pas connue, mentionner explicitement où la source est téléchargeable
  # (page produit, Centre de téléchargements) — JAMAIS un simple nom sans pointeur.
  - title: "Page produit officielle (FR/France)"
    url: "https://www.duerrdental.com/fr/FR/produits/<categorie>/<produit>/"
    type: "page produit"
    language: "fr"
  - title: "Notice d'installation <NOM PRODUIT>"
    url: "http://qr.duerrdental.com/<code>"
    type: "notice d'installation"
    reference: "<code Dürr>"
    language: "multi"
  - title: "Notice d'utilisation <NOM PRODUIT>"
    url: "http://qr.duerrdental.com/<code>"
    type: "notice d'utilisation"
    reference: "<code Dürr>"
    language: "multi"
  - title: "Brochure commerciale FR — <Titre>"
    reference: "<référence article>"
    type: "brochure commerciale"
    language: "fr"
    note: "Téléchargeable depuis la page produit FR ou via le Centre de téléchargements"
  - title: "Déclaration de Conformité <NOM PRODUIT>"
    type: "Déclaration de Conformité MDD/MDR"
    date: "AAAA-MM-JJ"
    note: "Notified Body, code, numéro de certificat"
  - title: "Centre de téléchargements Dürr Dental France"
    url: "https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/"
    type: "portail documents"
    language: "fr"
last_factual_review: AAAA-MM-JJ
license: CC-BY-4.0
---

<!-- JSON-LD : MedicalDevice (à adapter par produit) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalDevice",
  "name": "NOM PRODUIT",
  "alternateName": ["alias 1", "alias 2"],
  "category": "Catégorie technique en anglais (pour Schema)",
  "description": "Description courte du dispositif.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/CATEGORIE/SOUS-DOSSIER/PAGE/",
  "inLanguage": "fr",
  "manufacturer": {
    "@type": "Organization",
    "name": "Dürr Dental SE",
    "url": "https://www.duerrdental.com"
  },
  "regulatoryClass": "ex. Class IIb (EU MDR 2017/745 / MDD 93/42/EEC)",
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "CE marking", "value": "CE XXXX" },
    { "@type": "PropertyValue", "name": "Notified Body", "value": "..." }
  ]
}
</script>

# NOM PRODUIT — Vue d'ensemble

## Identification du dispositif

| Champ | Valeur |
|---|---|
| **Nom commercial** | NOM PRODUIT |
| **Catégorie** | ... |
| **Fabricant** | Dürr Dental SE — Höpfigheimer Straße 17, 74321 Bietigheim-Bissingen, Allemagne |
| **Distributeur France** | Dürr Dental France SARL — 71 rue des Hautes Pâtures, 92000 Nanterre |
| **Site officiel** | [duerrdental.com](https://www.duerrdental.com) — [duerrdental.com/fr](https://www.duerrdental.com/fr/) |
| **Statut réglementaire** | ... |
| **Référence brochure FR** | ... |

## Statut réglementaire et certifications

(Tableau / verbatim sourcé sur DoC publique. Verbatim entre guillemets quand cité.)

## Technologie (capteur, mécanique, logiciel selon le produit)

(Tableau des caractéristiques techniques, sourcé sur brochure publique ou notice publique.)

## Programmes / fonctionnalités

(Liste structurée, regroupée par catégorie.)

## Caractéristiques mécaniques et électriques

(Tableau complet.)

## Intégration logicielle / écosystème

(Mention factuelle des intégrations VistaSoft / standards DICOM / TWAIN / etc. selon le cas. Pas de comparaison.)

## Limites et précisions

(Verbatim limites officielles du manuel. Mention non-remboursement organismes santé France si applicable.)

## Questions fréquentes

### Question 1 ?

Réponse en 2-3 phrases concises et factuelles.

### Question 2 ?

Réponse en 2-3 phrases concises et factuelles.

<!-- Une fois 4-6 Q&A rédigées, ajouter le bloc JSON-LD FAQPage en haut de page (ou ici en bas). -->

## Sources publiques

Toutes les sources ci-dessous sont **publiques, accessibles sans authentification**.
Aucun document marqué *Internal Use* ou *Strictly Confidential* n'est mobilisé.

### Pages officielles Dürr Dental

| Document | URL publique | Référence |
|---|---|---|
| Page produit officielle (FR/France) | <https://www.duerrdental.com/fr/FR/produits/.../> | — |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> | — |

### Notices publiques (qr.duerrdental.com)

| Document | URL publique | Référence Dürr |
|---|---|---|
| Notice d'installation | <http://qr.duerrdental.com/CODE> | `CODE` |
| Notice d'utilisation | <http://qr.duerrdental.com/CODE> | `CODE` |

### Brochure commerciale

| Document | Référence | Langue | Origine |
|---|---|---|---|
| *Titre brochure* | `RÉFÉRENCE` | Français | Téléchargeable depuis la page produit FR. |

### Conformité réglementaire

| Élément | Valeur |
|---|---|
| Déclaration de Conformité | Date, signataire |
| Notified Body | Nom, code |
| Numéro de certificat | ... |
| Réglementation | MDR EU 2017/745 / MDD 93/42/EEC, classe X |

### Bases réglementaires publiques

| Base | URL |
|---|---|
| Eudamed | <https://ec.europa.eu/tools/eudamed/> |
| FDA 510(k) | <https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm> |

### Pérennité — archive Wayback Machine

- Page produit archivée : <https://web.archive.org/web/2026*/duerrdental.com/fr/FR/.../>
- Notices archivées : <https://web.archive.org/web/2026*/qr.duerrdental.com/CODE>

*Pour déclencher un nouvel archivage : préfixer l'URL par `https://web.archive.org/save/`.*

## Pour aller plus loin

- [Index CATEGORIE](../)
- [Documentation française](../../)
- [Glossaire](../../glossaire/)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative personnelle,
non officielle. Dernière revue factuelle : AAAA-MM-JJ. Licence : CC-BY 4.0.*

<!--
CHECKLIST AVANT COMMIT :
- [ ] Aucun nom de marque concurrente cité (règle d'or Dürr)
- [ ] Aucun tableau / formulation comparative
- [ ] Aucun superlatif non quantifié
- [ ] Aucune mention "Strictly Confidential" / "Internal Use"
- [ ] Aucune donnée patient / praticien / cabinet identifiable
- [ ] Chaque chiffre / spec est sourcé (brochure, manuel, DoC publique)
- [ ] Frontmatter complet (title, description, keywords, canonical_url, permalink, schema_type, breadcrumbs, source_documents, last_factual_review)
- [ ] JSON-LD MedicalDevice (ou autre type pertinent) adapté
- [ ] FAQ rédigée + JSON-LD FAQPage ajouté si applicable
- [ ] Liens internes vers index parents fonctionnels
- [ ] CHANGELOG mis à jour
-->
