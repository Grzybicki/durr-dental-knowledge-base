#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Regenere llms.txt et llms-full.txt depuis les fiches docs/fr/**/overview.md.

Usage:
    python scripts/build_llms_full.py                # ecrit llms.txt + llms-full.txt
    python scripts/build_llms_full.py --check         # n'ecrit rien, rapporte les ecarts
    python scripts/build_llms_full.py --check-full-only

Regles reproduites depuis le format existant (verifiees par diff avant premiere ecriture) :
  - llms-full.txt : concatenation des corps de fiche (sans frontmatter ni <script> JSON-LD),
    separee par une ligne de 80 "=", precedee d'un en-tete "# Titre\nURL : <url>\n".
    Les liens internes absolus (/durr-dental-knowledge-base/... ou l'URL complete) sont
    reecrits en chemins relatifs (../autre-fiche/overview/, ../../glossaire/, etc.).
  - llms.txt : index groupe par categorie (Imagerie dentaire / Conventionnel / Hygiene et
    chimie / Entreprise), trie par titre, avec description tronquee a ~155 caracteres.
"""
import io
import os
import re
import sys
import posixpath
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_FR = os.path.join(ROOT, "docs", "fr")
BASE_URL = "https://grzybicki.github.io/durr-dental-knowledge-base"

CATEGORY_ORDER = ["imagerie", "conventionnel", "hygiene-chimie", "durr-dental-entreprise"]
CATEGORY_TITLES = {
    "imagerie": "Imagerie dentaire",
    "conventionnel": "Conventionnel — air comprimé et aspiration",
    "hygiene-chimie": "Hygiène et chimie de désinfection",
    "durr-dental-entreprise": "Entreprise",
}

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
SCRIPT_RE = re.compile(r"<script[^>]*>.*?</script>\n?", re.DOTALL)
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def find_overview_files():
    files = []
    for dirpath, _dirnames, filenames in os.walk(DOCS_FR):
        for fn in filenames:
            if fn == "overview.md":
                files.append(os.path.join(dirpath, fn))
    return sorted(files)


def parse_fiche(path):
    with io.open(path, encoding="utf-8") as fh:
        content = fh.read()
    m = FRONTMATTER_RE.match(content)
    if not m:
        raise ValueError("Pas de frontmatter valide: %s" % path)
    fm = yaml.safe_load(m.group(1))
    body = content[m.end():]
    return fm, body


def permalink_dir(permalink):
    """'/docs/fr/imagerie/dicom/overview/' -> 'docs/fr/imagerie/dicom'"""
    p = permalink.strip("/")
    if p.endswith("/overview"):
        p = p[: -len("/overview")]
    elif p == "overview":
        p = ""
    return p


def rewrite_links(body, current_permalink):
    current_dir = permalink_dir(current_permalink)

    def repl(match):
        url = match.group(1)
        original = url
        if url.startswith(BASE_URL):
            path = url[len(BASE_URL):]
        elif url.startswith("/durr-dental-knowledge-base"):
            path = url[len("/durr-dental-knowledge-base"):]
        else:
            return match.group(0)  # lien externe ou relatif deja : inchange

        has_overview = path.rstrip("/").endswith("/overview") or path.strip("/") == "overview"
        target_dir = path.strip("/")
        if has_overview:
            if target_dir.endswith("/overview"):
                target_dir = target_dir[: -len("/overview")]
            elif target_dir == "overview":
                target_dir = ""

        rel = posixpath.relpath(target_dir or ".", current_dir or ".")
        if rel == ".":
            rel = ""
        parts = [p for p in [rel, "overview" if has_overview else ""] if p]
        href = "/".join(parts)
        if not href:
            href = "."
        href += "/"
        return "](%s)" % href

    return LINK_RE.sub(repl, body)


def strip_scripts(body):
    return SCRIPT_RE.sub("", body)


def clean_body(body):
    # Retire les lignes vides en trop (max 1 ligne vide consecutive), trim global.
    lines = body.split("\n")
    out = []
    blank_run = 0
    for ln in lines:
        if ln.strip() == "":
            blank_run += 1
            if blank_run > 1:
                continue
        else:
            blank_run = 0
        out.append(ln)
    text = "\n".join(out).strip("\n")
    return text


def build_full_section(fm, body):
    permalink = fm["permalink"]
    url = BASE_URL + permalink
    title = fm["title"]
    rewritten = rewrite_links(body, permalink)
    rewritten = strip_scripts(rewritten)
    rewritten = clean_body(rewritten)
    header = "# %s\nURL : %s\n" % (title, url)
    return header + "\n" + rewritten + "\n"


def truncate_desc(desc, limit=155):
    desc = " ".join(desc.split())
    if len(desc) <= limit:
        return desc
    return desc[:limit].rstrip() + "…"


def category_of(path):
    rel = os.path.relpath(path, DOCS_FR)
    return rel.split(os.sep)[0]


def build_llms_txt(fiches):
    by_cat = {}
    for path, fm in fiches:
        cat = category_of(path)
        by_cat.setdefault(cat, []).append(fm)

    lines = []
    lines.append("# Dürr Dental Knowledge Base")
    lines.append("")
    lines.append(
        "> Base de connaissance indépendante et publiquement sourcée des produits Dürr "
        "Dental (imagerie dentaire, conventionnel, hygiène-chimie) : %d fiches en Markdown, "
        "sourcées sur des documents publics et structurées (JSON-LD MedicalDevice, FAQPage) "
        "pour la citation fidèle par les moteurs de réponse et LLM. Initiative personnelle "
        "d'un salarié Dürr Dental France — non officielle. Licence CC-BY 4.0, réutilisation "
        "IA autorisée." % len(fiches)
    )
    lines.append("")
    lines.append(
        "Toutes les sources sont strictement publiques : manuels qr.duerrdental.com, "
        "brochures et factsheets publiques, Déclarations de Conformité publiques, Eudamed, "
        "normes EN/ISO, pages de partenaires officiels. Aucune donnée confidentielle, aucune "
        "comparaison concurrentielle."
    )
    lines.append("")

    for cat in CATEGORY_ORDER:
        if cat not in by_cat:
            continue
        lines.append("## %s" % CATEGORY_TITLES[cat])
        lines.append("")
        entries = sorted(by_cat[cat], key=lambda fm: fm["title"])
        for fm in entries:
            url = BASE_URL + fm["permalink"]
            desc = truncate_desc(fm.get("description", ""))
            lines.append("- [%s](%s): %s" % (fm["title"], url, desc))
        lines.append("")

    lines.append("## Références transverses")
    lines.append("")
    lines.append(
        "- [Matrice réglementaire MDR (classes, Notified Body, certificats)](%s/sources/certificates/)"
        % BASE_URL
    )
    lines.append("- [Version concaténée pour ingestion LLM](%s/llms-full.txt)" % BASE_URL)
    lines.append("")
    lines.append("## Ressources fabricant officielles")
    lines.append("")
    lines.append("- https://www.duerrdental.com — site officiel Dürr Dental")
    lines.append("- https://www.duerrdental.com/fr/ — Dürr Dental France")
    lines.append("- https://ec.europa.eu/tools/eudamed/ — base européenne dispositifs médicaux (MDR)")
    lines.append("")
    return "\n".join(lines)


def main():
    check_only = "--check" in sys.argv

    files = find_overview_files()
    fiches = []
    sections = []
    for path in files:
        fm, body = parse_fiche(path)
        fiches.append((path, fm))
        sections.append(build_full_section(fm, body))

    sep = "=" * 80
    full_text = ("\n" + sep + "\n").join(sections)
    full_text = sep + "\n" + full_text + "\n"

    txt_text = build_llms_txt(fiches)

    full_path = os.path.join(ROOT, "llms-full.txt")
    txt_path = os.path.join(ROOT, "llms.txt")

    if check_only:
        for out_path, new_text in [(full_path, full_text), (txt_path, txt_text)]:
            if os.path.exists(out_path):
                with io.open(out_path, encoding="utf-8") as fh:
                    old_text = fh.read()
                if old_text.strip() == new_text.strip():
                    print("OK   (identique) :", out_path)
                else:
                    print("DIFF (a regenerer) :", out_path)
            else:
                print("ABSENT :", out_path)
        print("Fiches trouvees :", len(fiches))
        return

    with io.open(full_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(full_text)
    with io.open(txt_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt_text)
    print("Ecrit :", full_path, "(%d fiches)" % len(fiches))
    print("Ecrit :", txt_path)


if __name__ == "__main__":
    main()
