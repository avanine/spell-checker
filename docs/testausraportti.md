# Testausraportti

## Yksikkötestauksen kattavuusraportti

Damerau-Levenshtein-algoritmin testit puuttuvat vielä, ne lisätään seuraavaksi.

## Mitä on testattu

### Trie

- **Sanojen lisääminen ja haku**: Testattu, että trieen lisätyt sanat ("sanakirja", "kissa", "koira") löytyvät haulla. Testattu myös, että sanat joita ei ole lisätty ("sana", "kilpikonna") palauttavat False.
- **Tyhjä trie**: Testattu, että tyhjästä triestä haku palauttaa aina False.

## Miten testit voidaan toistaa

Asenna riippuvuudet:
```bash
poetry install
```

Aja testit ja generoi kattavuusraportti:
```bash
poetry run coverage run --branch -m pytest tests
poetry run coverage report -m
```