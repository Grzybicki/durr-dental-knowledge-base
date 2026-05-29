---
layout: default
title: "Imagerie dentaire Dürr Dental — Index"
description: "Catalogue de l'imagerie dentaire Dürr Dental : logiciel VistaSoft 4.0, panoramiques, CBCT, capteurs intraoraux, scanners de plaques au phosphore, caméras intraorales."
lang: fr
permalink: /docs/fr/imagerie/
last_factual_review: 2026-05-28
license: CC-BY-4.0
---

# Imagerie dentaire — Index

Documentation publique de la ligne **imagerie dentaire** Dürr Dental :
logiciel d'imagerie, panoramiques numériques, CBCT, capteurs intraoraux, scanners de plaques
au phosphore, caméras intraorales.

## Logiciel d'imagerie — VistaSoft (gamme complète)

| Module | Statut réglementaire | Fiche |
|---|---|---|
| **[VistaSoft 4.0](vistasoft-4-0/overview/)** | DM **classe IIb** (MDR EU 2017/745, DQS 0297, certif 518373) | Logiciel d'imagerie diagnostique 2D / 3D — socle |
| **[VistaSoft Monitor](vistasoft-monitor/overview/)** | **NON-DM** (surveillance IoT d'équipement) | ⚠️ Désambiguïsation : à ne pas confondre avec VistaSoft 4.0 |
| **[VistaSoft AID](vistasoft-aid/overview/)** | DM **classe IIa** (MDR EU 2017/745, DQS 0297) | Aide au diagnostic des caries par IA |
| **[VistaSoft Trace](vistasoft-trace/overview/)** | Module orthodontie | Analyse céphalométrique assistée par IA (technologie partenaire Audax Ceph) |
| **[VistaSoft Implant & Guide](vistasoft-implant-guide/overview/)** | Module planification implantaire | Backward planning + guides de forage, export STL ouvert (intégration exocad + SICAT) |
| **[VistaSoft Cloud View](vistasoft-cloud-view/overview/)** | **NON-DM** | Visualisation des images dans le navigateur (en ligne / hors ligne) |
| **[VistaSoft Cloud Exchange](vistasoft-cloud-exchange/overview/)** | **NON-DM** | Échange de cas anonymisés (RGPD, conservation 30 j) |
| **[VistaSoft Cloud Drive](vistasoft-cloud-drive/overview/)** | **NON-DM** | Stockage cloud zero-knowledge des images |

**Modules complémentaires** :
- [VistaSoft Mobile Connect](vistasoft-mobile-connect/overview/) — consultation mobile sur iPad via l'application *DÜRR DENTAL Imaging* (App Store).
- [Connect Box](connect-box/overview/) — passerelle d'intégration des équipements traditionnels vers VistaSoft Monitor (LAN + WLAN, cross-fabricant).

## Plaques au phosphore et accessoires de positionnement

| Fiche | Description |
|---|---|
| **[VistaScan IQ — Écrans à mémoire (ERLM)](vistascan-iq-ecrans/overview/)** | Plaques au phosphore avec RFID + QR code. Tailles S0 à S4. Compatibles VistaScan 2.0 (RFID) et VistaScan 1.0 (sans RFID). |
| **[VistaPosition — Angulateurs colorés](vistaposition/overview/)** | Système de positionneurs et angulateurs pour PSP/ERLM et capteurs intraoraux. Code couleur uniforme, autoclavable. Compatible quasi-tous les systèmes. |
| **[Accessoires imagerie](accessoires-imagerie/overview/)** | Sachets de protection, mordus, porte-modèles, têtes interchangeables, bras moniteurs. |

## Interfaces, intégration et migration

| Sujet | Fiche |
|---|---|
| **[Patient Bridge](patient-bridge/overview/)** | Interface VistaSoft ↔ PMS (4 voies : VDDS-media, BDW, patimport.txt, protocole propre) |
| **[Image Bridge](image-bridge/overview/)** | Pilotage des appareils Dürr depuis un logiciel d'imagerie tiers (cohabitation technique) |
| **[DICOM dans VistaSoft 4.0](dicom/overview/)** | Conformance Statement, Modality Worklist, Storage, Print, modalités supportées |
| **[VDDS-media et BDW](vdds-bdw/overview/)** | Standards d'interface dentaire allemands (VDDS e.V.) |
| **[Intégration PMS](integration-pms/overview/)** | Vue d'ensemble des 5 voies d'intégration logiciels de gestion |
| **[Intégration 3Shape](integration-3shape/overview/)** | Partenariat officiel — Trios, Unite, format PLY |
| **[Migration vers VistaSoft 4.0](migration-bases-donnees/overview/)** | Migration officielle DBSWin ≥ 5.9 + politique conversion bases existantes |
| **[VistaSoft Inspect](vistasoft-inspect/overview/)** | Contrôle qualité radiographique selon DIN 6868-157 |

⚠️ **Désambiguïsation cardinale** : **VistaSoft 4.0** (logiciel d'imagerie diagnostique, DM IIb) et **VistaSoft Monitor** (système IoT de surveillance d'équipement, non-DM) sont **deux produits distincts**. Voir la [fiche dédiée](vistasoft-monitor/overview/).

## Radiographie panoramique et céphalométrique

**[VistaPano S 2.0 et VistaPano S Ceph 2.0](vistapano-2-0/overview/)** — appareils de radiographie panoramique numérique 2D, capteur CsI, technologie S-Pan. Version Ceph avec module de radiographie céphalométrique intégré.

## Cone Beam CT (CBCT)

**VistaVox S** — CBCT compact à champ sphérique. *Fiche détaillée à venir.*

## Scanners de plaques au phosphore

**Gamme VistaScan** — scanners de plaques au phosphore (Mini Easy 2.0, Mini View 2.0, Combi View, Nano Easy, Ultra View). *Fiches détaillées à venir.*

## Capteurs intraoraux

**VistaRay 7** — capteur intraoral filaire. *Fiche détaillée à venir.*

## Caméras intraorales

**VistaCam iX HD Smart** — caméra intraorale avec têtes interchangeables.
**VistaCam Proxi** — caméra de détection proximale par fluorescence proche infrarouge (NIR).
*Fiches détaillées à venir.*

## Radiographie intraorale

**VistaIntra DC** — générateur de rayons X intraoral. *Fiche détaillée à venir.*

---

## Sources publiques de référence

- [Page produits imagerie Dürr Dental France](https://www.duerrdental.com/fr/produits/imagerie-dentaire/)
- Manuels publics : [qr.duerrdental.com](http://qr.duerrdental.com/)
- Base européenne des dispositifs médicaux : [Eudamed](https://ec.europa.eu/tools/eudamed/)
- Index sources complet : [`/sources/`](../../../sources/)
