# keesvanwanrooij.github.io (www.keesvanwanrooij.nl)

Persoonlijke merkwebsite van Kees van Wanrooij, belegger en NLP-practitioner, oprichter van Belegger Kees.

Live op https://www.keesvanwanrooij.nl/

De site is de centrale hub van het merk Kees van Wanrooij. Ongeveer 80% gaat over beleggen: [Belegger Kees](https://beleggerkees.nl) en de openbare [Belegger Kees Methode](https://www.keesvanwanrooij.nl/belegger-kees-methode/). Een klein deel is voor de technische achtergrond (TU Delft) en de gratis cursussen [Elektrotechniek](https://www.keesvanwanrooij.nl/cursus-elektrotechniek/) en [CV-ketels](https://www.keesvanwanrooij.nl/cursus-cv-ketels/). De Insider scanner volgt zodra hij openbaar is.

## Ecosysteem

Vier sites vormen samen het merk. Ze delen hetzelfde ecosysteemblok in de voettekst (Beleggen, Gratis cursussen, Kees van Wanrooij), met behoud van eigen navigatie en, bij de cursussen, de donatieknop.

| Site | Repository |
| --- | --- |
| [www.keesvanwanrooij.nl](https://www.keesvanwanrooij.nl/) (deze hub) | [keesvanwanrooij.github.io](https://github.com/keesvanwanrooij/keesvanwanrooij.github.io) |
| [Belegger Kees Methode](https://www.keesvanwanrooij.nl/belegger-kees-methode/) | [belegger-kees-methode](https://github.com/keesvanwanrooij/belegger-kees-methode) |
| [Cursus Elektrotechniek](https://www.keesvanwanrooij.nl/cursus-elektrotechniek/) | [cursus-elektrotechniek](https://github.com/keesvanwanrooij/cursus-elektrotechniek) |
| [Cursus CV-ketels](https://www.keesvanwanrooij.nl/cursus-cv-ketels/) | [cursus-cv-ketels](https://github.com/keesvanwanrooij/cursus-cv-ketels) |

Wijzig je de lijst met sites, pas dan het ecosysteemblok aan in alle vier: `tools/build-chrome.py` hier, `site/build.py` (`ECO`) in de methode, en `Views.footer()` in beide cursussen.

## Opbouw

Gewone HTML en CSS, geen JavaScript en geen afhankelijkheden. Kop en voet komen uit één bron: draai na een wijziging `python tools/build-chrome.py`. Alle paden beginnen met `/`, dus de site werkt vanaf de root van een domein.

```text
index.html                  home
beleggen/index.html         Beleggen met GARP en NLP (met FAQ)
cursussen/index.html        overzicht van de gratis cursussen
elektrotechniek/index.html  landingspagina voor de cursus Elektrotechniek
cv-ketels/index.html        landingspagina voor de cursus CV-ketels
over-mij/index.html         achtergrond en verhaal
404.html                    foutpagina
assets/css/style.css        alle stijlen en tokens
assets/fonts/               Inter en JetBrains Mono, zelf gehost
assets/img/                 portret en deelafbeelding (og.png)
tools/og.html               bron van og.png, zie het commentaar in het bestand
tools/build-chrome.py       zet de gedeelde kop en voet in alle pagina's
sitemap.xml, robots.txt, llms.txt
```

Lokaal bekijken:

```bash
python -m http.server 8123
```

Open daarna http://localhost:8123/.

## Sitemaps en robots.txt

Alleen de `robots.txt` in de root van het domein wordt door zoekmachines gelezen. Die staat in deze repository en noemt de sitemaps van alle vier de sites. De `robots.txt` in de submappen van de cursussen en de methode is dus alleen informatief. De `sitemap.xml` van de hub bevat de eigen pagina's plus de startpagina van elk van de andere drie sites. De sitemaps met alle lessen en hoofdstukken maken de andere repositories zelf.

## Huisstijl en regels

De stijl volgt het Belegger Kees ontwerpsysteem: wit en Apple-grijs, deep carbon `#1D1D1F`, execution red `#C4303C` als zeldzaam accent (hoogstens een rode knop per scherm), Inter voor tekst en JetBrains Mono voor cijfers, geen donkere modus. Tokens staan bovenaan `assets/css/style.css`.

Voor teksten gelden dezelfde regels als bij Belegger Kees: educatie en geen advies, geen verboden woorden, geen lang streepje, en nooit een cijfer, bron, datum of citaat verzinnen. Een pagina met financiële inhoud draagt de lange disclaimer, letterlijk.

## Repositories openbaar maken

De Belegger Kees Methode is openbaar en staat als Live op de home en op `beleggen/`. De Insider scanner staat nog op privé en heeft een kaart met het label "In aanbouw, binnenkort openbaar" en zonder link, zodat bezoekers geen 404 zien. Wordt de scanner openbaar:

1. Vervang op `index.html` (sectie "Waar ik aan werk") en `beleggen/index.html` (sectie "Tools en open projecten") het label door "Live" en zet een link naar de repository in de kaart.
2. Verwijder de regel "Zodra de repository openbaar is, staat hier de link." op `beleggen/index.html`.
3. Voeg de link toe aan `llms.txt`.
4. Werk `lastmod` in `sitemap.xml` en "Bijgewerkt" op de pagina bij.

## Nog te doen na de lancering van beleggerkees.nl

Zodra de nieuwe Astro-site live is (`/over`, `/auteur/kees-van-wanrooij`, `/redactioneel` en `/aandelen` geven nu nog 404):

- Link vanaf `over-mij/` naar de auteurspagina en voeg die toe aan `sameAs` in de Person-gegevens.
- Link vanaf `beleggen/` naar `/aandelen` en `/redactioneel`.
- Vraag vanaf beleggerkees.nl een link terug naar deze site (voorkeur: de auteurspagina en de voettekst).

## Lettertypen

Inter en JetBrains Mono worden gedistribueerd onder de SIL Open Font License 1.1. De bestanden in `assets/fonts/` zijn de Latin-subsets, gekopieerd uit de build van beleggerkees.nl.

## Auteur

Kees van Wanrooij. Educatie, geen beleggingsadvies.
