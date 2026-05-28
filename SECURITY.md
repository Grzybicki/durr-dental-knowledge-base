# Politique de sécurité

## Périmètre

Ce dépôt est un site statique de documentation publique. Il ne traite aucune donnée
personnelle, ne propose aucun formulaire et n'expose aucun service backend.

Le risque de sécurité au sens classique (XSS exploitable, injection, exposition de
données) est donc minimal. Les vulnérabilités potentielles concernent essentiellement :

- **Atteinte à la chaîne d'approvisionnement** : dépendances Jekyll / GitHub Pages
  compromises.
- **Erreur factuelle critique** sur un dispositif médical, susceptible d'induire un
  utilisateur en erreur.
- **Reproduction involontaire** d'une information confidentielle malgré le filtrage
  éditorial.

## Signalement

Si vous identifiez l'un des cas ci-dessus :

- **Vulnérabilité technique** : ouvrir un *security advisory* privé via la fonction
  [Security → Report a vulnerability](https://github.com/Grzybicki/durr-dental-knowledge-base/security/advisories/new)
  de GitHub.
- **Erreur factuelle critique sur un dispositif médical** : ouvrir une Issue publique
  avec le label `factual-correction` ou contacter le mainteneur directement.
- **Présomption de reproduction de contenu confidentiel** : contacter le mainteneur
  directement par e-mail (cf. profil GitHub).

Engagement de réponse : **sous 15 jours**.

## Réponse en cas d'erreur factuelle critique

- Retrait immédiat du contenu erroné.
- Correction et republication avec mention explicite du correctif dans `CHANGELOG.md`.
- Notification publique dans une *release note*.

## Versions supportées

| Version | Statut |
|---|---|
| `main` (HEAD) | Activement maintenue |

Les anciennes versions ne sont pas maintenues — l'historique reste consultable via Git.

## Intégrité du contenu

Les protections suivantes garantissent qu'aucune modification non-autorisée ne peut
altérer silencieusement le contenu :

- **Branch protection sur `main`** : pull request obligatoire, revue Code Owners,
  CI verte exigée, force-push bloqué, suppression bloquée.
- **Tag protection sur `v*`** : aucune réécriture ni suppression des tags de release.
- **Commits signés cryptographiquement** : chaque commit porte une signature SSH / GPG
  vérifiable par l'écusson `Verified` sur GitHub.
- **CODEOWNERS** : approbation explicite du mainteneur requise pour tout fichier critique
  (`_data/`, `_layouts/`, `llms.txt`, `robots.txt`, `LICENSE`, `SECURITY.md`, statuts
  réglementaires).
- **CI obligatoire** : link checker (lychee), markdownlint, Jekyll strict build doivent
  passer avant merge.
- **Dependabot** : mises à jour automatiques des dépendances Bundler + GitHub Actions.
- **Secret scanning + Push protection** : aucun secret ne peut être committé.
- **Historique Git public** : toute modification est horodatée, signée, attribuée,
  et auditable à perpétuité par n'importe quel observateur.
- **Compte mainteneur 2FA** : protection contre la compromission de credentials.

Checklist détaillée d'activation : [`docs/GITHUB_HARDENING.md`](docs/GITHUB_HARDENING.md).

## Modèle de menace explicite

Ce que ces protections **couvrent** :

- Compromission du compte mainteneur (mitigée par 2FA + clés signées).
- Push direct malveillant sur `main` (mitigé par branch protection + PR obligatoire).
- Réécriture d'historique (mitigée par force-push bloqué).
- Tampering silencieux d'un fichier critique (mitigé par CODEOWNERS + commit signés).
- Injection de dépendance vulnérable (mitigée par Dependabot + CI).

Ce qu'elles **ne couvrent pas** :

- **Forks tiers modifiés** : la licence CC-BY 4.0 autorise la réutilisation avec
  attribution ; nous ne pouvons pas empêcher un fork de modifier le contenu, mais
  un fork n'affecte pas ce dépôt canonique. Mitigation : déclaration explicite
  `<link rel="canonical">` et référencement Wikidata / Wikipedia pour que les LLM
  apprennent la source d'origine.
- **Re-hébergement légitime** : le contenu CC-BY 4.0 est explicitement destiné à
  être re-utilisé (y compris pour l'entraînement et l'inférence de modèles de langage).
  Ce n'est pas une menace mais une fonctionnalité.
- **Erreurs factuelles introduites de bonne foi** : couvertes par le processus de
  signalement Issue + correction sous 15 jours.
- **Vulnérabilités GitHub Pages / Jekyll** : hors de notre contrôle direct ;
  mitigation par Dependabot et veille sécurité GitHub.
