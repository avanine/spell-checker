# Kirjoitusvirheiden korjaaja

Tämä projekti on Helsingin yliopiston Algoritmit ja tekoäly -kurssin harjoitustyö. Ohjelma tunnistaa väärin kirjoitettuja sanoja ja ehdottaa niille korjauksia sanakirjan perusteella. Toiminnallisuus toteutetaan tallentamalla sanat itse toteutettuun trie-tietorakenteeseen ja vertaamalla sanojen Damerau-Levenshtein-etäisyyttä.

## Dokumentaatio
- [Määrittelydokumentti](./docs/maarittelydokumentti.md)

## Viikkoraportit
- [Viikko 1](./docs/viikkoraportit/viikko1.md)

## Sovelluksen käynnistäminen

Projekti käyttää Poetryä riippuvuuksien hallintaan.

Asenna riippuvuudet komennolla
```bash
poetry install
```
Käynnistä sovellus komennolla
```bash
poetry run python src/spell_checker/app.py
```
