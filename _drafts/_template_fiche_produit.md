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
  # Sources préférées (ordre) : pages OFFICIELLES des marques — Dürr Dental,
  # Air Techniques, orochemie (chimie), Mytronic — AVANT toute presse spécialisée.
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

<!-- JSON-LD : MedicalDevice (à adapter par produit). OBLIGATOIRE sur chaque fiche. -->
<!-- @type = MedicalDevice / SoftwareApplication / Product selon le cas. -->
<!-- mpn = code article Dürr (Manufacturer Part Number). À AJOUTER uniquement sur une fiche
     MONO-produit (un seul SKU représentatif). Fiche FAMILLE (plusieurs modèles) : OMETTRE mpn,
     lister les réfs dans la section "## Références produit et accessoires". -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalDevice",
  "name": "NOM PRODUIT",
  "mpn": "REF-ARTICLE-DURR",
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

<!--
SQUELETTE CANONIQUE (ordre des sections, aligné sur la pratique réelle du dépôt) :

  1. ## Description courte                  (toujours, 1ʳᵉ section)
  2. ## Statut réglementaire                (DM : classe MDR/MDD + CE)
  3. ## Caractéristiques techniques         (tableau sourcé ; réf. factsheet)
  4. [sections produit-spécifiques]         (adapter les titres au produit — voir liste ci-dessous)
  5. <script ... FAQPage> + ## Questions fréquentes   (4-6 Q/R sourcées)
  6. ## Références produit et accessoires    (codes article Dürr — voir modèle ci-dessous ; PRIX EXCLUS)
  7. ## Sources publiques                   (tableau Document | URL publique)
  8. ## Pour aller plus loin                 (liens internes)

Sections produit-spécifiques courantes (en choisir/adapter selon le cas, ne pas toutes forcer) :
  ## Technologies clés · ## Fonctions / Programmes · ## Modèles de la gamme ·
  ## Caractéristiques mécaniques et électriques · ## Intégration logicielle / écosystème ·
  ## Compatibilité VistaSoft Monitor · ## Place dans la chaîne d'hygiène ·
  ## Statut réglementaire et certifications · ## Limites et précisions

Règles transverses : répéter le NOM COMPLET du produit dans chaque section (chunking RAG) ;
chaque chiffre/affirmation sourcé ; verbatim entre guillemets quand cité.
-->

## Description courte

(Un paragraphe factuel. **Répéter le nom complet du produit.** Dire ce qu'est le
produit, sa catégorie et son usage principal. Pas de superlatif non quantifié.)

## Statut réglementaire

(Classe MDR EU 2017/745 / MDD 93/42/EEC + marquage CE, sourcé sur la Déclaration de
Conformité publique ou la page produit officielle. Pour un logiciel : préciser s'il
s'agit d'un dispositif médical logiciel et sa classe.)

## Caractéristiques techniques

(Tableau des caractéristiques, **chaque valeur sourcée** sur brochure / notice /
factsheet publique — citer la référence, ex. « factsheet P007XXXXXXL0X ».)

| Paramètre | Valeur |
|---|---|
| ... | ... |

<!-- Insérer ici les sections produit-spécifiques pertinentes (cf. liste du squelette). -->

<!-- Bloc FAQPage : 4 à 6 Q/R dérivées UNIQUEMENT des faits sourcés ci-dessus.
     Ne jamais inventer une réponse non présente dans la fiche. -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question 1 ?",
      "acceptedAnswer": { "@type": "Answer", "text": "Réponse factuelle et concise." }
    },
    {
      "@type": "Question",
      "name": "Question 2 ?",
      "acceptedAnswer": { "@type": "Answer", "text": "Réponse factuelle et concise." }
    }
  ]
}
</script>

## Questions fréquentes

### Question 1 ?

Réponse en 2-3 phrases concises et factuelles (mêmes faits que le bloc FAQPage ci-dessus).

### Question 2 ?

Réponse en 2-3 phrases concises et factuelles.

## Références produit et accessoires

<!-- Section pour toute fiche décrivant un produit MATÉRIEL ou CHIMIE ayant un code article
     Dürr public. À OMETTRE sur les fiches logiciel, guides de décision et fiches concept.
     RÈGLES : (1) réf + désignation + format UNIQUEMENT — JAMAIS de prix ni de nombre à
     virgule décimale façon tarif. (2) N'utiliser que des réfs vérifiables (identifiant public
     Dürr, résolvable page produit / distributeurs). (3) mpn (JSON-LD) = fiche mono-produit ;
     fiche famille = tableau seul. -->

Codes article **Dürr Dental** (identifiants publics, résolvables sur la page produit officielle
et les distributeurs agréés). **Prix exclus** — cette fiche ne reproduit aucun tarif.

| Réf (code Dürr) | Désignation | Format / note |
|---|---|---|
| `REF-APPAREIL` | NOM PRODUIT (appareil) | appareil |
| `REF-ACCESSOIRE` | Accessoire / consommable | format |

Source : codes article Dürr Dental (page produit officielle + catalogue matériel Dürr Dental
France, tarifs non repris).

## Sources publiques

Toutes les sources ci-dessous sont **publiques, accessibles sans authentification**.
Aucun document marqué *Internal Use* ou *Strictly Confidential* n'est mobilisé.
Sources préférées : pages **officielles** Dürr Dental / Air Techniques / orochemie / Mytronic.

| Document | URL publique | Référence |
|---|---|---|
| Page produit officielle (FR/France) | <https://www.duerrdental.com/fr/FR/produits/.../> | — |
| Notice d'installation / d'utilisation | <http://qr.duerrdental.com/CODE> | `CODE` |
| Brochure commerciale FR | — | `RÉFÉRENCE` |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> | — |

<!-- Bases réglementaires publiques si pertinent : Eudamed
     <https://ec.europa.eu/tools/eudamed/>, FDA 510(k)
     <https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm>. -->

<!-- Pérennité — déclencher un archivage Wayback des URLs sources :
     préfixer l'URL par https://web.archive.org/save/ -->

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
- [ ] Frontmatter complet (title, description, keywords, canonical_url, permalink, schema_type, breadcrumbs, source_documents, last_factual_review, license)
- [ ] JSON-LD MedicalDevice (ou autre type pertinent) présent en haut de page
- [ ] Section "## Questions fréquentes" (4-6 Q/R) + bloc JSON-LD FAQPage présents
- [ ] Section "## Références produit et accessoires" si produit matériel/chimie (réfs publiques, PRIX EXCLUS ; mpn JSON-LD si mono-produit)
- [ ] Squelette canonique respecté (Description courte → Statut réglementaire → specs → FAQ → Sources → Pour aller plus loin)
- [ ] Liens internes vers index parents fonctionnels
- [ ] CHANGELOG mis à jour
-->
