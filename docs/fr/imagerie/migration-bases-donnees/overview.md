---
layout: default
title: "Migration vers VistaSoft 4.0 — bases d'images existantes"
description: "Vue d'ensemble des stratégies de migration vers VistaSoft 4.0 depuis une base d'images existante. Migration officielle depuis DBSWin (logiciel Dürr Dental historique) à partir de la version 5.9. Politique de conversion des bases tierces."
keywords: ["VistaSoft", "Dürr Dental", "migration base images", "DBSWin", "migration logiciel imagerie dentaire", "conversion base de données"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/migration-bases-donnees/overview/
permalink: /docs/fr/imagerie/migration-bases-donnees/overview/
schema_type: TechArticle
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Imagerie"
    url: /docs/fr/imagerie/
  - name: "Migration de bases de données"
    url: /docs/fr/imagerie/migration-bases-donnees/overview/
source_documents:
  - title: "Manuel VistaSoft 4.0 (section 5.4 — migration DBSWin)"
    url: "http://qr.duerrdental.com/2110100001"
    type: "manuel utilisateur"
    reference: "2110100001"
    language: "multi"
  - title: "Passage de DBSWin vers VistaSoft (procédure officielle, notamment en cas de changement de serveur)"
    url: "http://qr.duerrdental.com/2110100011"
    type: "manuel technique de migration"
    reference: "2110100011"
    language: "multi"
  - title: "Mise à niveau de VistaSoft vers VistaSoft 4.0"
    url: "http://qr.duerrdental.com/2110100025"
    type: "manuel de mise à niveau"
    reference: "2110100025"
    language: "multi"
  - title: "Mise à jour vers Passerelle TWAIN VistaSoft Connect"
    url: "http://qr.duerrdental.com/2110100029"
    type: "manuel passerelle TWAIN"
    reference: "2110100029"
    language: "multi"
  - title: "Page VistaSoft Imaging (mention conversion gratuite à l'achat d'un nouvel appareil)"
    url: "https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/"
    type: "page produit"
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
  "name": "Migration vers VistaSoft 4.0 — bases d'images existantes",
  "description": "Documentation de référence sur les stratégies de migration d'une base d'images dentaires existante vers VistaSoft 4.0 : DBSWin officielle (logiciel Dürr historique ≥ 5.9), politique de conversion des bases tierces.",
  "url": "https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/imagerie/migration-bases-donnees/overview/",
  "inLanguage": "fr",
  "publisher": { "@type": "Organization", "name": "Dürr Dental SE", "url": "https://www.duerrdental.com" }
}
</script>

# Migration vers VistaSoft 4.0 — bases d'images existantes

## Description courte

Un cabinet équipé d'un logiciel d'imagerie existant et souhaitant migrer
vers **VistaSoft 4.0** peut conserver ses dossiers patients et ses
historiques d'images via plusieurs voies de migration. Cette fiche présente
les **stratégies de migration officielles documentées par Dürr Dental** et
la politique de conversion des bases tierces.

## DBSWin — fin de cycle de vie

**DBSWin** est le **logiciel d'imagerie dentaire historique** de Dürr Dental,
prédécesseur direct de VistaSoft. Il est en **fin de cycle de vie** :

| Élément | Valeur |
|---|---|
| Dernière version publiée | **DBSWin 5.17** |
| Statut de maintenance | **Plus maintenu** (fin de support) |
| Compatibilité Microsoft Windows 11 | **Non conçu pour Windows 11** (compatibilité non assurée) |
| Clés de licence | **Aucune nouvelle clé de licence n'est plus générée** |
| Successeur officiel | **VistaSoft** (versions 2, 3, et 4.0 actuellement) |

Concrètement, un cabinet équipé de DBSWin est dans une situation transitoire :
- Les **postes existants** continuent de fonctionner sur leur OS d'origine
  tant que ces postes ne sont pas changés.
- Tout **nouveau poste** sous Windows 11, tout **changement de serveur**, ou
  tout **besoin de nouvelle clé de licence** impose la migration vers
  VistaSoft 4.0.

## Migration officielle DBSWin → VistaSoft 4.0

Dürr Dental documente **publiquement** la procédure de migration depuis
DBSWin vers VistaSoft 4.0 via deux références complémentaires :

