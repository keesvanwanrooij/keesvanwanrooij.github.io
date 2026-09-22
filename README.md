# keesvanwanrooij.github.io (www.keesvanwanrooij.nl)

Persoonlijke merkwebsite van Kees van Wanrooij, ondernemer, belegger en NLP-practitioner, oprichter van Belegger Kees.

Live op https://www.keesvanwanrooij.nl/

De site gaat over beleggen: [Belegger Kees](https://beleggerkees.nl), de openbare [Belegger Kees Methode](https://www.keesvanwanrooij.nl/belegger-kees-methode/) en de BK Insider Screener die volgt zodra hij openbaar is. Het woord *cursus* staat bewust niet meer in het menu.

Alles wat niet over beleggen gaat, staat onder `/projecten/` en is daar benoemd als hobby project. Toekomstige projecten (zoals de calorieëntracker en het online spel) krijgen daar hun eigen infopagina. Nieuwe pagina's *over* beleggen komen juist in de root te staan, bijvoorbeeld `/bk-insider-screener/` en `/gratis-cursus-beleggen/`.

## Ecosysteem

Vier GitHub Pages repository's worden samen onder één domein bediend. Dat komt doordat de `CNAME` in deze user-site (`keesvanwanrooij.github.io`) het custom domain voor het hele account zet: GitHub stuurt `keesvanwanrooij.github.io/<repo>/` met een 301 door naar `www.keesvanwanrooij.nl/<repo>/`. De project-repo's hebben dus géén eigen `CNAME` en zijn ook niet los op github.io bereikbaar.

Voor Google is dit één website (één host), niet vier. Eén Search Console property op het domein dekt alles.

De hub en de methode delen het ecosysteemblok in de voettekst (Beleggen, Op Belegger Kees, Hobby projecten, Kees van Wanrooij). De twee cursussites hebben een eigen variant, omdat zij hobby zijn en hun eigen navigatie en donatieknop houden. Elke kolom heeft maximaal vier links.

| Site | Repository |
| --- | --- |
| [www.keesvanwanrooij.nl](https://www.keesvanwanrooij.nl/) (deze hub) | [keesvanwanrooij.github.io](https://github.com/keesvanwanrooij/keesvanwanrooij.github.io) |
| [Belegger Kees Methode](https://www.keesvanwanrooij.nl/belegger-kees-methode/) | [belegger-kees-methode](https://github.com/keesvanwanrooij/belegger-kees-methode) |
| [Cursus Elektrotechniek](https://www.keesvanwanrooij.nl/cursus-elektrotechniek/) | [cursus-elektrotechniek](https://github.com/keesvanwanrooij/cursus-elektrotechniek) |
| [Cursus CV-ketels](https://www.keesvanwanrooij.nl/cursus-cv-ketels/) | [cursus-cv-ketels](https://github.com/keesvanwanrooij/cursus-cv-ketels) |

Wijzig je de lijst met sites, pas dan het ecosysteemblok aan: `tools/build-chrome.py` hier en `site/build.py` (`ECO`) in de methode. De cursussen hebben hun eigen `Views.footer()` en verwijzen alleen terug naar deze site.

## Opbouw

Gewone HTML en CSS, geen JavaScript en geen afhankelijkheden. Kop en voet komen uit één bron: draai na een wijziging `python tools/build-chrome.py`. Alle paden beginnen met `/`, dus de site werkt vanaf de root van een domein.

```text
index.html                             home
beleggen/index.html                    Beleggen met GARP en NLP (met FAQ)
welke-kees/index.html                  wie Belegger Kees is, en wie niet (met FAQ)
over-mij/index.html                    achtergrond en verhaal
projecten/index.html                   overzicht van de hobby projecten
projecten/elektrotechniek/index.html   infopagina cursus Elektrotechniek
projecten/cv-ketels/index.html         infopagina cursus CV-ketels
cursussen/index.html                   doorstuurpagina naar /projecten/
elektrotechniek/index.html             doorstuurpagina naar /projecten/elektrotechniek/
cv-ketels/index.html                   doorstuurpagina naar /projecten/cv-ketels/
404.html                               foutpagina
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

Alleen de `robots.txt` in de root van het domein wordt door zoekmachines gelezen. Die staat in deze repository en noemt de sitemaps van alle vier de sites. De `robots.txt` in de submappen van de cursussen en de methode is dus alleen informatief.

De `sitemap.xml` van de hub bevat uitsluitend de eigen pagina's. De andere drie repository's leveren hun eigen sitemap; die staan in `robots.txt` en hoeven hier niet nog eens genoemd te worden.

De doorstuurpagina's (`cursussen/`, `elektrotechniek/`, `cv-ketels/`) staan op `noindex, follow` met een `canonical` naar de nieuwe URL en een meta refresh. GitHub Pages kan geen serverredirect, dus dit is de dichtstbijzijnde vervanging van een 301. Zet ze niet in de sitemap.

## Huisstijl en regels

De stijl volgt het Belegger Kees ontwerpsysteem: wit en Apple-grijs, deep carbon `#1D1D1F`, execution red `#C4303C` als zeldzaam accent (hoogstens een rode knop per scherm), Inter voor tekst en JetBrains Mono voor cijfers, geen donkere modus. Tokens staan bovenaan `assets/css/style.css`.

Voor teksten gelden dezelfde regels als bij Belegger Kees: educatie en geen advies, geen verboden woorden, geen lang streepje, en nooit een cijfer, bron, datum of citaat verzinnen. Een pagina met financiële inhoud draagt de lange disclaimer, letterlijk.

## Repositories openbaar maken

De Belegger Kees Methode is openbaar en staat als Live op de home en op `beleggen/`. De BK Insider Screener staat nog op privé en heeft een kaart met het label "In aanbouw, binnenkort openbaar" en zonder link naar de repository, zodat bezoekers geen 404 zien. Wordt de screener openbaar:

1. Vervang op `index.html` (sectie "Waar ik aan werk") en `beleggen/index.html` (sectie "Tools en open projecten") het label door "Live" en zet een link naar de repository in de kaart.
2. Verwijder de regel "Zodra de repository openbaar is, staat hier de link." op `beleggen/index.html`.
3. Overweeg een eigen pagina `/bk-insider-screener/`, in de root omdat het over beleggen gaat.
4. Voeg de link toe aan `llms.txt`.
5. Werk `lastmod` in `sitemap.xml` en "Bijgewerkt" op de pagina bij.

## Nog te doen na de lancering van beleggerkees.nl

Zodra de nieuwe Astro-site live is (`/over`, `/auteur/kees-van-wanrooij`, `/redactioneel` en `/aandelen` geven nu nog 404):

- Link vanaf `over-mij/` naar de auteurspagina en voeg die toe aan `sameAs` in de Person-gegevens.
- Link vanaf `beleggen/` naar `/aandelen` en `/redactioneel`.
- Vraag vanaf beleggerkees.nl een link terug naar deze site (voorkeur: de auteurspagina en de voettekst).

## Lettertypen

Inter en JetBrains Mono worden gedistribueerd onder de SIL Open Font License 1.1. De bestanden in `assets/fonts/` zijn de Latin-subsets, gekopieerd uit de build van beleggerkees.nl.

## Auteur

Kees van Wanrooij. Educatie, geen beleggingsadvies.
