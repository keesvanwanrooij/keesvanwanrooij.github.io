# keesvanwanrooij.github.io (www.keesvanwanrooij.nl)

Persoonlijke merkwebsite van Kees van Wanrooij, ondernemer, belegger en NLP-practitioner, oprichter van Belegger Kees.

Live op https://www.keesvanwanrooij.nl/

De site gaat alleen over beleggen, beleggingspsychologie en NLP: [Belegger Kees](https://beleggerkees.nl), de openbare [Belegger Kees Methode](https://www.keesvanwanrooij.nl/belegger-kees-methode/), de [Insider Scanner](https://www.keesvanwanrooij.nl/insider-scanner/), de [Stock Screener](https://www.keesvanwanrooij.nl/stock-screener/) en de analyses als [Investor Kees op Seeking Alpha](https://seekingalpha.com/author/investor-kees). Zo blijft de topical authority van dit domein zuiver, en versterkt het als auteurssite (E-E-A-T) beleggerkees.nl.

Wat niet over beleggen gaat, staat niet op dit domein en wordt hier nergens gelinkt. De twee cursussen hebben elk een eigen subdomein (zie hieronder). Nieuwe pagina's over beleggen komen in de root te staan, zoals `/insider-scanner/` en `/stock-screener/`.

## Domeinen en repository's

De `CNAME` in deze user-site (`keesvanwanrooij.github.io`) zet `www.keesvanwanrooij.nl` als domein voor het account. Een project-repo zonder eigen `CNAME` (de methode) staat daardoor op `www.keesvanwanrooij.nl/<repo>/`. Een project-repo met een eigen `CNAME` (de cursussen) staat op dat eigen subdomein, en GitHub stuurt het oude pad door.

| Site | Adres | Repository |
| --- | --- | --- |
| Deze hub | [www.keesvanwanrooij.nl](https://www.keesvanwanrooij.nl/) | [keesvanwanrooij.github.io](https://github.com/keesvanwanrooij/keesvanwanrooij.github.io) |
| Belegger Kees Methode | [www.keesvanwanrooij.nl/belegger-kees-methode/](https://www.keesvanwanrooij.nl/belegger-kees-methode/) | [belegger-kees-methode](https://github.com/keesvanwanrooij/belegger-kees-methode) |
| Cursus Elektrotechniek | [elektrotechniek.keesvanwanrooij.nl](https://elektrotechniek.keesvanwanrooij.nl/) | [cursus-elektrotechniek](https://github.com/keesvanwanrooij/cursus-elektrotechniek) |
| Cursus CV-ketels | [cv-ketels.keesvanwanrooij.nl](https://cv-ketels.keesvanwanrooij.nl/) | [cursus-cv-ketels](https://github.com/keesvanwanrooij/cursus-cv-ketels) |

Voor Google is `www.keesvanwanrooij.nl` één website: de hub plus de methode. De cursussen zijn voor Google aparte sites, elk met een eigen `sitemap.xml`, `robots.txt` en Search Console property. Ze worden vanaf dit domein nergens gelinkt; zij linken alleen met één regel "Gemaakt door Kees van Wanrooij" terug.

DNS bij TransIP: `@` met vier A- en vier AAAA-records naar GitHub Pages, en CNAME-records `www`, `elektrotechniek` en `cv-ketels` naar `keesvanwanrooij.github.io.`.

De hub en de methode delen het ecosysteemblok in de voettekst (Beleggen, Meer over beleggen, Onderzoek en tools, Kees van Wanrooij). Wijzig je de lijst, pas dan `tools/build-chrome.py` hier en `site/build.py` (`ECO`) in de methode allebei aan. Elke kolom heeft maximaal vier links.

Komen de Insider Scanner of de Stock Screener als eigen GitHub Pages-site online, noem de repository dan `insider-scanner` of `stock-screener` (zonder `bk-`), zodat hij op hetzelfde pad komt te staan als de uitlegpagina hier. Een project-site gaat voor op een map met dezelfde naam in de hub; verwijder dan de map hier en houd `sitemap-site.xml` en `tools/build-sitemap.py` bij.

## Opbouw

Gewone HTML en CSS, geen JavaScript in de pagina's zelf (het mobiele menu is een CSS-only checkbox-truc) en geen afhankelijkheden. Kop en voet komen uit één bron: draai na een wijziging `python tools/build-chrome.py`. Alle paden beginnen met `/`, dus de site werkt vanaf de root van een domein.

```text
index.html                             home
beleggen/index.html                    Beleggen met GARP en NLP (met FAQ)
welke-kees/index.html                  wie Belegger Kees is, en wie niet (met FAQ)
veelgestelde-vragen/index.html         alle FAQ's op een plek (met FAQ-schema)
over-mij/index.html                    achtergrond en verhaal
insider-scanner/index.html             uitleg Insider Scanner (tool in ontwikkeling)
stock-screener/index.html              uitleg Stock Screener (tool in ontwikkeling)
projecten/, cursussen/, elektrotechniek/, cv-ketels/, projecten/elektrotechniek/, projecten/cv-ketels/
                                       oude adressen: onzichtbare doorstuurpagina's
voortgang-overzetten.html              technische brug: zet cursusvoortgang over naar de subdomeinen
404.html                               foutpagina
assets/css/style.css        alle stijlen en tokens
assets/fonts/               Inter en JetBrains Mono, zelf gehost
assets/img/                 portret en deelafbeelding (og.png)
tools/og.html               bron van og.png, zie het commentaar in het bestand
tools/build-chrome.py       zet de gedeelde kop en voet in alle pagina's
tools/build-sitemap.py      bouwt sitemap.xml en sitemap/index.html (hub plus methode)
sitemap/index.html          leesbaar overzicht van alle pagina's, gegroepeerd per site
sitemap.xml                 platte lijst met alle pagina's van www.keesvanwanrooij.nl
sitemap-site.xml            brondata: alleen de eigen pagina's van deze site
robots.txt, llms.txt
```

Lokaal bekijken:

```bash
python -m http.server 8123
```

Open daarna http://localhost:8123/.

## Sitemaps en robots.txt

Alleen de `robots.txt` in de root van een host wordt door zoekmachines gelezen. Voor `www.keesvanwanrooij.nl` is dat die in deze repository; de `robots.txt` in de methode is alleen informatief. De cursussen staan op een eigen subdomein en hun eigen `robots.txt` telt daar wel.

`sitemap.xml` is één platte lijst met **alle pagina's van www.keesvanwanrooij.nl**: deze site plus de Belegger Kees Methode. De cursussen staan er bewust niet in. `tools/build-sitemap.py` bouwt hem: hij haalt de `sitemap.xml` van de methode live op (de hub heeft geen lokale toegang tot die broncode), haalt per pagina de `<title>` op om er een leesbare `/sitemap/`-pagina bij te maken, schrijft beide bestanden opnieuw en draait daarna `tools/build-chrome.py` voor de kop en voet.

```bash
python tools/build-sitemap.py
```

We probeerden eerst een sitemapindex (`sitemap.xml` die alleen naar de losse sitemaps wijst), maar die losse sitemaps van de andere sites werden in de praktijk nooit gezien: `https://www.keesvanwanrooij.nl/belegger-kees-methode/sitemap.xml` stond alleen als aparte `Sitemap:`-regel in `robots.txt` en werd niet als submap van een geregistreerde sitemap gecrawld. Eén platte lijst met alle URL's, plus een HTML-pagina vol interne links naar elke pagina, is voor deze site simpeler en geeft Google meer om aan te haken. Registreer `https://www.keesvanwanrooij.nl/sitemap.xml` in Search Console.

`.github/workflows/refresh-sitemap.yml` draait dit script automatisch, dagelijks en handmatig via "Run workflow", en committet het resultaat als er iets veranderd is. Dat vereist dat Actions in deze repository schrijfrechten heeft: **Settings → Actions → General → Workflow permissions → "Read and write permissions"**. Staat dat nog op read-only, dan faalt de commit-stap zichtbaar in de Action-log; de rest van de site blijft gewoon werken.

`sitemap-site.xml` blijft de handmatig onderhouden brondata voor de eigen pagina's van de hub: `tools/build-sitemap.py` leest die uit, in plaats van zelf de hele repository te scannen. Voeg je een pagina toe, werk dan eerst `sitemap-site.xml` bij en draai daarna het script.

De doorstuurpagina's (`projecten/`, `cursussen/`, `elektrotechniek/`, `cv-ketels/` en de twee onder `projecten/`) staan op `noindex, follow` met een `canonical` naar het nieuwe adres en een meta refresh: naar de homepage, of naar het subdomein van de cursus. GitHub Pages kan geen serverredirect, dus dit is de dichtstbijzijnde vervanging van een 301. Ze worden nergens gelinkt. Zet ze niet in `sitemap-site.xml`.

`voortgang-overzetten.html` is geen pagina voor bezoekers. De cursussen bewaren de voortgang in `localStorage`, en die hoort bij een origin. Toen de cursussen nog op `www.keesvanwanrooij.nl/cursus-.../` stonden, stond de voortgang dus onder deze origin. Een cursus op zijn nieuwe subdomein laadt deze pagina eenmalig onzichtbaar, vraagt de voortgang op en ruimt de oude service worker op. De pagina antwoordt alleen aan de twee cursusdomeinen. Laat hem staan zolang er nog bezoekers van voor de verhuizing kunnen terugkomen.

## Huisstijl en regels

De stijl volgt het Belegger Kees ontwerpsysteem: wit en Apple-grijs, deep carbon `#1D1D1F`, execution red `#C4303C` als zeldzaam accent (hoogstens een rode knop per scherm), Inter voor tekst en JetBrains Mono voor cijfers, geen donkere modus. Tokens staan bovenaan `assets/css/style.css`.

Voor teksten gelden dezelfde regels als bij Belegger Kees: educatie en geen advies, geen verboden woorden, geen lang streepje, en nooit een cijfer, bron, datum of citaat verzinnen. Een pagina met financiële inhoud draagt de lange disclaimer, letterlijk.

## Repositories openbaar maken

De Belegger Kees Methode is openbaar en staat als Live op de home en op `beleggen/`. De Insider Scanner en de Stock Screener zijn nog privé. Ze hebben elk een uitlegpagina (`/insider-scanner/`, `/stock-screener/`) en een kaart met het label "In ontwikkeling", zonder link naar de repository, zodat bezoekers geen 404 zien. Wordt een van beide openbaar:

1. Vervang op `index.html` (sectie "Waar ik aan werk") en `beleggen/index.html` (sectie "Tools en publicaties") het label door "Live" en zet een link naar de repository in de kaart.
2. Pas de statusregel op de uitlegpagina aan en zet de link naar GitHub erbij. Krijgt de tool een eigen GitHub Pages-site, zie dan de opmerking over de reponaam onder "Domeinen en repository's".
3. Voeg de link toe aan `llms.txt`.
4. Werk `lastmod` in `sitemap-site.xml` bij, "Bijgewerkt" op de pagina, en draai daarna `python tools/build-sitemap.py`.

## Nog te doen na de lancering van beleggerkees.nl

Zodra de nieuwe Astro-site live is (`/over`, `/auteur/kees-van-wanrooij`, `/redactioneel` en `/aandelen` geven nu nog 404):

- Link vanaf `over-mij/` naar de auteurspagina en voeg die toe aan `sameAs` in de Person-gegevens.
- Link vanaf `beleggen/` naar `/aandelen` en `/redactioneel`.
- Vraag vanaf beleggerkees.nl een link terug naar deze site (voorkeur: de auteurspagina en de voettekst).

## Lettertypen

Inter en JetBrains Mono worden gedistribueerd onder de SIL Open Font License 1.1. De bestanden in `assets/fonts/` zijn de Latin-subsets, gekopieerd uit de build van beleggerkees.nl.

## Auteur

Kees van Wanrooij. Educatie, geen beleggingsadvies.
