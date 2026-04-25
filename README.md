[![Pylint](https://github.com/avanine/spell-checker/actions/workflows/pylint.yml/badge.svg)](https://github.com/avanine/spell-checker/actions/workflows/pylint.yml)
[![codecov](https://codecov.io/gh/avanine/spell-checker/graph/badge.svg)](https://codecov.io/gh/avanine/spell-checker)

# Kirjoitusvirheiden korjaaja

Tämä projekti on Helsingin yliopiston Algoritmit ja tekoäly -kurssin harjoitustyö. Ohjelma tunnistaa väärin kirjoitettuja sanoja ja ehdottaa niille korjauksia sanakirjan perusteella. Toiminnallisuus toteutetaan tallentamalla sanat itse toteutettuun trie-tietorakenteeseen ja vertaamalla sanojen Damerau-Levenshtein-etäisyyttä.

<img width="966" height="513" alt="image" src="https://github.com/user-attachments/assets/0811a07f-2d57-4122-9e18-267799827951" />

## Dokumentaatio
- [Määrittelydokumentti](./docs/maarittelydokumentti.md)
- [Testausraportti](./docs/testausraportti.md)
- [Toteutusdokumentti](./docs/toteutusdokumentti.md)
- [Käyttöohje](./docs/kayttoohje.md)

## Viikkoraportit
- [Viikko 1](./docs/viikkoraportit/viikko1.md)
- [Viikko 2](./docs/viikkoraportit/viikko2.md)
- [Viikko 3](./docs/viikkoraportit/viikko3.md)
- [Viikko 4](./docs/viikkoraportit/viikko4.md)
- [Viikko 5](./docs/viikkoraportit/viikko5.md)
- [Viikko 6](./docs/viikkoraportit/viikko6.md)

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
