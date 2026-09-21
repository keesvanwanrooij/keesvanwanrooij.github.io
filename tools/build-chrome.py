"""
Zet de gedeelde kop (navigatie) en voet (ecosysteem) in alle pagina's.

In elke pagina staan de plaatshouders <!-- site:header --> en <!-- site:footer -->
(of het reeds gegenereerde blok tussen <!-- site:header:start/end -->). Dit script vult ze.
De ecosysteemblokken in de voet zijn hetzelfde in alle vier de repositories:
  www.keesvanwanrooij.nl (repo keesvanwanrooij.github.io), belegger-kees-methode, cursus-elektrotechniek, cursus-cv-ketels.
Wijzig je de lijst hieronder, pas dan ook de drie andere repositories aan.

Gebruik: python tools/build-chrome.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (pad, sleutel voor aria-current in kop, sleutel voor aria-current in voet)
PAGES = {
    "index.html": ("", "home"),
    "beleggen/index.html": ("beleggen", "beleggen"),
    "cursussen/index.html": ("cursussen", ""),
    "elektrotechniek/index.html": ("cursussen", ""),
    "cv-ketels/index.html": ("cursussen", ""),
    "over-mij/index.html": ("over-mij", "over-mij"),
    "404.html": ("", ""),
}

METHODE = "https://www.keesvanwanrooij.nl/belegger-kees-methode/"
ELEKTRO = "https://www.keesvanwanrooij.nl/cursus-elektrotechniek/"
CV = "https://www.keesvanwanrooij.nl/cursus-cv-ketels/"

NAV = [
    ("beleggen", "/beleggen/", "Beleggen"),
    ("methode", METHODE, "Methode"),
    ("cursussen", "/cursussen/", "Cursussen"),
    ("over-mij", "/over-mij/", "Over mij"),
]

# Kolommen van het ecosysteem: (kop, [(sleutel, href, tekst)])
ECO = [
    ("Beleggen", [
        ("belegger-kees", "https://beleggerkees.nl", "Belegger Kees"),
        ("methode", METHODE, "Belegger Kees Methode"),
        ("beleggen", "/beleggen/", "Beleggen met GARP en NLP"),
    ]),
    ("Gratis cursussen", [
        ("elektro", ELEKTRO, "Cursus Elektrotechniek"),
        ("cv", CV, "Cursus CV-ketels"),
    ]),
    ("Kees van Wanrooij", [
        ("home", "/", "Home"),
        ("over-mij", "/over-mij/", "Over mij"),
        ("linkedin", "https://www.linkedin.com/in/keesvanwanrooij/", "LinkedIn"),
        ("instagram", "https://www.instagram.com/beleggerkees/", "Instagram"),
        ("github", "https://github.com/keesvanwanrooij", "GitHub"),
    ]),
]


def header(current):
    items = []
    for key, href, text in NAV:
        cur = ' aria-current="page"' if key == current else ""
        items.append(f'          <li><a href="{href}"{cur}>{text}</a></li>')
    return (
        '  <header class="site-header">\n'
        '    <div class="wrap header-inner">\n'
        '      <a class="brand" href="/">Kees van Wanrooij<span class="dot" aria-hidden="true">.</span></a>\n'
        '      <nav class="site-nav" aria-label="Hoofdmenu">\n'
        '        <ul>\n' + "\n".join(items) + '\n        </ul>\n'
        '      </nav>\n'
        '    </div>\n'
        '  </header>'
    )


def footer(current):
    cols = []
    for kop, links in ECO:
        lis = []
        for key, href, text in links:
            cur = ' aria-current="true"' if key == current else ""
            lis.append(f'            <li><a href="{href}"{cur}>{text}</a></li>')
        cols.append(
            f'        <nav aria-label="{kop}">\n'
            f'          <h2>{kop}</h2>\n'
            f'          <ul>\n' + "\n".join(lis) + '\n          </ul>\n'
            f'        </nav>'
        )
    return (
        '  <footer class="site-footer">\n'
        '    <div class="wrap">\n'
        '      <div class="footer-grid">\n'
        '        <div>\n'
        '          <p class="footer-brand">Kees van Wanrooij<span class="dot" aria-hidden="true">.</span></p>\n'
        '          <p class="small">Belegger en NLP-practitioner. Oprichter van Belegger Kees. Educatie, geen beleggingsadvies.</p>\n'
        '        </div>\n' + "\n".join(cols) + '\n'
        '      </div>\n'
        '      <div class="footer-legal">\n'
        '        <p>© 2026 Kees van Wanrooij. Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.</p>\n'
        '      </div>\n'
        '    </div>\n'
        '  </footer>'
    )


def fill(text, name, block):
    marked = re.compile(rf"  <!-- site:{name}:start -->.*?<!-- site:{name}:end -->", re.S)
    wrapped = f"  <!-- site:{name}:start -->\n{block}\n  <!-- site:{name}:end -->"
    if marked.search(text):
        return marked.sub(lambda m: wrapped, text)
    return text.replace(f"  <!-- site:{name} -->", wrapped)


for page, (nav_key, foot_key) in PAGES.items():
    p = ROOT / page
    t = p.read_text(encoding="utf-8")
    t = fill(t, "header", header(nav_key))
    t = fill(t, "footer", footer(foot_key))
    p.write_text(t, encoding="utf-8")
    print("bijgewerkt:", page)
