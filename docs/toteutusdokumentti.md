# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma koostuu neljästä päämoduulista:

- **trie.py**: Trie-tietorakenne, joka tallentaa sanakirjan sanat. Tukee sanojen lisäämistä (insert), hakua (search) ja iterointia generaattorin avulla (\_\_iter__, _collect_words).
- **damerau_levenshtein.py**: Laskee kahden sanan välisen Damerau-Levenshtein-etäisyyden. Algoritmi tukee neljää operaatiota: lisäys, poisto, korvaus ja transpositio.
- **suggestions.py**: Hakee korjausehdotuksia vertaamalla annettua sanaa kaikkiin trien sanoihin ja palauttaa lähimmät vastineet etäisyyden mukaan järjestettynä.
- **app.py**: Flask-sovellus, joka tarjoaa käyttöliittymän kirjoitusvirheiden tarkistukseen. Sisältää kaksi endpointia: /check tarkistaa sanojen oikeinkirjoituksen ja /suggest palauttaa korjausehdotukset.

Käyttöliittymä on toteutettu HTML/CSS/JavaScript-pohjaisena. Käyttäjä kirjoittaa tekstiä textarea-kenttään, ja väärin kirjoitetut sanat korostetaan reaaliaikaisesti. Korjausehdotukset haetaan klikkaamalla korostettua sanaa.

## Puutteet ja parannukset
- algoritmin optimointi
- sanakirjan vaihtaminen sellaiseen, joka sisältää yleisyystiedon
- käyttöliittymän hiominen

## Laajojen kielimallien käyttö

**ChatGPT-5.3**
- Damerau-Levenshtein-etäisyyden ymmärtäminen: pyydetty selittämään miten algoritmi toimii, tarkentaen epäselvimpiä kohtia
- koodin toiminnallisuuden tarkistus
- aikataulutuksessa auttaminen

## Lähteet
- https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
- https://en.wikipedia.org/wiki/Trie
- https://www.reddit.com/r/leetcode/comments/1exqiph/a_visual_guide_to_tries/