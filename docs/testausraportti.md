# Testausraportti

## Yksikkötestauksen kattavuusraportti
<img width="978" height="349" alt="coverage" src="https://github.com/user-attachments/assets/e904ae7a-ce72-4648-acaa-7874ecc5c205" />

## Mitä on testattu

### Trie

- **Sanojen lisääminen ja haku**: Testattu, että trieen lisätyt sanat ("sanakirja", "kissa", "koira") löytyvät haulla. Testattu myös, että sanat joita ei ole lisätty ("sana", "kilpikonna") palauttavat False.
- **Tyhjä trie**: Testattu, että tyhjästä triestä haku palauttaa aina False.
- **Iteraattori**: Testattu, että sortattu trie on oikean muotoinen.

### Damerau-Levenshtein

- **Kaikki neljä operaatiota**: Testattu, että kirjaimen lisääminen, poistaminen, vaihtaminen, sekä transpositio toimivat oikein.
- **Tyhjät syötteet**: Testattu, että kahden tyhjän merkkijonon välinen etäisyys on 0. Testattu myös, että tyhjän merkkijonon ja ei-tyhjän merkkijonon välinen etäisyys on ei-tyhjän merkkijonon pituus.
- **Identtiset sanat**: Testattu, että kahden identtisen merkkijonon välinen etäisyys on 0.
- **Usea muokkaus**: Testattu, että useamman muokkauksen vaativat sanat palauttavat oikean etäisyyden.

### Sanojen korjausehdotukset

- Sana löytyy sanakirjasta
- Sanaa ja kahden operaation etäisyydellä olevaa ehdotusta ei löydy sanakirjasta
- Transposition vaativa ehdotus löytyy
- Yhden muokkauksen vaativa ehdotus löytyy

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