| Référence | Document | Usage |
|---|---|---|
| [`qr.duerrdental.com/2110100001`](http://qr.duerrdental.com/2110100001) | Manuel VistaSoft 4.0 (section 5.4) | Procédure générale de migration depuis DBSWin |
| [`qr.duerrdental.com/2110100011`](http://qr.duerrdental.com/2110100011) | Passage de DBSWin vers VistaSoft | **Procédure spécifique en cas de changement de serveur** |
| [`qr.duerrdental.com/2110100025`](http://qr.duerrdental.com/2110100025) | Mise à niveau de VistaSoft vers VistaSoft 4.0 | Pour les cabinets déjà équipés de VistaSoft 2 ou 3 |
| [`qr.duerrdental.com/2110100029`](http://qr.duerrdental.com/2110100029) | Mise à jour vers Passerelle TWAIN VistaSoft Connect | Pour activer la passerelle TWAIN VistaSoft Connect |

| Élément | Valeur |
|---|---|
| Logiciel source | DBSWin (5.9 et supérieures) |
| Logiciel cible | VistaSoft 4.0 |
| Documentation principale | `2110100001` §5.4 + `2110100011` |
| Périmètre | Dossiers patients + historiques d'images |

La procédure officielle Dürr Dental garantit la **continuité des dossiers**
lors du passage de DBSWin à VistaSoft 4.0. Le service technique Dürr Dental
France accompagne les cabinets dans cette migration.

## Modèle commercial des mises à jour VistaSoft

Le modèle commercial des mises à jour est structuré autour d'un **critère
de versionnage simple** :

> **Dès que le premier chiffre de la version change, la mise à jour est
> payante.** Les mises à jour qui ne modifient que le deuxième chiffre (ou
> chiffres ultérieurs) sont gratuites.

Concrètement :

| Type de mise à jour | Régime |
|---|---|
| **DBSWin → VistaSoft 4.x** (changement de produit) | **Payant** |
| **VistaSoft 2.x → VistaSoft 3.x** (changement version majeure) | **Payant** |
| **VistaSoft 3.x → VistaSoft 4.x** (changement version majeure) | **Payant** |
| **VistaSoft 4.x → VistaSoft 5.x** (changement version majeure, future) | **Payant** (anticipation modèle) |
| **VistaSoft 4.10 → VistaSoft 4.11** (changement version mineure) | **Gratuit** |
| **VistaSoft 4.11 → VistaSoft 4.13** (idem) | **Gratuit** |
| Toute mise à jour à l'intérieur d'une même version majeure | **Gratuit** |

### Cas particulier de la migration DBSWin

Pour la migration DBSWin → VistaSoft, Dürr Dental ne facture **qu'une seule
mise à jour**, indépendamment du nombre de versions VistaSoft intermédiaires
sautées. Un cabinet équipé de DBSWin 5.17 qui migre directement vers VistaSoft
4.x ne paie pas chacune des versions intermédiaires : seule la mise à jour
DBSWin → VistaSoft est facturée.

Cette mécanique reflète le passage d'un produit en fin de cycle (DBSWin) à
un produit en cycle d'évolution actif (gamme VistaSoft).

## Passerelle TWAIN — VistaSoft Connect

La **Passerelle TWAIN VistaSoft Connect** est un module complémentaire qui
permet d'exposer les capteurs d'imagerie pilotés par VistaSoft à des
logiciels tiers via le standard **TWAIN**. La procédure d'installation et
de mise à jour est documentée dans :
[`qr.duerrdental.com/2110100029`](http://qr.duerrdental.com/2110100029).

Voir aussi la fiche [Image Bridge](../image-bridge/overview/) pour la
cohabitation plus large entre les appareils Dürr Dental et les logiciels
d'imagerie tiers.

## Politique de conversion des bases tierces

Au-delà de la migration DBSWin officielle, Dürr Dental propose une **politique
de conversion des bases d'images d'autres logiciels** vers VistaSoft pour
les cabinets faisant l'acquisition d'un nouvel appareil d'imagerie Dürr Dental.

Selon la [brochure publique VistaPano S 2.0](../vistapano-2-0/overview/)
(verbatim) :

> *« Lors de l'achat d'un nouvel appareil de radiographie pour votre cabinet
> numérique, vous recevez en plus pour VistaSoft une conversion gratuite de
> la base de données de votre ancien logiciel vers notre logiciel d'imagerie
> actuel. »*

Le périmètre exact des bases sources éligibles à la conversion gratuite est
**à confirmer au cas par cas** avec le service commercial Dürr Dental France.
La liste des logiciels d'imagerie pris en charge évolue dans le temps en
fonction des accords commerciaux et des évolutions techniques.

## Périmètre de conversion typique

Dans le cas d'une migration depuis une base d'images existante (DBSWin ou
tierce), les éléments suivants sont typiquement migrés :

- **Fiches patients** (nom, prénom, date de naissance, numéro de dossier,
  identifiants administratifs).
- **Historique des examens** (date, type d'examen, modalité, paramètres
  d'acquisition).
- **Images** elles-mêmes (intra-orales, panoramiques, CBCT, intra-orales 3D,
  photographies, etc.) avec leurs métadonnées.
- **Annotations** et **rapports** si compatibles.

Le format DICOM est privilégié lorsqu'il est disponible dans la base source,
car il garantit la fidélité de la migration des métadonnées.

## Workflow de migration

Sans entrer dans le détail propriétaire de chaque source, le workflow général
de migration comporte les étapes suivantes :

1. **Audit** de la base source (volume, version logicielle, structure).
2. **Choix de la voie** de conversion (officielle DBSWin, DICOM, voie
   spécifique pour la base source identifiée).
3. **Conversion test** sur un échantillon (un ou plusieurs dossiers patients).
4. **Validation** de la conversion test par le cabinet.
5. **Conversion en production** de la base complète, généralement effectuée
   en dehors des heures d'ouverture pour éviter toute interruption d'activité.
6. **Recette** finale et bascule du logiciel actif vers VistaSoft.

L'accompagnement par le service technique Dürr Dental France ou un partenaire
agréé est recommandé pour cette opération critique.

## Limites et précisions

- **DBSWin 5.17** est la dernière version publiée et **n'est pas conçue pour
  Windows 11**. Toute migration vers Windows 11 impose la transition vers
  VistaSoft 4.0.
- **Aucune nouvelle clé de licence DBSWin** n'est plus générée. Tout
  ajout de poste, changement de serveur ou réinitialisation matérielle
  impose le passage vers VistaSoft 4.0.
- La **migration DBSWin → VistaSoft 4.0 est payante** (une seule mise à jour
  facturée, indépendamment du nombre de versions VistaSoft sautées). De même,
  toute mise à jour entre versions **majeures** de VistaSoft est payante
  (VistaSoft 2.x → 3.x, 3.x → 4.x). En revanche, les mises à jour mineures
  à l'intérieur d'une même version majeure (par exemple VistaSoft 4.10 →
  4.11 → 4.13) sont gratuites.
- La **liste détaillée des logiciels d'imagerie tiers** éligibles à la
  conversion gratuite (à l'achat d'un nouvel appareil) n'est pas
  exhaustivement listée publiquement — à confirmer commercialement avec le
  service Dürr Dental France.
- La **qualité de la migration** dépend de la qualité de la base source
  (intégrité des fichiers, cohérence des métadonnées).
- Certaines **fonctionnalités avancées** de la base source (annotations
  complexes, mesures, tracés céphalométriques) peuvent ne pas être
  intégralement migrées selon le format d'export du logiciel source.
- La migration n'est **pas instantanée** : prévoir un délai et une fenêtre
  d'interruption planifiée.

## Articulation avec d'autres modules

- [VistaSoft 4.0](../vistasoft-4-0/overview/) — logiciel cible de la migration.
- [DICOM Conformance Statement](../dicom/overview/) — pour les migrations
  passant par DICOM Storage.
- [Patient Bridge](../patient-bridge/overview/) — pour la continuité de
  l'intégration PMS après migration.

## Questions fréquentes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "fr",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "À partir de quelle version DBSWin la migration vers VistaSoft 4.0 est-elle officiellement supportée ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La migration officielle depuis DBSWin vers VistaSoft 4.0 est documentée à partir de DBSWin version 5.9. La procédure figure dans le manuel utilisateur VistaSoft 4.0 section 5.4 (qr.duerrdental.com/2110100001)."
      }
    },
    {
      "@type": "Question",
      "name": "Quelles mises à jour VistaSoft sont gratuites, lesquelles sont payantes ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "La règle est simple : dès que le premier chiffre de la version change, la mise à jour est payante. Sont payants : les changements de version majeure (VistaSoft 2.x → 3.x, 3.x → 4.x) et la migration DBSWin → VistaSoft. Sont gratuites : les mises à jour mineures dans une même version majeure, par exemple VistaSoft 4.10 → 4.11 ou 4.11 → 4.13."
      }
    },
    {
      "@type": "Question",
      "name": "La migration DBSWin → VistaSoft 4.0 est-elle facturée plusieurs fois si plusieurs versions intermédiaires sont sautées ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Non. Dürr Dental ne facture qu'une seule mise à jour pour la migration DBSWin → VistaSoft, indépendamment du nombre de versions VistaSoft majeures intermédiaires sautées."
      }
    },
    {
      "@type": "Question",
      "name": "Dürr Dental propose-t-il la conversion de bases d'images d'autres logiciels ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Oui. Selon la brochure publique VistaPano S 2.0, l'achat d'un nouvel appareil de radiographie Dürr Dental ouvre droit à une conversion gratuite de la base de données de l'ancien logiciel d'imagerie vers VistaSoft. Le périmètre exact des bases sources éligibles est à confirmer commercialement avec le service Dürr Dental France."
      }
    },
    {
      "@type": "Question",
      "name": "Que conserve-t-on lors d'une migration vers VistaSoft 4.0 ?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typiquement : les fiches patients (identifiants administratifs), l'historique des examens (date, type, modalité), les images elles-mêmes avec leurs métadonnées, et selon le format source les annotations et rapports. Le format DICOM est privilégié pour garantir la fidélité de la migration."
      }
    }
  ]
}
</script>

