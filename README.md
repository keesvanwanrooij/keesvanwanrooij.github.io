# keesvanwanrooij.github.io

Persoonlijke merkwebsite van Kees van Wanrooij, belegger en NLP-practitioner, oprichter van Belegger Kees.

Live op https://keesvanwanrooij.github.io/

De site is de centrale hub die naar de projecten linkt: [Belegger Kees](https://beleggerkees.nl), de gratis [Cursus Elektrotechniek](https://keesvanwanrooij.github.io/cursus-elektrotechniek/) en, zodra ze openbaar zijn, de Belegger Kees Methode en de Insider scanner. Klimaat en HVAC volgt.

## Opbouw

Gewone HTML en CSS, geen build-stap, geen JavaScript en geen afhankelijkheden. Alle paden beginnen met `/`, dus de site werkt vanaf de root van een domein.

```text
index.html                  home
beleggen/index.html         Beleggen met GARP en NLP (met FAQ)
elektrotechniek/index.html  landingspagina voor de cursus
over-mij/index.html         achtergrond en verhaal
404.html                    foutpagina
assets/css/style.css        alle stijlen en tokens
assets/fonts/               Inter en JetBrains Mono, zelf gehost
assets/img/                 portret en deelafbeelding (og.png)
tools/og.html               bron van og.png, zie het commentaar in het bestand
sitemap.xml, robots.txt, llms.txt
```

Lokaal bekijken:

```bash
python -m http.server 8123
```

Open daarna http://localhost:8123/.

## Huisstijl en regels

De stijl volgt het Belegger Kees ontwerpsysteem: wit en Apple-grijs, deep carbon `#1D1D1F`, execution red `#C4303C` als zeldzaam accent (hoogstens een rode knop per scherm), Inter voor tekst en JetBrains Mono voor cijfers, geen donkere modus. Tokens staan bovenaan `assets/css/style.css`.

Voor teksten gelden dezelfde regels als bij Belegger Kees: educatie en geen advies, geen verboden woorden, geen lang streepje, en nooit een cijfer, bron, datum of citaat verzinnen. Een pagina met financiële inhoud draagt de lange disclaimer, letterlijk.

## Repositories openbaar maken

De Belegger Kees Methode en de Insider scanner staan op privé. Op de site hebben ze een kaart met het label "Binnenkort openbaar" en zonder link, zodat bezoekers geen 404 zien. Wordt een repository openbaar:

1. Vervang op `index.html` (sectie "Open projecten") en `beleggen/index.html` (sectie "Tools en open projecten") het label door "Live".
2. Verwijder de regel "Zodra de repository openbaar is, staat hier de link." en zet een link naar de repository in de kaart.
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
