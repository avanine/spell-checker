# Määrittelydokumentti

## Perustiedot

**Opinto-ohjelma:** TKT

**Ohjelmointikieli:** Python

**Dokumentaation kieli:** suomi

**Pystyn vertaisarvioimaan myös seuraavilla kielillä tehtyjä projekteja (tarvittaessa muitakin):** Java, TypeScript

## Ohjelman toiminnallisuus

Ohjelma korjaa kirjoitusvirheitä. Käyttäjä syöttää tekstiä, jota ohjelma tarkistaa. Se tunnistaa väärin kirjoitetun sanan ja ehdottaa sille oikeaa kirjoitusasua. Ohjelma vertaa syötettyä sanaa sanakirjaan tallennettuihin sanoihin ja palauttaa lähimmät vastineet havaitessaan kirjoitusvirheen.

## Algoritmit ja tietorakenteet

### Trie-tietorakenne

Sanakirjan sanat tallennetaan itse toteutettuun trie-tietorakenteeseen, joka mahdollistaa sanojen tehokkaan tallennuksen ja haun. Trie soveltuu tähän erityisen hyvin, koska sanat jakavat usein yhteisiä alkuosia.

### Damerau-Levenshtein-etäisyys

Käyttäjän syöttämän sanan ja sanakirjan sanojen välistä etäisyyttä mitataan Damerau-Levenshtein-etäisyydellä. Tämä etäisyysmitta huomioi neljä operaatiota:

1. Merkin lisäys (insertion)
2. Merkin poisto (deletion)
3. Merkin korvaus (substitution)
4. Kahden vierekkäisen merkin vaihto keskenään (transposition)

Tämä on hyvä kirjoitusvirheiden tunnistamiseen, koska tavallisimmat kirjoitusvirheet johtuvat ylimääräisestä tai puuttuvasta merkistä, väärästä kirjaimesta tai kahden vierekkäisen kirjaimen vaihtumisesta keskenään.

## Aika- ja tilavaativuudet

### Trie

- **Sanan lisäys:** O(m), missä m on sanan pituus.
- **Sanan haku:** O(m), missä m on sanan pituus.
- **Tilavaativuus:** Pahimmassa tapauksessa O(n * m), missä n on sanojen määrä ja m on sanan keskipituus. Käytännössä trie säästää tilaa, koska sanat jakavat yhteisiä alkuosia.

### Damerau-Levenshtein-etäisyys

- **Aikavaativuus:** O(m * n) kahdelle sanalle, joiden pituudet ovat m ja n. Tämä johtuu siitä, että algoritmi täyttää (m+1) x (n+1) -kokoisen matriisin, jossa jokainen solu lasketaan vakioajassa edellisten solujen arvoista.
- **Tilavaativuus:** O(m * n)

## Harjoitustyön ydin

Työn ydin on Damerau-Levenshtein-etäisyyden laskenta ja trie-tietorakenteen toteutus sanojen tallentamiseen. Ohjelman keskeinen haaste on löytää oikeat korjausehdotukset tehokkaasti suuresta sanakirjasta. Suurin osa kehitysajasta käytetään näiden toteuttamiseen ja optimointiin.

## Lähteet

- [Wikipedia: Damerau-Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Geeks for Geeks: Damerau-Levenshtein distance](https://www.geeksforgeeks.org/damerau-levenshtein-distance/)
- [Wikipedia: Trie](https://en.wikipedia.org/wiki/Trie)
