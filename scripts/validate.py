#!/usr/bin/env python3
"""
validate.py — vérifications déterministes pré-commit / CI

Pour chaque fichier Markdown / YAML / HTML du dépôt, vérifie :

1.  Frontmatter YAML présent et conforme (titres, schema_type, source_documents, etc.)
2.  Aucune mention de marque concurrente (règle d'or Dürr Dental)
3.  Aucune mention « Internal Use » / « Strictly Confidential » / « Sales Information »
4.  Aucune donnée patient / praticien / cabinet identifiable (regex Dr/Dre [Nom])
5.  Chaque entrée de `source_documents` possède une URL OU une note explicite de provenance
6.  Les blocs JSON-LD inline (<script type="application/ld+json">) sont du JSON valide
7.  Les liens internes Markdown existent

Sortie : rapport humain + code de retour 0 (clean) / 1 (errors)
Usage  : python scripts/validate.py [--root <chemin>]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML required. Install with: python -m pip install pyyaml",
        file=sys.stderr,
    )
    sys.exit(2)


# ------------------------------------------------------------------
# Configuration des règles
# ------------------------------------------------------------------

# Marques concurrentes interdites (règle d'or Dürr). Liste non exhaustive — à
# enrichir au fil des observations. Tout match déclenche une erreur bloquante.
BANNED_COMPETITOR_NAMES = [
    r"\bPlanmeca\b",
    r"\bRomexis\b",
    r"\bPearl\b",
    r"\bOverjet\b",
    r"\bDiagnocat\b",
    r"\bVatech\b",
    r"\bDexis\b",
    r"\bCarestream\b",
    r"\bDTX Studio\b",
    r"\bSirona\b",
    r"\bEnvista\b",
    r"\bNobel Biocare\b",
    r"\bMyRay\b",
    r"\bCefla\b",
    r"\bWoodpecker\b",
    r"\bVisiodent\b",
    r"\bJulie\b",
    r"\bLogosw\b",
    # DBSWin (DBSWIN) = logiciel Dürr historique, prédécesseur de VistaSoft.
    # Citable comme tel — chemin de migration officiel documenté (manuel public §5.4, DBSWin >= 5.9).
]

# Exceptions autorisées (mentions techniques non-comparatives, cf. audit 17)
# Si un nom interdit apparaît dans une phrase qui contient une de ces clés,
# le warning devient WARN au lieu d'ERROR. À utiliser parcimonieusement.
WHITELISTED_TECHNICAL_CONTEXTS = [
    r"Image Bridge",  # cohabitation Sidexis documentée dans le manuel public
    r"Patient Bridge",
    r"qr\.duerrdental\.com",
    r"manuel public",
]

# Sidexis = exception explicite du manuel VistaSoft (Image Bridge)
SIDEXIS_EXCEPTION_PATTERN = re.compile(r"Sidexis", re.IGNORECASE)

# Mentions de documents internes interdites
BANNED_INTERNAL_MARKERS = [
    r"Internal Use",
    r"Strictly Confidential",
    r"Sales Information.*Internal",
    r"Confidentiel interne",
    r"Usage interne",
    r"For internal use",
    r"À usage interne",
]

# Fichiers de gouvernance où les mentions BANNED_INTERNAL_MARKERS sont attendues
# (ces fichiers définissent ou rappellent la règle, ils ne sont pas des fuites)
META_GOVERNANCE_FILES = {
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "STATEMENT_OF_INTEGRITY.md",
    "WORKFLOW.md",
    "GITHUB_HARDENING.md",
    "PULL_REQUEST_TEMPLATE.md",
    "_template_fiche_produit.md",
    "validate.py",
    "README.md",
    "CODE_OF_CONDUCT.md",
    "factual-correction.yml",
    "source-update.yml",
    "new-product-page.yml",
    "config.yml",
}

# Mots-clés indiquant que la ligne est une MENTION META de la règle
# (pas une fuite). Si l'un de ces mots apparaît dans la ligne, on rétrograde.
META_MENTION_KEYWORDS = [
    r"\binterdit",
    r"\binterdite",
    r"\binterdites",
    r"\binterdits",
    r"\binterdiction",
    r"\bbanni",
    r"\bbannie",
    r"\bbannies",
    r"\bbannis",
    r"\bne pas\b",
    r"\baucun\b",
    r"\baucune\b",
    r"\bsans\b",
    r"\bjamais\b",
    r"\bno\s+internal",
    r"\bforbidden",
    r"\bblock",
    r"\bfilter",
    r"\bregex",
    r"\brule",
    r"\brègle",
    r"\bexclu",
    r"\bexclue",
    r"\bn'utilise jamais",
    r"\bdoes not contain",
    r"\bdoit pas",
    r"\bdo not",
    r"\bne contient pas",
    r"non mobilis",
    r"non reproduit",
    r"strict.{0,30}public",
]

# Patterns de données personnelles (praticiens / cabinets identifiables)
# Tolère Dr/Dre dans les termes communs (« Dr CBCT », etc.) en exigeant un mot
# capitalisé suivant. Liste blanche pour les titres génériques.
PII_PATTERN = re.compile(
    r"\b(Dr|Dre|Docteur|Dr\.|Professeur|Pr\.|Pr)\.?\s+(?!Dental|Test|TEST|Anonyme|Demo|Exemple)[A-Z][a-zà-öù-ÿ]+",
    re.UNICODE,
)

# Schémas Schema.org acceptés pour `schema_type` du frontmatter
ALLOWED_SCHEMA_TYPES = {
    "MedicalDevice",
    "SoftwareApplication",
    "Product",
    "FAQPage",
    "DefinedTermSet",
    "WebPage",
    "Article",
    "TechArticle",
    "Dataset",
    "Organization",
}

# Champs obligatoires du frontmatter pour les pages de docs/
REQUIRED_FRONTMATTER_FIELDS_DOCS = {
    "layout",
    "title",
    "description",
    "lang",
    "permalink",
    "last_factual_review",
    "license",
}

# Extensions à valider
TARGET_EXTENSIONS = {".md", ".html"}

# Dossiers à exclure
EXCLUDED_DIRS = {".git", "node_modules", "_site", "vendor", ".jekyll-cache", "_drafts"}


# ------------------------------------------------------------------
# Structure de rapport
# ------------------------------------------------------------------

@dataclass
class Issue:
    path: Path
    severity: str  # "ERROR" or "WARN"
    rule: str
    message: str
    line: int | None = None


@dataclass
class Report:
    issues: list[Issue] = field(default_factory=list)
    files_scanned: int = 0
    pages_with_frontmatter: int = 0

    def add(self, issue: Issue) -> None:
        self.issues.append(issue)

    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "ERROR"]

    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "WARN"]


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
JSONLD_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def split_frontmatter(content: str) -> tuple[dict | None, str]:
    """Sépare le frontmatter YAML et le corps Markdown."""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return None, content
    try:
        data = yaml.safe_load(m.group(1)) or {}
        return data, content[m.end():]
    except yaml.YAMLError as e:
        raise ValueError(f"frontmatter YAML invalide : {e}")


def get_line_number(content: str, offset: int) -> int:
    return content.count("\n", 0, offset) + 1


# ------------------------------------------------------------------
# Règles de validation
# ------------------------------------------------------------------

def check_competitor_names(report: Report, path: Path, body: str) -> None:
    """Règle d'or Dürr : aucun nom de concurrent."""
    for pattern in BANNED_COMPETITOR_NAMES:
        for m in re.finditer(pattern, body, re.IGNORECASE):
            # Tolérance : si le match apparaît dans une ligne qui contient
            # un contexte technique whitelisté, on rétrograde en WARN.
            line_start = body.rfind("\n", 0, m.start()) + 1
            line_end = body.find("\n", m.end())
            if line_end < 0:
                line_end = len(body)
            line_text = body[line_start:line_end]
            severity = "ERROR"
            for ctx in WHITELISTED_TECHNICAL_CONTEXTS:
                if re.search(ctx, line_text):
                    severity = "WARN"
                    break
            report.add(Issue(
                path=path,
                severity=severity,
                rule="rule-of-gold",
                message=f"mention concurrent interdite : « {m.group(0)} » — règle d'or Dürr",
                line=get_line_number(body, m.start()),
            ))

    # Sidexis : autorisé uniquement dans le contexte Image Bridge
    for m in SIDEXIS_EXCEPTION_PATTERN.finditer(body):
        line_start = body.rfind("\n", 0, m.start()) + 1
        line_end = body.find("\n", m.end())
        if line_end < 0:
            line_end = len(body)
        line_text = body[line_start:line_end]
        if not re.search(r"Image Bridge|cohabit", line_text, re.IGNORECASE):
            report.add(Issue(
                path=path,
                severity="WARN",
                rule="rule-of-gold-sidexis",
                message="mention 'Sidexis' hors contexte Image Bridge — autorisé uniquement pour la cohabitation technique documentée",
                line=get_line_number(body, m.start()),
            ))


