[![Pylint](https://github.com/avanine/spell-checker/actions/workflows/pylint.yml/badge.svg)](https://github.com/avanine/spell-checker/actions/workflows/pylint.yml)

# Kirjoitusvirheiden korjaaja

Tämä projekti on Helsingin yliopiston Algoritmit ja tekoäly -kurssin harjoitustyö. Ohjelma tunnistaa väärin kirjoitettuja sanoja ja ehdottaa niille korjauksia sanakirjan perusteella. Toiminnallisuus toteutetaan tallentamalla sanat itse toteutettuun trie-tietorakenteeseen ja vertaamalla sanojen Damerau-Levenshtein-etäisyyttä.

## Dokumentaatio
- [Määrittelydokumentti](./docs/maarittelydokumentti.md)

## Viikkoraportit
- [Viikko 1](./docs/viikkoraportit/viikko1.md)
- [Viikko 2](./docs/viikkoraportit/viikko2.md)
- [Viikko 3](./docs/viikkoraportit/viikko3.md)

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
Testikattavuusraportin saa generoitua komennoilla
```bash
poetry run coverage run --branch -m pytest tests
```
```bash
poetry run coverage report -m
```
