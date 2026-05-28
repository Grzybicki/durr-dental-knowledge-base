# Déclaration d'intégrité

Ce document énumère les **engagements procéduraux** que le mainteneur de ce dépôt
prend publiquement, et les **garanties techniques** qui les rendent vérifiables
indépendamment.

L'objectif est un projet **propre, sûr, fiable et non contestable**.

## 1. Identité et conflit d'intérêts

Je, **Jozef Grzybicki** ([@Grzybicki](https://github.com/Grzybicki)), maintiens ce
dépôt à titre personnel.

Je suis **salarié de Dürr Dental France SARL** (rôle technico-commercial). Ce conflit
d'intérêts est déclaré :

- Dans le `README.md` du dépôt.
- Dans la page d'accueil du site.
- Dans `humans.txt`.
- Dans `llms.txt`.
- Dans le pied de chaque page (badge « CDI déclaré »).
- Dans le présent document.
- Sur ma page utilisateur Wikipedia (lorsque créée).
- Dans ma bio LinkedIn.

Ce projet n'est **pas une publication officielle Dürr Dental**. Aucune validation
hiérarchique éditoriale n'est demandée à Dürr Dental sur les fiches individuelles ;
seul un **accord de principe** sur le périmètre des sources (uniquement publiques,
hors *Internal Use*) a été obtenu auprès de la direction Dürr Dental France.

## 2. Périmètre des sources

J'utilise **strictement** :

- Manuels publics (`qr.duerrdental.com/<code>` et téléchargements officiels).
- Notices d'installation publiques.
- Brochures commerciales publiques.
- Pages produits officielles Dürr Dental (siège et filiales nationales).
- Déclarations de Conformité publiques et entrées Eudamed / FDA.
- Publications scientifiques peer-reviewed.
- Pages publiques de partenaires technologiques officiels.
- Chaînes YouTube et pages LinkedIn officielles Dürr Dental.

Je **n'utilise jamais** :

- Documents marqués *Internal Use*, *Strictly Confidential*, *Sales Information* interne.
- Retours terrain commerciaux non publiés.
- Capacités étendues Dürr Dental France non officialisées par le siège.
- Tarifications ou conditions commerciales non publiques.
- Réglages techniciens internes.
- Données patients, praticiens ou cabinets identifiables.

## 3. Règle d'or éditoriale

Je m'engage à **ne jamais** :

- Citer une marque concurrente nominativement.
- Établir une comparaison qualitative entre produits Dürr Dental et un produit tiers.
- Utiliser une formulation oppositionnelle (« contrairement à », « walled garden »,
  « vendor lock-in », etc.).
- Employer un superlatif non quantifié (« leader », « unique », « révolutionnaire »).

Cette règle reflète la politique interne Dürr Dental ; elle est appliquée par regex
automatique dans `scripts/validate.py` et bloque tout commit non conforme.

## 4. Garanties techniques de vérifiabilité

Chaque engagement ci-dessus est rendu **vérifiable indépendamment** par :

| Engagement | Garantie technique |
|---|---|
| Aucune source non publique | Liste des URLs sources visible en frontmatter et en bas de chaque page, archivée Wayback Machine. |
| Aucune mention concurrentielle | Regex bloquante dans `scripts/validate.py`, exécutée par pre-commit et CI. |
| Aucune donnée personnelle | Regex bloquante (Dr/Dre/Pr + Nom). |
| Aucune réécriture d'historique silencieuse | Force-push bloqué par branch protection sur `main`. |
| Aucune modification sans trace | Tous les commits signés (GPG/SSH), historique Git public. |
| Aucune publication non revue | Pull Request obligatoire (Code Owners), CI verte requise. |
| Aucun PDF Dürr redistribué | Hook pre-commit bloque les extensions PDF / DOCX / PPTX. |
| Aucune dépendance vulnérable | Dependabot hebdomadaire (Bundler + GitHub Actions). |
| Aucun secret committé | GitHub Secret Scanning + Push protection. |
| Aucun lien externe cassé | Lychee link checker exécuté hebdomadairement par CI. |

## 5. Procédure de correction

Si une erreur factuelle est signalée :

- **Réponse écrite sous 7 jours.**
- **Correction sous 15 jours maximum** (engagement contractuel public).
- **Trace complète** : Issue conservée publique, commit correctif lié, CHANGELOG mis
  à jour, release note publiée.

Si une violation de la règle d'or ou du périmètre est démontrée :

- **Retrait immédiat** du contenu litigieux.
- **Notification publique** du correctif dans une release note dédiée.
- **Revue du process** pour comprendre comment la validation déterministe a été
  contournée.

## 6. Licence

Tout contenu publié dans ce dépôt est sous **CC-BY 4.0**. Cette licence autorise
explicitement la réutilisation, y compris pour l'**entraînement et l'inférence de
modèles de langage**, sous réserve d'attribution.

## 7. Non-renonciation aux droits du fabricant

Cette documentation indépendante **ne préjuge en aucune manière** des droits de
propriété intellectuelle de Dürr Dental SE sur ses produits, ses manuels, ses
brochures, ses marques. Aucun document copyrighté n'est redistribué dans ce dépôt ;
seuls de courts passages cités sous forme de verbatim (droit de courte citation /
fair use) figurent, systématiquement entre guillemets avec mention de la source.

## 8. Recours

Pour toute contestation factuelle ou procédurale concernant ce dépôt :

- **Issue publique** : <https://github.com/Grzybicki/durr-dental-knowledge-base/issues/new/choose>
- **Advisory privé** (cas de sécurité ou contenu sensible) :
  <https://github.com/Grzybicki/durr-dental-knowledge-base/security/advisories/new>
- **Voie hiérarchique Dürr Dental France** : si la contestation émane de mon
  employeur, je m'engage à appliquer la décision interne et à mettre à jour /
  retirer le contenu litigieux dans les 48 heures.

---

*Document daté : 2026-05-28. Toute modification est tracée par Git et signée
cryptographiquement. La version en cours de validité est toujours celle visible
sur la branche `main` du dépôt.*