def check_internal_markers(report: Report, path: Path, body: str) -> None:
    """Mentions de documents internes interdites.

    Tolérance forte : les fichiers de gouvernance (CHANGELOG, CONTRIBUTING, etc.)
    mentionnent la règle elle-même ; les pages contenant un mot-clé de négation
    sur la même ligne sont également tolérées (mention META de la règle).
    """
    # Fichiers de gouvernance : on saute totalement
    if path.name in META_GOVERNANCE_FILES:
        return

    for pattern in BANNED_INTERNAL_MARKERS:
        for m in re.finditer(pattern, body, re.IGNORECASE):
            # Vérifier le contexte ligne pour détecter une mention META
            line_start = body.rfind("\n", 0, m.start()) + 1
            line_end = body.find("\n", m.end())
            if line_end < 0:
                line_end = len(body)
            line_text = body[line_start:line_end]
            is_meta_mention = any(
                re.search(kw, line_text, re.IGNORECASE) for kw in META_MENTION_KEYWORDS
            )
            if is_meta_mention:
                # Mention META de la règle, pas une fuite — on saute
                continue
            report.add(Issue(
                path=path,
                severity="ERROR",
                rule="internal-use-leak",
                message=f"mention 'Internal Use' interdite : « {m.group(0)} »",
                line=get_line_number(body, m.start()),
            ))