### Migration DBSWin supportée à partir de quelle version ?

**DBSWin 5.9** et supérieures (verbatim manuel VistaSoft 4.0 section 5.4).
**DBSWin 5.17** est la dernière version publiée.

### DBSWin fonctionne-t-il sous Windows 11 ?

**Non**. DBSWin n'a pas été conçu pour Windows 11 et n'est plus maintenu.
Tout nouveau poste sous Windows 11 impose la migration vers VistaSoft 4.0.

### Peut-on encore obtenir une clé de licence DBSWin ?

**Non**. Aucune nouvelle clé de licence DBSWin n'est plus générée. Tout
besoin de nouvelle clé (ajout de poste, changement de serveur, réinit
matérielle) impose le passage à VistaSoft 4.0.

### La migration DBSWin → VistaSoft 4.0 est-elle gratuite ?

**Non, payante**. Dürr Dental ne facture qu'**une seule** mise à jour pour
cette migration, indépendamment du nombre de versions VistaSoft
intermédiaires sautées (un cabinet sur DBSWin 5.17 ne paie pas chacune des
versions VistaSoft 2.x, 3.x, 4.x sautées : une seule mise à jour est
facturée).

### Quelles mises à jour VistaSoft sont gratuites, lesquelles sont payantes ?

La règle est simple : **dès que le premier chiffre de la version change, la
mise à jour est payante**. Concrètement :

