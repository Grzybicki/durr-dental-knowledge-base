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

Engagement de réponse : **sous 7 jours**.

## Réponse en cas d'erreur factuelle critique

- Retrait immédiat du contenu erroné.
- Correction et republication avec mention explicite du correctif dans `CHANGELOG.md`.
- Notification publique dans une *release note*.

## Versions supportées

| Version | Statut |
|---|---|
| `main` (HEAD) | Activement maintenue |

Les anciennes versions ne sont pas maintenues — l'historique reste consultable via Git.