def check_pii(report: Report, path: Path, body: str) -> None:
    """Données personnelles : praticiens / cabinets identifiables."""
    # Ne pas vérifier le glossaire / CONTRIBUTING (ils mentionnent des exemples)
    if path.name in {"glossaire.md", "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md"}:
        return
    for m in PII_PATTERN.finditer(body):
        report.add(Issue(
            path=path,
            severity="ERROR",
            rule="pii-praticien",
            message=f"donnée personnelle potentielle (praticien identifiable) : « {m.group(0)} »",
            line=get_line_number(body, m.start()),
        ))


def check_frontmatter(report: Report, path: Path, fm: dict | None) -> None:
    """Frontmatter conforme aux conventions.

    Les fichiers de gouvernance dans docs/ (WORKFLOW.md, GITHUB_HARDENING.md)
    ne sont pas des fiches produit — frontmatter optionnel pour eux.
    """
    is_governance = path.name in META_GOVERNANCE_FILES

    if fm is None:
        # Frontmatter absent : OK pour la racine et fichiers gouvernance
        if "docs" in path.parts and not is_governance:
            report.add(Issue(
                path=path,
                severity="ERROR",
                rule="frontmatter-missing",
                message="frontmatter YAML absent (obligatoire pour les pages docs/)",
            ))
        return

    report.pages_with_frontmatter += 1

    # Champs obligatoires (uniquement pour les pages docs/ hors gouvernance)
    if "docs" in path.parts and not is_governance:
        missing = REQUIRED_FRONTMATTER_FIELDS_DOCS - set(fm.keys())
        if missing:
            report.add(Issue(
                path=path,
                severity="ERROR",
                rule="frontmatter-fields",
                message=f"champs frontmatter manquants : {sorted(missing)}",
            ))

    # schema_type connu
    schema_type = fm.get("schema_type")
    if schema_type and schema_type not in ALLOWED_SCHEMA_TYPES:
        report.add(Issue(
            path=path,
            severity="WARN",
            rule="frontmatter-schema",
            message=f"schema_type inhabituel : '{schema_type}' (valeurs courantes : {sorted(ALLOWED_SCHEMA_TYPES)})",
        ))

    # Sources : chaque entrée doit avoir url OU note explicite
    sources = fm.get("source_documents", [])
    if isinstance(sources, list):
        for idx, source in enumerate(sources):
            if isinstance(source, dict):
                if not source.get("url") and not source.get("note"):
                    report.add(Issue(
                        path=path,
                        severity="ERROR",
                        rule="source-without-url",
                        message=f"source #{idx + 1} ('{source.get('title', '?')}') sans 'url' ni 'note' explicite — URL publique directe obligatoire",
                    ))


