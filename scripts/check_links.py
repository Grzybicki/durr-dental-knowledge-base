#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verification des liens externes (equivalent approximatif du job CI 'lychee').

Usage:
    python scripts/check_links.py [--include-llms-full] [--workers N]

Codes acceptes (alignes sur .github/workflows/ci.yml) : 200,206,301,302,308,403,429
"""
import concurrent.futures
import glob
import io
import re
import sys
import time

import requests

ROOT_GLOBS = ["**/*.md", "**/*.html", "llms.txt", "humans.txt", "robots.txt"]
ACCEPTED = {200, 206, 301, 302, 308, 403, 429}
TIMEOUT = 20
UA = "Mozilla/5.0 (compatible; durr-dental-kb-linkcheck/1.0)"

LINK_RE = re.compile(r"""
    (?:\]\((?P<md>[^)\s]+)(?:\s+"[^"]*")?\))       # ](url) ou ](url "title")
    |
    (?:<(?P<angle>https?://[^>\s]+)>)                # <https://...>
    |
    (?:href=["'](?P<href>[^"']+)["'])                # href="..."
""", re.VERBOSE)


def find_files(include_llms_full):
    files = set()
    for pattern in ROOT_GLOBS:
        for f in glob.glob(pattern, recursive=True):
            if "_site" in f or "node_modules" in f or f.startswith("_drafts"):
                continue
            files.add(f)
    if include_llms_full:
        files.add("llms-full.txt")
    return sorted(files)


def extract_urls(path):
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        content = fh.read()
    urls = set()
    for m in LINK_RE.finditer(content):
        url = m.group("md") or m.group("angle") or m.group("href")
        if not url:
            continue
        url = url.strip()
        if url.startswith("mailto:"):
            continue
        if not (url.startswith("http://") or url.startswith("https://")):
            continue
        urls.add(url)
    return urls


def check_url(url):
    try:
        r = requests.head(url, allow_redirects=True, timeout=TIMEOUT,
                           headers={"User-Agent": UA})
        if r.status_code == 405 or r.status_code >= 400:
            # certains serveurs refusent HEAD -> retenter en GET
            r = requests.get(url, allow_redirects=True, timeout=TIMEOUT,
                              headers={"User-Agent": UA}, stream=True)
        return url, r.status_code, None
    except requests.exceptions.RequestException as e:
        return url, None, str(e)[:200]


def main():
    include_full = "--include-llms-full" in sys.argv
    workers = 12
    for a in sys.argv:
        if a.startswith("--workers="):
            workers = int(a.split("=", 1)[1])

    files = find_files(include_full)
    print("Fichiers scannes :", len(files))

    url_to_files = {}
    for f in files:
        for url in extract_urls(f):
            url_to_files.setdefault(url, []).append(f)

    urls = sorted(url_to_files)
    print("URLs externes uniques :", len(urls))
    print()

    start = time.time()
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(check_url, urls):
            results.append(res)

    ok, failed = [], []
    for url, status, err in results:
        if status in ACCEPTED:
            ok.append((url, status))
        else:
            failed.append((url, status, err))

    print("OK   : %d / %d  (%.1fs)" % (len(ok), len(urls), time.time() - start))
    print("ECHEC: %d" % len(failed))
    print()

    if failed:
        print("=" * 80)
        print("LIENS EN ECHEC")
        print("=" * 80)
        for url, status, err in sorted(failed, key=lambda x: x[0]):
            label = str(status) if status else "ERREUR"
            print("[%s] %s" % (label, url))
            if err:
                print("     -> %s" % err)
            for f in url_to_files[url]:
                print("     dans:", f)
            print()

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
