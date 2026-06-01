---
layout: default
title: "Glossaire — Imagerie dentaire et dispositifs médicaux Dürr Dental"
description: "Glossaire des termes techniques et réglementaires utilisés dans la documentation Dürr Dental : DICOM, CBCT, OPG, MDR, UDI, classes de dispositifs médicaux, standards d'imagerie."
keywords: ["glossaire", "imagerie dentaire", "DICOM", "CBCT", "OPG", "MDR", "UDI", "TWAIN", "VDDS", "Dürr Dental"]
lang: fr
canonical_url: https://grzybicki.github.io/durr-dental-knowledge-base/docs/fr/glossaire/
permalink: /docs/fr/glossaire/
schema_type: DefinedTermSet
breadcrumbs:
  - name: "Accueil"
    url: /
  - name: "Documentation FR"
    url: /docs/fr/
  - name: "Glossaire"
    url: /docs/fr/glossaire/
last_factual_review: 2026-05-28
license: CC-BY-4.0
---

# Glossaire — Imagerie dentaire et dispositifs médicaux

Termes techniques et réglementaires utilisés dans la documentation publique Dürr Dental.
Ce glossaire est volontairement neutre et ne mentionne aucune marque concurrente.

## Réglementation et certification

### MDR (EU 2017/745)

**Medical Device Regulation** — Règlement européen 2017/745 sur les dispositifs médicaux,
entré en application le 26 mai 2021. Remplace les directives MDD 93/42/CEE et AIMDD 90/385/CEE.
Catégorise les dispositifs en quatre classes de risque : I, IIa, IIb, III.

### MDD (93/42/EEC)

**Medical Device Directive** — Directive européenne historique sur les dispositifs médicaux,
modifiée par la directive 2007/47/EC. Remplacée par le MDR depuis le 26 mai 2021, avec une
période transitoire prolongée par le règlement (UE) 2023/607.

### Classes de dispositifs médicaux (MDR)