def check_jsonld_blocks(report: Report, path: Path, content: str) -> None:
    """Blocs JSON-LD inline doivent être du JSON valide."""
    for m in JSONLD_RE.finditer(content):
        raw = m.group(1).strip()
        # Tolérance : si le bloc contient du templating Liquid ({{ ... }} ou {% ... %}),
        # on saute la validation JSON (sera rendu par Jekyll au build).
        if "{{" in raw or "{%" in raw:
            continue
        try:
            data = json.loads(raw)
            if "@context" not in data:
                report.add(Issue(
                    path=path,
                    severity="WARN",
                    rule="jsonld-context",
                    message="bloc JSON-LD sans clé '@context'",
                    line=get_line_number(content, m.start()),
                ))
            if "@type" not in data:
                report.add(Issue(
                    path=path,
                    severity="WARN",
                    rule="jsonld-type",
                    message="bloc JSON-LD sans clé '@type'",
                    line=get_line_number(content, m.start()),
                ))
        except json.JSONDecodeError as e:
            report.add(Issue(
                path=path,
                severity="ERROR",
                rule="jsonld-invalid",
                message=f"bloc JSON-LD invalide : {e}",
                line=get_line_number(content, m.start()),
            ))


def _resolve_internal_link(root: Path, path: Path, target: str) -> bool:
    """Vrai si le lien interne correspond à un fichier source existant.

    Gère deux conventions :
    - chemin de fichier direct (``../x/overview.md``, ``./img.png``) ;
    - permalink Jekyll (``../x/overview/`` ou ``/docs/fr/.../x/overview/``) dont
      le fichier source est ``x/overview.md`` — et NON ``x/overview/index.md``.
    """
    # Une page publiée est servie SOUS le baseurl : tout lien interne absolu doit
    # donc être préfixé du baseurl, sinon il pointe hors du site → 404 live.
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        rel = path.name
    is_published = (
        rel.startswith("docs/fr/") or rel.startswith("sources/")
        or rel in ("index.md", "404.html")
    )

    # Lien baseurl-absolu (/durr-dental-knowledge-base/docs/...) : retirer le
    # baseurl pour retomber sur un chemin racine-absolu résolvable localement.
    baseurl = "/durr-dental-knowledge-base"
    if target == baseurl or target == baseurl + "/":
        return True  # page d'accueil (landing, dépôt racine séparé)
    if target.startswith(baseurl + "/"):
        target = target[len(baseurl):]
    elif is_published and target.startswith("/") and not target.startswith("//"):
        # lien racine-absolu SANS baseurl depuis une page publiée = 404 live
        # (ex. `/docs/fr/` au lieu de `/durr-dental-knowledge-base/docs/fr/`).
        return False

    stem = target.rstrip("/")
    if target.startswith("/"):
        # lien racine-absolu : relatif à la racine du dépôt
        base = root
        stem = stem.lstrip("/")
    else:
        # lien relatif : relatif au fichier courant. NB : sur les pages publiées
        # (permalinks Jekyll à slash final), un lien relatif se résout un cran
        # plus bas côté navigateur — cause du bug 404. Les liens internes des
        # pages publiées sont donc désormais TOUS en absolu baseurl (voir plus
        # haut), ce qui supprime cette ambiguïté. Ici on reste fichier-relatif,
        # correct pour les docs de dev non publiées (README, docs/WORKFLOW…).
        base = path.parent

    # Fichier direct écrit en dur (asset, ``x/overview.md``, ``img.png``) :
    # accepté uniquement si c'est vraiment un FICHIER (pas un dossier nu — un
    # lien vers `.../produit/` 404 en live, seul `.../produit/overview/` existe).
    try:
        if (base / stem).resolve().is_file():
            return True
    except (OSError, ValueError):
        pass
    # Permalink Jekyll : `.../x/overview/` → fichier source `x/overview.md` ;
    # `.../ligne/` → `ligne/index.md`. On ne mappe PAS un lien-dossier vers un
    # `overview.md` enfant (Jekyll ne sert pas `.../produit/` mais `.../produit/overview/`).
    candidates = (
        base / (stem + ".md"),       # permalink → fichier source .md
        base / (stem + ".html"),     # permalink → fichier source .html
        base / stem / "index.md",    # dossier avec index -> servi à `.../<dossier>/`
    )
    for c in candidates:
        try:
            if c.resolve().is_file():
                return True
        except (OSError, ValueError):
            continue
    return False


