# -*- coding: utf-8 -*-
"""
Bouwt één compleet overzicht van alle pagina's op www.keesvanwanrooij.nl,
over de vier repository's heen: deze hub, de Belegger Kees Methode en de
twee cursussen. Ze staan onder hetzelfde domein maar in aparte repo's, dus
de hub kan hun pagina's niet lokaal inlezen: dit script haalt hun eigen
sitemap.xml en de <title> van elke pagina live op.

Output:
  sitemap.xml       platte sitemap met alle ~350 pagina's van het domein.
  sitemap/index.html  overzichtelijke HTML-pagina met dezelfde lijst,
                    gegroepeerd per site en per sectie, voor bezoekers
                    en voor de interne links die Google's crawler volgt.

sitemap-site.xml (de eigen pagina's van de hub) blijft de brondata voor het
"Kees van Wanrooij"-deel van beide bestanden; die lijst onderhoud je nog
altijd zelf. Draai dit script opnieuw na elke wijziging aan een van de
vier sites, of laat .github/workflows/refresh-sitemap.yml het periodiek
doen.

Gebruik: python tools/build-sitemap.py
"""
import concurrent.futures
import html
import io
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent.parent
HUB = "https://www.keesvanwanrooij.nl"
UA = "Mozilla/5.0 (compatible; keesvanwanrooij-sitemap-builder/1.0)"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# (naam, sitemap-URL, URL-prefix van die site, labels per padsegment)
EXTERNE_SITES = [
    (
        "Belegger Kees Methode",
        HUB + "/belegger-kees-methode/sitemap.xml",
        HUB + "/belegger-kees-methode/",
        {
            "docs": "Docs", "manifesto": "Manifesto", "analyseproces": "Analyseproces",
            "onderzoek": "Onderzoek", "resources": "Resources", "community": "Community",
            "nlp-coaching-voor-beleggers": "NLP-coaching", "over-belegger-kees": "Over Belegger Kees",
        },
    ),
    (
        "Cursus Elektrotechniek",
        HUB + "/cursus-elektrotechniek/sitemap.xml",
        HUB + "/cursus-elektrotechniek/",
        {"module": "Modules", "les": "Losse lessen", "toepassingen": "Toepassingen",
         "merken": "Merken", "naslag": "Naslag"},
    ),
    (
        "Cursus CV-ketels",
        HUB + "/cursus-cv-ketels/sitemap.xml",
        HUB + "/cursus-cv-ketels/",
        {"module": "Modules", "les": "Losse lessen", "storingzoeker": "Storingzoeker",
         "kaarten": "Flashcards", "naslag": "Naslag"},
    ),
]

def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def fetch_title(url):
    try:
        raw = fetch(url, timeout=10).decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError):
        return None
    m = re.search(r"<title>(.*?)</title>", raw, re.S)
    if not m:
        return None
    titel = html.unescape(m.group(1)).strip()
    titel = re.sub(r"\s+", " ", titel)
    # "Paginanaam | Sitenaam" -> alleen de paginanaam.
    if " | " in titel:
        eerste = titel.split(" | ", 1)[0].strip()
        if eerste:
            titel = eerste
    return titel or None


def slug_titel(pad):
    laatste = [seg for seg in pad.strip("/").split("/") if seg][-1:]
    if not laatste:
        return "Home"
    woord = laatste[0].replace("-", " ")
    return woord[:1].upper() + woord[1:]


def groep_van(loc, prefix, labels):
    rest = loc[len(prefix):].strip("/")
    if not rest:
        return None  # de homepage van de site zelf
    segment = rest.split("/", 1)[0]
    return labels.get(segment, segment.replace("-", " ").capitalize())


def own_pages():
    """Leest de eigen sitemap-site.xml (brondata, handmatig onderhouden) en
    haalt per pagina de titel uit het lokale bestand, zonder netwerk."""
    tree = ElementTree.parse(ROOT / "sitemap-site.xml")
    out = []
    for url_el in tree.getroot():
        loc = url_el.find("sm:loc", NS).text.strip()
        lastmod_el = url_el.find("sm:lastmod", NS)
        lastmod = lastmod_el.text.strip() if lastmod_el is not None else None
        pad = loc[len(HUB):] or "/"
        bestand = ROOT / pad.strip("/") / "index.html" if pad != "/" else ROOT / "index.html"
        titel = None
        if bestand.exists():
            m = re.search(r"<title>(.*?)</title>", bestand.read_text(encoding="utf-8"), re.S)
            if m:
                titel = html.unescape(m.group(1)).strip()
                if " | " in titel:
                    titel = titel.split(" | ", 1)[0].strip()
        out.append({"loc": loc, "lastmod": lastmod, "titel": titel or slug_titel(pad)})
    return out


