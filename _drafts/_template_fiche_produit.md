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
  - "Brochure publique <réf>, Dürr Dental France"
  - "Manuel utilisateur <réf URL qr.duerrdental.com>"
  - "Déclaration de Conformité publique du <date>"
  - "Page produit publique duerrdental.com/fr/produits/..."
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

- **Brochure FR officielle** : référence article, éditeur.
- **Déclaration de Conformité publique** : date, certification.
- **Page produit publique** : URL.
- **Base Eudamed** : URL.

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