def check_internal_links(report: Report, root: Path, path: Path, body: str) -> None:
    """Liens Markdown vers des fichiers locaux doivent exister."""
    for m in MD_LINK_RE.finditer(body):
        href = m.group(2)
        # Ignorer URLs absolues et ancres pures
        if href.startswith(("http://", "https://", "mailto:", "#", "//")):
            continue
        # Ignorer les liens Jekyll Liquid (résolution post-build)
        if "{{" in href or "{%" in href:
            continue
        # Retirer ancre éventuelle
        target_path = href.split("#")[0]
        if not target_path:
            continue
        # Résolution Jekyll-aware (permalink ../x/overview/ → fichier ../x/overview.md)
        if not _resolve_internal_link(root, path, target_path):
            report.add(Issue(
                path=path,
                severity="WARN",
                rule="link-broken",
                message=f"lien interne non résolu (peut être un permalink Jekyll) : « {href} »",
                line=get_line_number(body, m.start()),
            ))


# ------------------------------------------------------------------
# Moteur de scan
# ------------------------------------------------------------------

def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in TARGET_EXTENSIONS:
            continue
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        yield path


def validate_file(report: Report, root: Path, path: Path) -> None:
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        report.add(Issue(
            path=path,
            severity="ERROR",
            rule="io",
            message=f"impossible de lire le fichier : {e}",
        ))
        return

    report.files_scanned += 1

    try:
        fm, body = split_frontmatter(content)
    except ValueError as e:
        report.add(Issue(
            path=path,
            severity="ERROR",
            rule="frontmatter-invalid",
            message=str(e),
        ))
        return

    check_frontmatter(report, path, fm)
    check_competitor_names(report, path, body)
    check_internal_markers(report, path, body)
    check_pii(report, path, body)
    check_jsonld_blocks(report, path, content)
    check_internal_links(report, root, path, body)


# ------------------------------------------------------------------
# Entrée
# ------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validation déterministe du dépôt Dürr Dental Knowledge Base.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Racine du dépôt à valider (défaut : répertoire courant).",
    )
    parser.add_argument(
        "--warn-as-error",
        action="store_true",
        help="Traiter les warnings comme des erreurs (code de retour 1).",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report = Report()

    for path in iter_files(root):
        validate_file(report, root, path)

    # Rapport humain
    print()
    print("=" * 72)
    print("VALIDATE.PY — rapport")
    print("=" * 72)
    print(f"Fichiers scannés         : {report.files_scanned}")
    print(f"Pages avec frontmatter   : {report.pages_with_frontmatter}")
    print(f"Erreurs                  : {len(report.errors())}")
    print(f"Avertissements           : {len(report.warnings())}")
    print()

    if not report.issues:
        print("Aucun problème détecté.")
        return 0

    by_severity = {"ERROR": [], "WARN": []}
    for issue in report.issues:
        by_severity[issue.severity].append(issue)

    for severity in ("ERROR", "WARN"):
        items = by_severity[severity]
        if not items:
            continue
        print(f"--- {severity} ({len(items)}) ---")
        for issue in items:
            try:
                rel = issue.path.relative_to(root)
            except ValueError:
                rel = issue.path
            line = f":{issue.line}" if issue.line else ""
            print(f"  [{issue.rule}] {rel}{line}")
            print(f"      {issue.message}")
        print()

    has_errors = bool(report.errors())
    has_warnings = bool(report.warnings())
    if has_errors:
        return 1
    if args.warn_as_error and has_warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