def externe_pages(naam, sitemap_url, prefix, labels):
    raw = fetch(sitemap_url)
    tree = ElementTree.fromstring(raw)
    entries = []
    for url_el in tree:
        loc = url_el.find("sm:loc", NS).text.strip()
        lastmod_el = url_el.find("sm:lastmod", NS)
        lastmod = lastmod_el.text.strip() if lastmod_el is not None else None
        entries.append({"loc": loc, "lastmod": lastmod, "groep": groep_van(loc, prefix, labels)})

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
        titels = list(ex.map(lambda e: fetch_title(e["loc"]), entries))
    for e, t in zip(entries, titels):
        e["titel"] = t or slug_titel(e["loc"][len(prefix):])
    return naam, entries


def esc(s):
    return html.escape(s, quote=True)


def schrijf_sitemap_xml(alle_paginas):
    regels = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in alle_paginas:
        lm = f"<lastmod>{esc(p['lastmod'])}</lastmod>" if p.get("lastmod") else ""
        regels.append(f"  <url><loc>{esc(p['loc'])}</loc>{lm}</url>")
    regels.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(regels) + "\n", encoding="utf-8", newline="\n")


def schrijf_sitemap_pagina(eigen, externe, totaal):
    def lijst(paginas):
        lis = []
        for p in sorted(paginas, key=lambda p: p["loc"]):
            lis.append(f'          <li><a href="{esc(p["loc"])}">{esc(p["titel"])}</a></li>')
        return "\n".join(lis)

    secties = []

    secties.append(
        '      <div class="sitemap-site">\n'
        '        <h2>Kees van Wanrooij <span class="small">(deze site)</span></h2>\n'
        '        <ul>\n' + lijst(eigen) + "\n        </ul>\n"
        "      </div>"
    )

    for naam, entries, prefix in externe:
        homepagina = [p for p in entries if p["loc"].rstrip("/") == prefix.rstrip("/")]
        rest = [p for p in entries if p["loc"].rstrip("/") != prefix.rstrip("/")]
        groepen = {}
        for p in rest:
            groepen.setdefault(p.get("groep") or "Overig", []).append(p)

        blok = [f'      <div class="sitemap-site">\n        <h2>{esc(naam)} <span class="small">({len(entries)} pagina\'s)</span></h2>']
        if homepagina:
            blok.append('        <ul>\n' + lijst(homepagina) + "\n        </ul>")
        for groepnaam in sorted(groepen):
            blok.append(f'        <h3>{esc(groepnaam)}</h3>\n        <ul>\n{lijst(groepen[groepnaam])}\n        </ul>')
        blok.append("      </div>")
        secties.append("\n".join(blok))

    body = "\n\n".join(secties)

    pagina = f'''<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sitemap | Kees van Wanrooij</title>
  <meta name="description" content="Alle pagina's van www.keesvanwanrooij.nl op een plek: deze site, de Belegger Kees Methode en de twee gratis cursussen, {totaal} pagina's in totaal.">
  <link rel="canonical" href="{HUB}/sitemap/">
  <meta name="robots" content="index, follow">
  <meta name="author" content="Kees van Wanrooij">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="preload" href="/assets/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <a class="skip" href="#main">Ga naar de inhoud</a>

  <!-- site:header:start -->
  <!-- site:header:end -->

  <main id="main">
    <section class="page-hero" style="border-bottom:0" aria-labelledby="titel">
      <div class="wrap">
        <p class="label">Overzicht</p>
        <h1 id="titel">Sitemap</h1>
        <p class="lead">Alle {totaal} pagina's van www.keesvanwanrooij.nl op een plek: deze site, de Belegger Kees Methode en de twee gratis cursussen. Machineleesbaar staat alles ook in <a href="/sitemap.xml">sitemap.xml</a>.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap sitemap-grid">
{body}
      </div>
    </section>
  </main>

  <!-- site:footer:start -->
  <!-- site:footer:end -->
</body>
</html>
'''
    doel = ROOT / "sitemap"
    doel.mkdir(exist_ok=True)
    (doel / "index.html").write_text(pagina, encoding="utf-8", newline="\n")


def main():
    eigen = own_pages()
    externe_ruw = []
    for naam, sitemap_url, prefix, labels in EXTERNE_SITES:
        print(f"ophalen: {naam} ({sitemap_url})", file=sys.stderr)
        try:
            _, entries = externe_pages(naam, sitemap_url, prefix, labels)
        except Exception as e:
            print(f"  MISLUKT: {e}", file=sys.stderr)
            raise
        print(f"  {len(entries)} pagina's", file=sys.stderr)
        externe_ruw.append((naam, entries, prefix))

    alle = list(eigen)
    for _, entries, _ in externe_ruw:
        alle.extend(entries)
    alle.sort(key=lambda p: p["loc"])

    schrijf_sitemap_xml(alle)
    schrijf_sitemap_pagina(eigen, externe_ruw, len(alle))

    print(f"sitemap.xml: {len(alle)} pagina's ({len(eigen)} eigen + "
          + ", ".join(f"{len(e)} {n}" for n, e, _ in externe_ruw) + ")")


if __name__ == "__main__":
    main()
