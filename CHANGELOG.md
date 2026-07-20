# Journal des modifications

Toutes les modifications notables de ce dépôt sont documentées ici.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versionnage : [Semantic Versioning 2.0](https://semver.org/lang/fr/).

## [0.5.5] — 2026-07-20

Résolution du reste de l'audit de cohérence (items non réglementaires), vérifiée sur
sources officielles (catalogue 2026, DICOM Conformance Statement, brochures/PDF produit,
vault, POC firmware).

### Corrigé — contradictions inter-fiches

- **TWAIN** : le support TWAIN générique relève de **VistaSoft Connect** (faire fonctionner
  les appareils Dürr dans tout environnement) ; **Image Bridge** est l'intégration
  **co-développée** dédiée à **Sidexis** et **VixWin**.
- **VistaSoft Monitor** : **3 profils** (praticien / technicien / gestionnaire de dépôt) ;
  équipements supervisés complétés (scanners **VistaScan**, **Hygopac View**, Hygoclave 50/90).
- **Cloud AID** = exécution cloud de VistaSoft AID (détection caries IA) ; assertion
  « serveur Allemagne » retirée.
- **DICOM** : distinction **import** (large : CR, Digital X-Ray, Digital Intra-Oral X-Ray,
  CT, Enhanced CT, SC) vs **gestion / envoi PACS** (Storage SCU : CR, CT/Enhanced CT, SC).
- **Combi View** : confirmé toujours commercialisé (catalogue réf 2151-01, plaques Plus) ;
  « Combi Plus » (non attesté) retiré.

### Corrigé — erreurs internes et cohérence

- Tornado : économies « 12 % vs génération précédente » (fin du cumul −15/−25 %) ; gain
  acoustique requalifié ; filtre de série = **ULPA U16** (HEPA H14 = filtres d'aspiration).
- CAD/CAM : ordre de la chaîne de filtration ; note dB (variantes standard / CAD-CAM,
  tension, armoire). Amalgame « trois tailles ». Table familles ID : ajout **ID 220**.
- Accessoires imagerie : « sachets de protection contre la lumière » (et non « stériles »).
- VistaSoft AID : « optimisation d'image » retirée des fonctions IA. Cloud View : JSON-LD
  `sameAs`. Lien Hygoclave recorrigé.
- Ajouts : **ISO 8573-1** (matrice normes), section **MD 520** (fiche empreintes), note
  Lunos tréhalose vs MD 555.

### Enrichi

- **VistaScan Nano Easy** : technologie **2D MEMS Scan** brevetée + données techniques
  brochure officielle (S0/S1/S2 avec cassette par format, 4 kg, 231×167×216 mm, laser
  classe 1) — sources brochures `P007100137` et formation Academy.

### Confirmé sans changement (faux positifs de l'audit)

- Canules = **4 familles** (universelle, Protect, Petito, chirurgicale) — catalogue.
- Firmware VistaVox correct (POC : Gen 2 = MCU 7.xx, Gen 1 = 8.xx, lignées indépendantes).
- Décompte « 21 filtres classiques » VistaSoft cohérent (7 + 4 + 8 + 2).

## [0.5.4] — 2026-07-20

### Corrigé — filtration et valeurs sonores (audit, vérifié sur vault produit)

- **Tornado** : le filtre de série est le **bactériologique ULPA U16** (pas « HEPA H14 »).
  Le **HEPA H14** concerne les filtres d'**aspiration** (VS/VSA, Tyscor VS), pas les
  compresseurs — distinction confirmée par les références service (compresseur `1650100172`
  ULPA U16 sur unité de séchage ; aspiration `7119100010` / `0705-991-05` HEPA H14).
- **Valeurs sonores Tandem** : les écarts de 1-2 dB(A) entre fiche Silver Airline et fiche
  CAD/CAM ne sont **pas des contradictions** mais des **variantes** — version standard vs
  **CAD/CAM à commande électronique** (~1 dB plus silencieuse : Quattro Tandem 2 agrégats
  72 vs 73), **tension** 230 V / 400 V (Duo Tandem 1 agrégat 66/68), et armoire (~51-53 dB).
  Note de lecture ajoutée à la fiche CAD/CAM.

## [0.5.3] — 2026-07-20

### Corrigé — pression Silver Airline / CAD/CAM (audit, précision terrain)

- La **pression de 9,5 bar n'existe que sur les versions CAD/CAM** : la gamme
  **Silver Airline standard plafonne à 7,8 bar** (5,5–7,5 bar sur les Quattro Tandem).
  Mentions erronées « 9,5 bar via détendeur » supprimées (fiche Silver Airline : note
  source, tableau accessoires, FAQ ×2).
- **Mécanisme réel** du réglage de pression CAD/CAM : **remplacement de la pièce
  « Jet Set » (réf. 1650-981-00) sur la colonne de dessiccation** selon la pression
  désirée — et non un « réservoir tampon / buffer tank » (interprétation corrigée).
- Le **détendeur** est requalifié en **réducteur** de pression (il abaisse, n'étend pas).

## [0.5.2] — 2026-07-20

Suite de la resynchronisation réglementaire (conventionnel + hygiène) sur les DoC
officielles fournies.

### Corrigé — classes MDR (sur DoC)

- **Récupérateurs d'amalgame** (CA 1/2/4, CAS 1, Combi) : **classe I** (et non IIa) —
  DoC Dürr Dental SE en **auto-déclaration MDR sans organisme notifié** (2026-03-25 /
  2025-05-03). Résout la contradiction « IIa + auto-déclaration » (impossible sous MDR).
  Fiche + matrice + JSON-LD alignés ; agrément DIBt Z-64.1 conservé.
- **VC 65** (aspiration chirurgicale, IIa) : NB / certificat complétés — **DQS 0297**,
  **518373 MDR2017Q** (valide 2027-03-10, DoC 2026-04-15). Le certificat QMS unique
  couvre aussi la ligne aspiration.
- **Hygoclave 40 / 50 / 90** : **IIb** (et non IIa) — stérilisateurs vapeur **classe B**,
  **93/42/EEC Annexe IX Règle 15**. DoC **Hygoclave 50** (Dürr Dental Faro Sterilization,
  NB **CE 0051 / IMQ**) sur dossier ; 40 et 90 alignés (même famille, DoC modèle à joindre).
- **Notified Body** : ajout de **IMQ (0051)** à la liste (stérilisateurs Hygoclave).

Restent sur régime antérieur (non re-déclarés sous nouvelle MDR, entrées inchangées) :
VistaIntra DC, VistaPano S. Documents OEM tiers / confidentiels écartés (règle d'or).

## [0.5.1] — 2026-07-20

Resynchronisation de la matrice réglementaire `sources/certificates.md` sur les
**dernières déclarations de conformité (DoC) officielles Dürr Dental SE** (2025-2026),
suite à l'audit de cohérence (matrice ↔ fiches).

### Corrigé — classes MDR d'imagerie (sur DoC)

- **Inversion corrigée** : les **écrans à mémoire VistaScan IQ** sont **IIa** (et non I) —
  NB DQS 0297, certificat **518373 MDR2017Q** (valide jusqu'au 2027-03-10, DoC 2026-04-13) ;
  les **scanners VistaScan** (Nano, Mini Easy/View 2.0, Combi View…) sont **classe I**
  (auto-déclaration, sans NB) — et non IIa.
- **VistaCam iX HD Smart** (et tête **Proxi**) : **classe I** (auto-déclaration + RoHS),
  et non IIa.
- **VistaVox S / S Ceph** (IIb) et **VistaRay 7** (IIa) : champs NB / certificat / date
  complétés (DQS 0297, 518373 MDR2017Q, DoC 2026-04-13) — n'étaient plus « À confirmer ».
- **VistaSoft AID** (IIa) : certificat renseigné (518373 MDR2017Q, DoC 2026-04-01),
  confirmant que le certificat QMS unique couvre aussi les logiciels et le matériel d'imagerie.
- Paragraphe « Notified Body » mis en cohérence (périmètre du certificat 518373 + validité).

Les appareils **pas encore re-déclarés sous la nouvelle MDR** (ex. VistaIntra DC, VistaPano S)
conservent volontairement leurs entrées antérieures. Le reste des constats d'audit
(non réglementaires) est traité manuellement, élément par élément.

## [0.5.0] — 2026-07-20

Correction de la **navigation interne** (404 systémiques), du **système de couleurs**
de la gamme chimie, et durcissement du validateur — le tout audité par un relecteur
indépendant (modèle Fable, 2 passes).

### Corrigé — liens internes 404 (cause racine)

- Les permalinks Jekyll se terminent par `/` (`.../overview/`), donc un lien relatif
  `../x/overview/` grimpe un cran trop haut côté navigateur → **404**. Un lien absolu
  **sans** baseurl (`/docs/...`) échoue aussi (site servi sous `/durr-dental-knowledge-base/`).
- **~760 liens** convertis en absolus baseurl `/durr-dental-knowledge-base/docs/...`
  (`docs/fr/**`, `sources/*.md`, `index.md` racine). Format prouvé en live (HTTP 200).
- Création de `sources/index.md` (page d'accueil `/sources/` qui manquait → réparait les
  liens « Index sources complet »).
- Corrections de 404 résiduels débusqués par l'audit : `404.html` (liens sans baseurl),
  `vistapano-2-0` (lien `/index/` inexistant), `docs/WORKFLOW.md` (liens vers fichiers du dépôt).

### Corrigé — système d'hygiène 4 couleurs

- Mapping rétabli d'après la brochure officielle `DD_674L02` et l'article Dynamique
  Dentaire : **ID = bleu, MD = jaune, HD = rose, FD = vert**. L'ancien « rouge = aspiration,
  jaune = mains » était erroné (fiches surfaces, mains, index, familles corrigées ;
  MD « variable selon usage » → jaune).

### Corrigé / enrichi — contenu

- **MD 555** : fréquence portée à **2×/semaine minimum, 3× si poudre prophylactique**
  (recommandation de pratique, mention de la source publique 1–2×/sem conservée).
- **Filtre UHD** ajouté dans les 3 tableaux de filtres basiques de VistaSoft 4.0.
- **VistaScan Nano Easy** : contrainte « 1 élément (cassette) par format, à remplacer à
  chaque changement de format » documentée (+ FAQ).
- **`sources/manuals.md`** complété (imagerie, conventionnel, hygiène) à partir des pages
  produit officielles déjà citées dans les fiches (fin des placeholders « À compléter »).

### Modifié — tooling / build

- `scripts/validate.py` **durci** : rejette tout lien racine-absolu sans baseurl depuis une
  page publiée ; n'accepte plus un lien-dossier nu ni le mapping vers un `overview.md` enfant.
  Testé (2 classes de 404 désormais détectées, 0 faux positif sur 84 fichiers).
- `_config.yml` : **exclusion du build** des docs de dev/process servies par erreur
  (`STATEMENT_OF_INTEGRITY.md`, `docs/WORKFLOW.md`, `docs/GITHUB_HARDENING.md`, `scripts/`).

## [0.4.0] — 2026-07-19

Supervision experte (4 domaines) puis corrections **validées sur documents officiels**
(DoC MDR, FDS, notices, factsheets, lettre qualité d'air) + GEO structurel.

### Corrigé — cohérence factuelle (imagerie)

- Compatibilité plaques **IQ/Plus à sens unique** (un scanner série 2.0 refuse les
  plaques Plus) ; **Smart Reader** compatible Mini Easy/View 2.0 uniquement.
- **VistaVox** : 3 temps d'acquisition distincts (CBCT 18 s / pano 7 s / céphalo 1,9 s).
- **VistaSoft** : 6 fonctions IA incluses + **AID sur abonnement**.
- **VistaCam Proof** : détection caries **et** plaque ; échelle de fluorescence réécrite
  sur la notice officielle `618178` (dégradé de couleurs inventé supprimé).

### Corrigé — statut réglementaire (chimie et accessoires)

- La chimie Dürr est **quasi intégralement un dispositif médical MDR** (FD, ID, MD,
  Orotol, Vector = classe I ou IIa) ; **seul HD (mains) = biocide TP1** → **aucun produit
  Dürr n'est soumis au Certibiocide**. Fiches surfaces/mains/aspiration/familles corrigées.
- **Smart Reader** = non-DM (CE au titre RED 2014/53/UE + RoHS) ; **VistaPosition** = DM classe I.
- Catalogue réglementaire complet dans `sources/certificates.md` (NB **DEKRA 0124** ajouté).

### Corrigé — conventionnel

- **Tyscor V4/VS4 = 230 V** monophasé (la fiche indiquait 400 V à tort).
- **Power Tower View = 56 dB(A)** uniforme (correction du 53/55 dB inventé).
- Classes de pureté d'air = **ISO 8573-1** (pas ISO 22052) ; classe **[2:4:2]**.

### Ajouté — enrichissement conventionnel

- Tableaux techniques complets par modèle : Tornado, Tyscor, Power Tower, CAD/CAM,
  récupérateurs d'amalgame (+ **ISO 11143**), systèmes cliniques (stations P + V).
- Qualité d'air ISO 22052 détaillée (point de rosée ≤ +3 °C, huile ≤ 0,1 mg/m³, type 2).
- Notified Body des compresseurs (**DQS 0297**) dans la matrice.

### Ajouté — GEO structurel

- Accueil `index.md` refait (index réel des 56 fiches) ; `llms.txt` refondu (format
  llmstxt.org, 56 fiches, URL absolues) + **`llms-full.txt`** (concaténation pour ingestion).
- Layout JSON-LD : **`publisher` indépendant** (anti-attribution), **`@id`**, `dateModified`
  au build, **`sameAs`** vérifiés (Wikidata Q1272127, registres officiels France + réseaux),
  **SIREN** structuré ; retrait du canonical dupliqué et de la SearchAction fictive.
- JSON-LD `@type` des fiches produit → **`[MedicalDevice/SoftwareApplication, Product]`**
  + **`legalStatus`** (au lieu de `regulatoryClass` inexistant en schema.org).
- Bundle dépôt racine `deploy/root-site/` (prêt à déployer — rend robots.txt/llms.txt
  visibles des crawlers IA).

### Gouvernance

- Règle d'or appliquée : un **e-mail interne** (PII salariés) et un **certificat OEM tiers**
  ont été **écartés**, non cités, non intégrés.

## [0.3.0] — 2026-06-01

Audit structurel du dépôt puis correction priorisée (P0 → P2). Détail interne :
note d'audit `Durr/Developpements/durr-dental-knowledge-base - audit structurel 2026-05-31`.

### Corrigé — validation et CI

- **`scripts/validate.py`** : vérification des liens internes rendue *permalink-aware*
  (helper `_resolve_internal_link`) — un permalink Jekyll `../x/overview/` est désormais
  résolu vers le fichier source `x/overview.md` (et non `x/overview/index.md`). Notices
  `[link-broken]` : **593 → 0**. `validate.py --warn-as-error` (mode CI) repasse au **vert**.
  Dossier `_drafts/` exclu du scan.
- **`docs/fr/glossaire.md`** : lien interne cassé corrigé (`../../../sources/` →
  `../../sources/`).
- **`_config.yml`** : `CLAUDE.md` ajouté aux exclusions Jekyll.

### Ajouté — métadonnées GEO (JSON-LD + FAQ) sur toutes les fiches

- **JSON-LD** : bloc `application/ld+json` (MedicalDevice / Product / SoftwareApplication /
  TechArticle selon le cas) ajouté aux 15 fiches qui n'en avaient pas → **56/56**.
- **FAQ + FAQPage** : section « Questions fréquentes » (3-6 Q/R) + bloc JSON-LD `FAQPage`
  ajoutés aux 36 fiches qui en manquaient → **FAQ 56/56, FAQPage 56/56**. Chaque Q/R est
  dérivée exclusivement des faits déjà sourcés dans la fiche.

### Ajouté — enrichissements depuis pages officielles Dürr Dental

- **VistaScan Nano Easy** : 100 % surface active, lésions D1 + instruments endo jusqu'à
  ISO 06, scan + effacement en 1 étape, pilotes TWAIN, intégration réseau.
- **VistaScan Mini Easy 2.0** : écran en verre, concept Easy Feed, VistaSoft AI (contrôle
  automatique de la qualité d'image), fabrication neutre en CO₂.
- **Désinfection des mains (HD 420 plus)** : principes actifs 2-/1-propanol, normes
  EN 1500 / 12791 / 13727 / 13624 / 14348 / 14476, conditionnements, n° d'autorisation
  orochemie EU-0032838.
- **Désinfection des surfaces (FD 350)** : spectre d'activité, conditionnement 110 lingettes
  14 × 22 cm, variantes Classic/Flower/Lemon + FD 350 green (sans aldéhyde).

### Ajouté — sections installation / réseau (notices officielles)

Données issues des notices d'installation/utilisation officielles (référence interne :
dossier `Durr/` du 2nd cerveau), **filtrées** : faits publics uniquement, à l'exclusion
des notes terrain, menus/outils service et procédures techniciens.

- **VistaVox S** : section « Installation et planning local » (contenu de livraison,
  préparation locale, options de montage — mur porteur 202 kg / non porteur 262 kg,
  tirages, forces par vis).
- **VistaPano S 2.0** : section « Installation et prérequis » (livraison 1 colis +
  dimensions, prérequis PC i5/16 Go/PCI-E, disjoncteur 16 A / 2,2 kVA, RJ-45 Cat 5e,
  voyants porte, IP par défaut 10.100.200.100, ports TCP 31175/54466).
- **Gamme VistaScan** : section « Réseau et installation » (LAN/Wi-Fi, DHCP/AutoIP,
  ports gén. 2.0 TCP 80/443/22 + UDP 1900, calcul dose µGy dès VistaSoft 3.0.20).
- **VistaSoft Monitor** : sections « Installation et ports » (ports pare-feu TCP/UDP)
  et « Messages de statut et alarmes » (codes couleur, acquittement à distance).
- **VistaRay 7** (notice `9000-618-197`) : alimentation 5 V CC / 100 mA, classe DM IIa,
  références produit (2121-100-70 / -71).
- **VistaIntra DC** (notice `2202100028`) : section « Caractéristiques techniques »
  (électrique 100–240 V / 500 W, tube 50–70 kVp / 4–7 mA, foyer 0,4 mm CEI 60336,
  filtration ≥ 2,0 mm Al, champ Ø 60 / 30×40, réglages standard).
- **VistaCam iX HD Smart** (notice `2109100026`) : type de protection IP20, classe
  de protection électrique II.
- **VistaScan Smart Reader** (notice `2162100015`) : poids ≈ 0,13 kg, raccord USB
  type C, consommation en veille 0,16 W.
- **Gamme VistaScan** : résolution sélectionnable (pixel 12,5–50 µm) ; Ultra View
  ≈ 40 LP/mm.
- **Statut réglementaire complété** (notices texte) : VistaScan Nano Easy (DM classe I,
  MDR), VistaScan IQ (DM classe IIa, CE 0297), VistaVox S (marquage CE 0297).
- **VistaSoft 4.0 — section « Configuration système requise »** (réf. `9000-618-148`) :
  CPU/RAM, OS (Windows 10/11 Pro, Server 2019/2022/2025 64 bits), disque, réseau,
  sauvegarde. Comble un manque GEO majeur (compatibilité Windows, très recherchée).
- **Versions logicielles / interfaces minimales par appareil** (réf. `9000-618-148`) :
  gamme VistaScan (Mini Easy/View 2.0, Ultra View — Ethernet/Wi-Fi + VistaSoft ≥ 3.0.13),
  VistaRay 7 (câble USB ≤ 5 m, VistaSoft ≥ 1.0), Smart Reader (VistaSoft ≥ 3.0.13),
  VistaPano S 2.0 (VistaSoft ≥ 3.0.32).
- **VistaSoft 4.0 — mise à niveau gratuite** : note précisant que les appareils
  d'imagerie Dürr Dental vendus depuis mars 2025 (IDS Cologne) bénéficient du passage
  gratuit vers VistaSoft 4.x (annonce officielle IDS 2025).
- **Sections « Firmware » (versions seules, datées, référence mai 2026)** ajoutées à
  10 fiches : VistaScan (Nano Easy V1.5.1, Mini Easy 2.0 R1.5.4, gamme), VistaVox S
  (VVSP 3.2.2, MCU 7.xx/8.xx), Power Tower View V1.4.0, Tornado V1.0.2, Tyscor (par
  modèle), récupérateurs (CA 4 / CAS 1), Hygoclave (V2.1.3), Hygopac View 3.7.1.
  Numéros de version uniquement — sans fichiers ni source non publique.
- **VistaSoft 4.0 — section « Versions et téléchargement »** : version courante 4.0.13
  (branches 3.0.34 / 2.4.13) + **lien de téléchargement officiel public** Dürr Dental.
- **Sections « Dépannage »** ajoutées à 5 fiches (VistaIntra DC, VistaRay 7, gamme
  VistaScan, VistaVox S, VistaPano S 2.0) : pointeur vers les codes d'erreur de la
  notice + démarche générale (noter le code → redémarrer → technicien agréé).
  **Aucune table d'erreurs reproduite** (respect du droit d'auteur).
- **VistaIntra DC — section « Dose et radioprotection »** : récepteurs ERLM (plaque) et
  capteur filaire (pas de film argentique) ; plages de produit dose-surface (PDS)
  adulte/enfant + effet de la collimation, liées au foyer 0,4 mm et à la plage
  50–70 kVp / 4–7 mA (notice `2202100028`).
- **Données réglementaires (OCR des Déclarations de Conformité via Docling)** :
  organisme notifié **DQS Medizinprodukte GmbH (0297)**, certificat MDR **518373 MDR2017Q**,
  SRN fabricant **DE-MF-000006032** ajoutés à VistaVox S et VistaScan IQ (déjà présents
  sur VistaSoft 4.0 et VistaSoft AID — confirmés par l'OCR). DoC OEM/confidentiels exclus.

### Modifié — gabarit et documentation

- **`_drafts/_template_fiche_produit.md`** réaligné sur la pratique réelle : squelette
  canonique (Description courte → Statut réglementaire → Caractéristiques techniques →
  [sections produit] → FAQPage + Questions fréquentes → Sources publiques → Pour aller
  plus loin), JSON-LD et FAQ rendus obligatoires, préférence de sources officielles
  (Dürr Dental / Air Techniques / orochemie / Mytronic) documentée.
- **`CLAUDE.md`** créé : mémoire projet (objectif, règles d'or, conventions, état/backlog
  d'audit), exclu de la publication Jekyll.

## [0.2.0] — 2026-05-29

### Ajouté — nouvelles fiches produits

- **`docs/fr/conventionnel/support-tuyaux-comfort/overview.md`** —
  Support de tuyaux Comfort (modulaire 5-6 composants), brochure
  `P007-173-03`. Inclut **22 références de canules**
  (`0700-054-00`, `0700-055/056-50/51/53/54/55`, `0700-059-00/50/51/54`,
  `0700-007-50/51`, `0700-058-50`) par coloris et conditionnement.
- **`docs/fr/imagerie/vistascan-mini-easy-2-0/overview.md`** —
  Scanner de plaques chairside, technologie PCS, tailles 0-4.
- **`docs/fr/imagerie/vistascan-nano-easy/overview.md`** —
  Scanner ultracompact, tailles 0-2, scan + effacement en 1 étape.

### Ajouté — sections techniques complètes (factsheets officielles)

Sources : factsheets Dürr Dental France lues depuis la dernière page
(« Données techniques en un coup d'œil ») — confirmation explicite de
l'utilisateur que les specs précises sont à cet emplacement.

- **`docs/fr/conventionnel/silver-airline/`** — Tableau complet 12
  modèles **Primo** (61/71 l/min, 65/66 dB(A), 69×49×47 cm, 45 kg) →
  **Quattro P 20** (16 praticiens, 1032/1172 l/min, 76 dB(A),
  114×115×77 cm, 300 kg). Niveau sonore dans armoire pour Primo-Quattro.
  Source : `P007-158-03/N04`.
- **`docs/fr/conventionnel/tornado/`** — Tableau complet **NEW Tornado 1/2/4**
  : dimensions nu / avec dessiccateur / **avec capot + dessiccateur**
  (84×63×60 cm pour T1/T2), poids 32/38/49 kg (T1), niveau sonore
  **64 → 58 → 47 dB(A)** (nu / carter / armoire à 50 Hz). Source :
  `P007100308L03/T09`.
- **`docs/fr/conventionnel/power-tower/`** — Tableau **7 modèles
  Power Tower View** (VS/V 600/900 S/1200 S), dimensions
  **208 × 64 × 61 cm**, poids 265-275 kg, 53-55 dB(A) @ 35 °C, débits
  115/230 l/min. Source : `P007100194L03/N10`.
- **`docs/fr/conventionnel/cad-cam-compresseurs/`** — 4 références
  4 152-54 / 4 642-54 / 4 252-54 / 4 682-54 + table compatibilité par
  plage de pression CAM machine (5,5 → 8,5 bar selon les usineuses
  référencées dans la factsheet officielle). Source : `P007100024L02/R02`.
- **`docs/fr/conventionnel/aspiration-chirurgicale/`** (VC 65) —
  Pompe à pistons, **65/75 l/min**, dépression **910 mbar**,
  **44 dB(A)**, **35 × 33 × 37 cm**, 16 kg, bocal 2 L à gélifiant
  intégré. Source : `P007100188L03/L04`.
- **`docs/fr/conventionnel/recuperateurs-amalgame/`** — Tableaux
  complets CS 1, CAS 1, CA 1 (24 V) + CA 2 (56 dB(A), 8 kg, cassette
  90 cm³) + CA 4 (55/46 dB(A), 10 kg, cassette 600 cm³, taux 98,9 %)
  + VSA 300 S. Taux récupération TÜV Essen, agréments DIBT
  Z-64.1-15/20/22. Source : `P007-619-03/TM-dd.de`.
- **`docs/fr/conventionnel/systemes-cliniques/`** — Gamme P 6000 / 9000 /
  12000 (compresseurs cliniques) + V 6000 / 9000 / 12000 / 15000 / 18000
  (aspirations centralisées). Nouveau panneau de commande intégré +
  interface CAN + connexion VistaSoft Monitor depuis octobre 2023.
  Couvre jusqu'à 80 praticiens simultanés.
- **`docs/fr/conventionnel/canules-universelles/`** — 22 références
  produits par coloris et conditionnement (III adultes / Petito enfants /
  Protect anti-reflux / chirurgicale stérile Ø 2,5 mm /
  prophylactique aéropolissage).

- **`docs/fr/imagerie/vistavox-s/`** — Caractéristiques techniques
  complètes : générateur 50-99 kV / 1,6 kW, capteur CsI **49,5 µm**
  (135,8 × 36,4 mm) + capteur Ceph 100 µm (157,2 × 16,3 mm), FOV
  **Ø 130 × 85 mm** + 10 volumes Ø 50 × 50 mm, hauteur 1 406-2 206 mm,
  poids **180 kg** (S) / **202 kg** (Ceph), L × P 1 212 × 1 545 mm
  (S) / 1 941 × 1 615 mm (Ceph), 200-240 V / 170 W / max 2,2 kVA,
  17 + 6 programmes pano / Ceph, MAR + S-Pan + 4 fonctions IA.
  Fabriqué à Gechingen, Allemagne. Source : `P007100059L03/R05`.
- **`docs/fr/imagerie/vistacam-ix-hd-smart/`** — USB 2.0/3.0,
  **1 280 × 1 024 pixels**, **70 g** / **200 mm**, câble 2,5 m
  (rallonge 19 m via support actif USB), 3 têtes interchangeables
  Cam (blanc) / Proof (405 nm violet) / Proxi (850 nm IR), échelle
  fluorescence Proof 0-1 émail sain → > 2,5 dentine profonde. Source :
  `P007100020L03/J10`.
- **`docs/fr/imagerie/vistaray-7/`** — Structure interne du capteur
  (blindage + scintillateur Dürr + optique flexible + puce CMOS +
  absorbeur de choc), accessoires (set angulateurs + support mural /
  bras scialytique), conformité RKI, fabrication Allemagne. Source :
  `P007-670-03/C5`.
- **`docs/fr/imagerie/vistasoft-4-0/`** — Section **filtre UHD**
  (Ultra High Definition, nouveau VistaSoft 4.0, présenté **IDS 2025**,
  ajuste luminosité+contraste+netteté **région par région** sur les 4
  types intra-oral / pano / ceph / 3D-CBCT). Sources Facebook officiel
  + page UK. **6 fonctions IA inclusive** détaillées (rotation auto,
  côté inversé, qualité IQ, dents, traçage canal nerveux, Clear Pan).
  **Tableau des 21 filtres numériques classiques** (7 intra-oral +
  4 pano + 8 céphalo + 2 Proof) extrait du manuel `2110100001L03`
  (édition 2311V029).

- **`docs/fr/hygiene-chimie/hygoclave-hygopure/`** — Hygoclave 50 et
  50 Plus (chambre **17 L** / **22 L**, **484 × 493 × 642 mm**,
  **57 kg** / **61 kg**), 5 programmes 134/121 °C type B (45 → 62 min),
  charges max (5,5/6,5 kg massive), 3 modes alimentation eau, USB +
  Ethernet + PDF. DM IIb CE **0051**. Source : `P007100196L03/N11`.
- **`docs/fr/hygiene-chimie/hygobox-hygopac-emballage/`** — Hygopac
  et Hygopac View côte à côte : 550 / 900 W, 5,3 / 9 m/min, **9 / 13 mm**
  largeur soudure, 7,2 / 7,8 kg, 160 × 435 × 135 mm / 170 × 370 × 140 mm.
  Différences clés Hygopac View (écran tactile + validation + SD/réseau).
  Source : `P007100138L03/J12`.
- **`docs/fr/hygiene-chimie/hygosonic/`** — Référence `6035-50`,
  220-240 V / 280 W / IP 20, Boost +25 % / Sweep / Degas, ID 220
  (bain pour fraises) + MD 530/535 (dissolvants ciments/plâtre).
  **Sonoswiss AG** fabricant légal depuis mars 2021 (MDR EU 2017/745).
- **`docs/fr/hygiene-chimie/hygowater-traitement-eau/`** —
  ⚠️ **Statut commercial fin de vie** : vente arrêtée
  **1ᵉʳ janvier 2024** (Hygowater + Hygowater Compact). Consommables
  et pièces détachées disponibles au catalogue. Fiche conservée
  comme référence historique.
- **`docs/fr/hygiene-chimie/vector-paro/`** — **25-35 kHz**,
  réservoir **600 ml** (≈ 20 min d'autonomie à 30 ml/min), poudre
  Vector Fluid polish grain **< 10 µm**, **16 × 21,5 × 25,5 cm**,
  **2,5 kg**. Source : `P007-171-03/HK-dd.de`.

### Ajouté — fiche entreprise enrichie

- **`docs/fr/durr-dental-entreprise/overview.md`** :
  - Frise complète **1941 → 2026** (Stuttgart-Feuerbach, transfert
    Bietigheim 1954, premier compresseur sans huile 1965, VS 300 en
    1993, VistaCam 1995, VistaRay 1997, VistaScan 2002, VistaIntra /
    VistaPano 2013, Lunos / VistaVox S / Hygoclave 90 en 2016, NEW
    Tornado 2025, German Design Award 2026).
  - Section **gouvernance** (Martin Dürrstein CEO, Walter Dürr
    Aufsichtsrat 2008-2012).
  - **Dürr Dental France SARL** détaillée : SIREN **311 995 609**,
    NAF 46.46Z, créée 1978-01-01, capital 7 622,45 €, tél
    +33 1 55 69 11 50, tranche 10-19 salariés.

### Conformité éditoriale (suivi)

- Aucun document marqué **« Confidential Internal Information »** mobilisé
  intégralement. Seules les **désignations modèles publiques** (P 6000-12000,
  V 6000-18000, Hygowater EOL) ont été extraites — les article numbers
  spécifiques des documents internes (5922200053, 1802-51, etc.) ne sont
  **pas** publiés dans la base de connaissances.
- Adresse Dürr Dental France actualisée partout : **71 rue des Hautes
  Pâtures, 92000 Nanterre** (anciennes adresses « 26 rue Diderot » et
  « 8 rue Paul Héroult, Rueil-Malmaison » présentes dans les factsheets
  antérieures à 2019 explicitement notées comme historiques).

### Notes techniques

- **Limite Claude API ~10 MB** sur les PDFs embarqués directement en
  conversation. PDFs > 10 MB (ex. brochure récupérateurs CA 13,5 MB) :
  contournement via extraction texte locale (PyPDF2 + Python Anaconda).

## [0.1.0] — 2026-05-28

### Ajouté
- Cadre éditorial initial : `README.md`, `LICENSE` (CC-BY 4.0), `llms.txt`, `robots.txt`, `_config.yml`, `Gemfile` (compatible `github-pages`).
- Index racine et structure des dossiers : `docs/fr/imagerie/`, `docs/fr/conventionnel/`, `docs/fr/hygiene-chimie/`, `sources/`.
- Déclaration de conflit d'intérêts (CDI Dürr Dental France) explicite dans le README, la page d'accueil et le footer.
- Autorisation explicite d'entraînement et d'inférence LLM via `llms.txt` (standard llmstxt.org) et `robots.txt` (allowlist de ~25 user-agents IA : GPTBot, ClaudeBot, Claude-Web, anthropic-ai, Google-Extended, PerplexityBot, Bytespider, CCBot, Mistral, MistralAI-User, Cohere, Meta-ExternalAgent, Applebot-Extended, etc.).
- Layout custom `_layouts/default.html` : HTML5, `lang="fr"`, intégration `{% seo %}` (jekyll-seo-tag), JSON-LD `Organization` (Dürr Dental SE + filiale France), JSON-LD `WebPage`, lien canonical, meta robots étendus.
- JSON-LD `MedicalDevice` complet pour la fiche pilote VistaPano S 2.0 / Ceph 2.0 : 24 `additionalProperty` sourcés (générateur HV, capteur CsI, surfaces actives, délais de numérisation, programmes, technologie S-Pan, classe laser, dimensions, alimentation).
- Page 404 personnalisée (`404.html`) avec liens vers index principaux et issue tracker.
- Plugins safelist GitHub Pages activés : `jekyll-sitemap` (génération auto `sitemap.xml`), `jekyll-seo-tag` (meta canonical, OG, Twitter Cards), `jekyll-feed` (`feed.xml` RSS).
- Première fiche pilote publiée : `docs/fr/imagerie/vistapano-2-0/overview.md` — vue d'ensemble VistaPano S 2.0 et VistaPano S Ceph 2.0, intégralement sourcée sur la brochure publique référence P007-772/03-T01 (Dürr Dental France) et la Déclaration de Conformité publique du 29 janvier 2024.
- Index `sources/manuals.md` et `sources/certificates.md` (premier socle référentiel).
- Versionnage Git : tag `v0.1.0`.

### Conformité éditoriale
- Aucune citation ni comparaison concurrentielle (règle d'or Dürr respectée).
- Aucun document marqué Internal Use / Strictly Confidential mobilisé.
- Aucune donnée patient / praticien / cabinet identifiable.

### Workflow non-contestable — validation déterministe
- **`scripts/validate.py`** : script Python de validation déterministe du dépôt. Vérifications automatiques :
  - règle d'or Dürr (regex de ~20 marques concurrentes bannies + exception Sidexis hors contexte Image Bridge)
  - pas de mention `Internal Use` / `Strictly Confidential` / `Sales Information interne`
  - pas de donnée personnelle praticien (regex `Dr|Dre|Pr + Nom propre`)
  - frontmatter YAML obligatoire avec champs requis (`layout`, `title`, `description`, `lang`, `permalink`, `last_factual_review`, `license`)
  - `schema_type` parmi liste blanche Schema.org
  - `source_documents` : chaque entrée doit avoir `url` OU `note` explicite
  - blocs JSON-LD inline doivent être du JSON valide
  - liens internes Markdown résolvables
  - sortie : rapport humain avec code retour 0 (clean) / 1 (erreurs)
- **`.pre-commit-config.yaml`** : 4 catégories de hooks (sanity, markdownlint-cli, `validate-repo` local, `forbid-pdf-commits`). Installation : `pre-commit install` une seule fois.
- **`.github/workflows/ci.yml`** : ajout du job `validate-repo` (`python scripts/validate.py --warn-as-error`) — bloque tout PR non-conforme.
- **`docs/WORKFLOW.md`** : procédure éditoriale en 10 étapes, des pré-requis à la correction d'erreur. Garanties procédurales tabulées en synthèse.
- **`STATEMENT_OF_INTEGRITY.md`** : déclaration publique des 8 engagements procéduraux du mainteneur (identité + CDI, périmètre sources, règle d'or, garanties techniques vérifiables, procédure de correction, licence, non-renonciation droits fabricant, recours). Sert de référence opposable en cas de contestation.
- **`CONTRIBUTING.md`** : section *Validation déterministe pré-commit* avec instructions d'installation et liste des hooks.
- **`README.md`** : liens enrichis vers WORKFLOW + STATEMENT.

### Sourçage renforcé (URLs directes obligatoires)
- **Fiche pilote VistaPano S 2.0 — section *Sources publiques* restructurée** : 4 tableaux par catégorie (pages officielles, notices `qr.duerrdental.com`, brochure commerciale, conformité réglementaire) avec **URL publique directe par source**. Ajout des URLs `qr.duerrdental.com/2208100006` (notice installation) et `qr.duerrdental.com/2208100028` (notice utilisation), URL page produit FR officielle confirmée (`duerrdental.com/fr/FR/produits/imagerie/diagnostic-extra-oral/vistapano-s-20/`), URL Centre de téléchargements FR, URL Eudamed avec recherche fabricant pré-filtrée.
- **`source_documents` frontmatter restructuré en YAML enrichi** : `title`, `url`, `type`, `reference`, `language`, `date`, `note` par source — exploitable pour génération future de JSON-LD `Citation` et pour inspection automatisée.
- **Section *Pérennité Wayback Machine*** ajoutée à la fiche pilote : 3 URLs archivées pré-renseignées pour citabilité long terme.
- **`sources/manuals.md`** mis à jour avec les références VistaPano S 2.0 et URL directes `qr.duerrdental.com`.
- **`sources/certificates.md`** mis à jour avec le numéro de certificat complet (`10877-2017-CE-KOR-NA-PS Rev 3.0`) et la procédure de récupération de la DoC via Centre de téléchargements et Eudamed.
- **`_drafts/_template_fiche_produit.md`** mis à jour : `source_documents` en format YAML structuré obligatoire, section *Sources publiques* avec 6 tableaux standards + Wayback.
- **`CONTRIBUTING.md`** complété : règle non-négociable « URL directe obligatoire par source » + patterns d'URL standards Dürr Dental (notices, page produit FR/EN, Centre de téléchargements, Eudamed, FDA 510(k)) + procédure d'archivage Wayback + note sur l'interdiction de committer les PDF originaux (propriété intellectuelle fabricant).

### Intégrité et durcissement
- `.github/CODEOWNERS` : revue obligatoire du mainteneur pour les fichiers critiques (`_data/`, `_layouts/`, `llms.txt`, `robots.txt`, `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `.well-known/`, fiches réglementaires).
- `.github/dependabot.yml` : mises à jour hebdomadaires automatiques (Bundler + GitHub Actions), labellisées, format Conventional Commits.
- `docs/GITHUB_HARDENING.md` : checklist d'activation manuelle post-push (2FA, branch protection sur `main`, tag protection sur `v*`, commits signés SSH/GPG, secret scanning, push protection, Pages HTTPS forcé). 9 sections avec modèle de menace explicite.
- `SECURITY.md` enrichi : section *Intégrité du contenu* listant les protections par couche, modèle de menace explicite (ce qui est couvert / ce qui ne l'est pas, avec attention aux forks et au re-hébergement CC-BY 4.0).

### Polish final
- `favicon.svg` : monogramme DD pour onglet navigateur et signal crawl.
- `.well-known/security.txt` (RFC 9116) : emplacement standard pointant vers SECURITY.md et les advisories GitHub.
- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1 — version française officielle).
- Badges README : licence, CI status, GitHub Pages, langue, Conventional Commits, CDI déclaré.
- Layout enrichi : `<link rel="icon">` favicon SVG, `<link rel="alternate" hreflang="fr|x-default">` (préparation multilingue future), `<link rel="me">` vers profil GitHub (identité décentralisée), `<meta property="og:locale" content="fr_FR">`.
- `_config.yml` : `include: [.well-known]` pour que Jekyll publie le dossier (sinon ignoré par défaut).

### Couche structurelle et gouvernance (anti-refactoring futur)
- **Centralisation `_data/durr.yml`** : source de vérité unique pour les données organisationnelles Dürr Dental SE et filiale France, les Notified Bodies, les règlements et bases publiques. Le layout consomme ces données pour générer les JSON-LD `Organization` — évite la duplication et la dérive entre fiches.
- **JSON-LD `BreadcrumbList`** auto-généré à partir du frontmatter `breadcrumbs` de chaque page.
- **JSON-LD `FAQPage`** embarqué dans la fiche pilote VistaPano S 2.0 (6 Q&A structurées).
- **JSON-LD `WebSite` avec `SearchAction`** dans le layout (signal sitelinks search).
- **Glossaire `docs/fr/glossaire.md`** : 25+ termes (MDR, MDD, classes DM, UDI, Eudamed, DICOM, TWAIN, VDDS, BDW, CBCT, OPG, FOV, SMV, stitching, CsI:TI, CMOS, kV/mA, CEI 80001-1, DIN 6868-157, etc.) — référencé par toutes les fiches futures.
- **Gabarit de fiche** `_drafts/_template_fiche_produit.md` : frontmatter complet, JSON-LD MedicalDevice template, sections obligatoires, checklist pré-commit.
- **`CONTRIBUTING.md`** : conventions de nommage ASCII, structure de dossiers, frontmatter standard, conventions JSON-LD par page, style éditorial (verbatim, sourçage, format Q&A), workflow Git Conventional Commits, versioning SemVer.
- **`SECURITY.md`** : politique de signalement (advisory privé, correction erreur factuelle critique sous 7 jours).
- **`humans.txt`** : déclaration de l'équipe et du conflit d'intérêts.
- **`.gitattributes`** : normalisation des fins de ligne (LF) et déclaration Linguist `linguist-documentation`.
- **`.editorconfig`** : charset UTF-8, LF, indentation 2 espaces.
- **`.github/ISSUE_TEMPLATE/`** : 3 formulaires Issue Forms (correction factuelle, ajout de source publique, nouvelle fiche produit) + `config.yml` (liens contact alternatifs : duerrdental.com, qr.duerrdental.com, Eudamed).
- **`.github/PULL_REQUEST_TEMPLATE.md`** : checklist éditoriale + checklist technique (frontmatter, JSON-LD, FAQ, sources).
- **`.github/workflows/ci.yml`** : 3 jobs CI — lychee (vérification hebdomadaire et à chaque push des liens externes), markdownlint-cli2, Jekyll build strict.
- **`.markdownlint-cli2.yaml`** : règles Markdown adaptées (HTML inline autorisé pour les blocs JSON-LD, URLs brutes autorisées).
- **Layout enrichi** : meta `author`, meta `referrer` `strict-origin-when-cross-origin`, navigation breadcrumb HTML rendue, badge « CDI déclaré » dans le footer, affichage de `last_factual_review` en pied de chaque page.
- **`feed.xml`** RSS auto-généré (plugin jekyll-feed).