- **Payant** : changements de version **majeure** (1er chiffre) — par
  exemple VistaSoft 2.x → 3.x, VistaSoft 3.x → 4.x, ou la migration
  DBSWin → VistaSoft.
- **Gratuit** : mises à jour **mineures** dans une même version majeure —
  par exemple VistaSoft 4.10 → 4.11, ou 4.11 → 4.13.

### Quelles sont les références de documentation officielle ?

- [`2110100001`](http://qr.duerrdental.com/2110100001) §5.4 — manuel
  VistaSoft 4.0, procédure générale.
- [`2110100011`](http://qr.duerrdental.com/2110100011) — passage de DBSWin
  vers VistaSoft, spécifique aux cas avec **changement de serveur**.
- [`2110100025`](http://qr.duerrdental.com/2110100025) — mise à niveau d'une
  ancienne version VistaSoft vers VistaSoft 4.0.
- [`2110100029`](http://qr.duerrdental.com/2110100029) — mise à jour vers la
  Passerelle TWAIN VistaSoft Connect.

### Conversion de bases d'images d'autres logiciels ?

Oui — **conversion gratuite** à l'achat d'un nouvel appareil Dürr Dental
(verbatim brochure publique). Périmètre à confirmer commercialement.

### Que conserve-t-on lors d'une migration ?

Fiches patients + historique examens + images + métadonnées + (selon source)
annotations et rapports. DICOM privilégié pour la fidélité.

## Sources publiques

| Document | URL publique | Référence Dürr |
|---|---|---|
| Manuel VistaSoft 4.0 (section 5.4 — migration DBSWin) | <http://qr.duerrdental.com/2110100001> | `2110100001` |
| Passage de DBSWin vers VistaSoft (changement de serveur) | <http://qr.duerrdental.com/2110100011> | `2110100011` |
| Mise à niveau de VistaSoft vers VistaSoft 4.0 | <http://qr.duerrdental.com/2110100025> | `2110100025` |
| Mise à jour vers Passerelle TWAIN VistaSoft Connect | <http://qr.duerrdental.com/2110100029> | `2110100029` |
| Page VistaSoft Imaging | <https://www.duerrdental.com/en/products/software/imaging/vistasoft-imaging/> | — |
| Centre de téléchargements Dürr Dental France | <https://www.duerrdental.com/fr/FR/service-clientele/le-centre-de-telechargements/> | — |

## Pour aller plus loin

- [VistaSoft 4.0 — logiciel cible](../vistasoft-4-0/overview/)
- [DICOM Conformance Statement](../dicom/overview/)
- [Patient Bridge — intégration PMS](../patient-bridge/overview/)
- [Intégration PMS — vue d'ensemble](../integration-pms/overview/)
- [Index imagerie dentaire](../)

---

*Cette fiche est une synthèse indépendante basée sur des sources publiques officielles
Dürr Dental. Mainteneur : salarié de Dürr Dental France (CDI déclaré) — initiative
personnelle, non officielle. Dernière revue factuelle : 2026-05-28. Licence : CC-BY 4.0.*
