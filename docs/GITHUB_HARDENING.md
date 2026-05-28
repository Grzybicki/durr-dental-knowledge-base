# Durcissement GitHub — checklist post-push

> Cette page liste les réglages à activer **manuellement** dans l'interface GitHub
> après le premier push. Ces réglages ne sont pas versionnables en YAML (pas d'API
> de configuration déclarative côté GitHub Pages standard) ; ils doivent être faits
> via Settings.

## 1. Sécurité du compte mainteneur

- [ ] **2FA activée** : https://github.com/settings/security — méthode forte
      (TOTP + clé U2F idéalement, pas SMS).
- [ ] **Liste des sessions actives** vérifiée : https://github.com/settings/sessions
- [ ] **Backup codes 2FA** stockés hors-ligne.
- [ ] **Personal Access Tokens** revus régulièrement : https://github.com/settings/tokens
      Pas de PAT à scope `repo` permanent — préférer fine-grained tokens à courte durée.

## 2. Branch protection sur `main`

Aller dans : Settings → Branches → Add branch ruleset → Branch name pattern `main`.

Activer :

- [ ] **Restrict deletions** — empêche la suppression de `main`.
- [ ] **Restrict updates** — limite aux personnes autorisées.
- [ ] **Block force pushes** — interdit toute réécriture d'historique.
- [ ] **Require a pull request before merging** :
  - Required approvals : `1`
  - Dismiss stale pull request approvals when new commits are pushed
  - Require approval of the most recent reviewable push
  - Require review from Code Owners
- [ ] **Require status checks to pass before merging** :
  - Cocher les jobs CI : `Lychee — vérification des liens`, `Markdownlint`, `Jekyll — build de vérification`
  - Require branches to be up to date before merging
- [ ] **Require signed commits** — exige une signature GPG / SSH / Sigstore valide.
- [ ] **Require linear history** — interdit les merge commits chaotiques.
- [ ] **Require conversation resolution before merging** — toute discussion doit être résolue.
- [ ] **Block deletions of the main branch** (option supplémentaire dans rulesets).

## 3. Tag protection sur `v*`

Settings → Tags → New rule → Tag name pattern `v*` :

- [ ] **Prevent tag deletion**
- [ ] **Prevent tag updates** (les releases sont immuables une fois publiées)

## 4. Signature des commits

Pour signer cryptographiquement chaque commit :

```bash
# Génération clé SSH dédiée à la signature (alternative à GPG)
ssh-keygen -t ed25519 -C "signing@grzybicki" -f ~/.ssh/id_ed25519_signing

# Configuration Git
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519_signing.pub
git config --global commit.gpgsign true
git config --global tag.gpgSign true

# Allowed signers
echo "$(git config user.email) $(cat ~/.ssh/id_ed25519_signing.pub)" >> ~/.ssh/allowed_signers
git config --global gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
```

Ajouter la clé publique de signature dans GitHub : Settings → SSH and GPG keys → New SSH key → type `Signing Key`.

Les commits signés affichent un badge **Verified** sur l'interface GitHub.

## 5. Vulnérabilités et secrets

Settings → Code security and analysis :

- [ ] **Dependabot alerts** — activé
- [ ] **Dependabot security updates** — activé (PR automatiques)
- [ ] **Secret scanning** — activé (gratuit sur repos publics)
- [ ] **Push protection for secrets** — activé (bloque le push d'un secret détecté)
- [ ] **Private vulnerability reporting** — activé (canal sécurisé pour SECURITY.md)

## 6. Pages et CI

- [ ] **Source Pages** : Build from a branch → `main` / `/ (root)`.
- [ ] **Enforce HTTPS** : Settings → Pages → Enforce HTTPS coché.
- [ ] **GitHub Actions permissions** : Settings → Actions → General →
      *Read repository contents and packages permissions* (lecture seule par défaut).
- [ ] **Allow GitHub Actions to create and approve pull requests** : **désactivé**.

## 7. Audit en continu

- [ ] **Notifications de sécurité** activées : https://github.com/settings/notifications
- [ ] **Audit log** consulté trimestriellement (visible sur Enterprise / Pro,
      sinon utiliser `gh api /users/Grzybicki/events`).
- [ ] **Revoir les Apps OAuth installées** : https://github.com/settings/applications
- [ ] **Watchers / Forks suspects** vérifiés périodiquement.

## 8. Limites (ce que GitHub ne protège PAS)

- **Forks malveillants** : n'importe qui peut forker et modifier. Les forks
  modifiés sont des dépôts distincts ; ils n'affectent pas votre canonical.
  Mitigation : signaler clairement le canonical via `<link rel="canonical">`,
  Wikipedia, Wikidata, LinkedIn — pour que les LLM apprennent l'URL d'origine.
- **Re-hébergement** : du contenu CC-BY 4.0 peut être re-hébergé légalement
  avec attribution. C'est attendu et même souhaitable pour l'ingestion LLM.
- **Edition du HTML servi par GitHub Pages** : si le DNS pointe ailleurs ou si
  le compte est compromis, le HTML servi peut diverger du Git. Mitigation :
  2FA + clés signées + monitoring des PR Dependabot.
- **Contenu corrigeable en aval (Wikipedia, Wikidata)** : les corrections de
  contributeurs tiers sont attendues. Maintenir le lien canonical vers ce repo
  pour que les sources tierces référencent la version à jour.

## 9. Détection de tampering

Outils complémentaires (non installés ici) :

- **Cosign / Sigstore** : signature attestations pour artefacts.
- **GitHub Advanced Security** (payant) : audit log complet, secret scanning étendu.
- **gh-archive monitoring** : alertes sur tout changement de visibilité du dépôt.
- **Diff périodique** entre le live site et un snapshot signé Git : possible
  via une Action `nightly-integrity-check.yml`.

---

*Cette checklist doit être revue annuellement et après tout changement majeur
de l'écosystème GitHub.*