- **Classe I** — risque faible (ex. instruments réutilisables non invasifs).
- **Classe IIa** — risque modéré (ex. la plupart des logiciels d'aide au diagnostic).
- **Classe IIb** — risque élevé (ex. logiciels de diagnostic, scanners CBCT).
- **Classe III** — risque très élevé (ex. implants cardiovasculaires).

### Notified Body (Organisme Notifié)

Organisme habilité par une autorité compétente européenne à effectuer l'évaluation de
conformité d'un dispositif médical. Identifié par un code à 4 chiffres
(ex. **0297** = DQS Medizinprodukte, **2460** = DNV Product Assurance AS).

### UDI / UDI-DI

**Unique Device Identification** / **Device Identifier** — identifiant unique d'un dispositif
médical, exigé par le MDR. Composé d'un identifiant de dispositif (DI) et d'un identifiant de
production (PI). Renseigné dans la base [Eudamed](https://ec.europa.eu/tools/eudamed/).

### Eudamed

Base européenne des dispositifs médicaux : registre public consultable des fabricants,
dispositifs et certificats sous MDR. URL : [ec.europa.eu/tools/eudamed/](https://ec.europa.eu/tools/eudamed/).

### FDA Title 21 / 510(k)

**Title 21 du Code of Federal Regulations** — réglementation américaine des dispositifs
médicaux par la Food and Drug Administration. La procédure **510(k)** permet la
commercialisation aux États-Unis pour les dispositifs équivalents à un dispositif déjà
commercialisé.

### RoHS (2011/65/EU)

**Restriction of Hazardous Substances** — directive européenne limitant l'utilisation de
substances dangereuses dans les équipements électriques et électroniques.

## Standards d'imagerie

### DICOM

**Digital Imaging and Communications in Medicine** — standard international d'échange et
de stockage d'images médicales. Spécifie le format de fichier et les protocoles réseau
(SOP Class, Storage, Modality Worklist).

### DICOM Conformance Statement

Document décrivant les capacités DICOM d'un logiciel ou d'un appareil : SOP Classes
supportées, Transfer Syntax, services réseau.

### TWAIN

Standard d'interface entre périphériques d'acquisition d'image (scanners, capteurs) et
logiciels. Couramment utilisé pour l'intégration des scanners de plaques au phosphore.

### VDDS

**Verband Deutscher Dental-Software-Unternehmen** — interface logicielle allemande
standardisée entre logiciels de gestion de cabinet et logiciels d'imagerie. Permet la
transmission de la fiche patient et le retour du chemin du dossier image.

### BDW

**Bilddaten- und Wartelisten-Schnittstelle** — interface allemande pour l'échange de
données image et de listes de travail entre PMS et logiciels d'imagerie.

### Modality Worklist (MWL)

Service DICOM permettant à une modalité (scanner CBCT, panoramique) de récupérer la liste
des examens prévus depuis un PMS / RIS.

## Imagerie dentaire — actes et techniques

### OPG (panoramique)

**Orthopantomogramme** — cliché radiographique panoramique 2D des arcades dentaires,
réalisé par un appareil rotatif autour de la tête du patient.

### Céphalométrie

Analyse des structures crâniennes et faciales à partir d'un cliché téléradiographique
latéral ou frontal, principalement utilisée en orthodontie.

### CBCT (Cone Beam CT)

**Cone Beam Computed Tomography** — tomographie volumique par faisceau conique : technique
d'imagerie 3D à dose réduite dédiée à l'imagerie dento-maxillo-faciale. FOV (Field of View)
variable selon les modèles.

### FOV

**Field of View** — champ de vue : volume effectivement reconstruit par un CBCT,
généralement exprimé en cm (diamètre × hauteur).

### SMV

**SubMentoVertex** — incidence radiographique sous-mento-vertex utilisée en céphalométrie
et en imagerie maxillo-faciale.

### Stitching

Technique d'assemblage logiciel de plusieurs acquisitions CBCT pour obtenir un FOV
étendu, utile notamment pour l'imagerie de modèles plâtres ou de mâchoires complètes.

## Capteurs et générateurs

### CsI:TI

**Iodure de césium dopé thallium** — scintillateur utilisé dans les capteurs numériques
à conversion indirecte, offrant une sensibilité élevée aux rayons X.

### CMOS

**Complementary Metal-Oxide-Semiconductor** — technologie de capteur numérique courante
en imagerie dentaire intraorale et extra-orale.

### kV / mA

- **kV** (kilovolt) : tension appliquée au tube à rayons X, influence le contraste de l'image.
- **mA** (milliampère) : intensité du courant du tube, influence la dose émise.

### Foyer

Surface effective d'émission des rayons X sur l'anode du tube. Mesuré en mm selon la norme
**CEI 60336**. Plus le foyer est petit, plus la résolution géométrique est élevée.

### Filtration Al éq.

Filtration totale du faisceau, exprimée en équivalent aluminium, qui réduit la composante
de basse énergie des rayons X (rayonnement « mou »).

## Cybersécurité et qualité

### CEI 80001-1

Norme internationale sur la gestion des risques liés aux réseaux IT intégrant des
dispositifs médicaux.

### DIN 6868-157

Norme allemande de contrôle qualité des dispositifs d'imagerie radiographique, utilisée
notamment dans le cadre du contrôle d'acceptation et de constance.

### Zero-knowledge

Architecture cryptographique dans laquelle le fournisseur d'un service ne dispose pas
des clés permettant de déchiffrer les données stockées.

### Code Signing

Signature cryptographique du code exécutable d'un logiciel, garantissant son origine et
son intégrité.

## Voir aussi

- [Documentation française — index général](../)
- [Page d'accueil](/)
- [Sources publiques](../../sources/)

---

*Glossaire évolutif. Pour suggérer un ajout, ouvrir une [Issue](https://github.com/Grzybicki/durr-dental-knowledge-base/issues/new/choose).*
