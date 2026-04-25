# Käyttöohje

## Sovelluksen käynnistäminen

Asenna riippuvuudet:
```bash
poetry install
```

Käynnistä sovellus:
```bash
poetry run python src/spell_checker/app.py
```

Avaa selaimessa osoite http://127.0.0.1:5001

## Käyttö

Kirjoita tekstiä tekstikenttään. Sovellus tarkistaa sanat automaattisesti kun sanan jälkeen painetaan välilyöntiä. Väärin kirjoitetut sanat korostetaan violetilla taustalla. Voit myös copypasteta pidemmän tekstin tekstikenttään.

Klikkaa korostettua sanaa nähdäksesi korjausehdotukset. Ehdotukset näkyvät tekstikentän alla järjestettynä lähimmästä vastaavuudesta kauimpaan. Sanojen yleisyys otetaan huomioon ehdotuksissa.

Klikkaa ehdotusta korvataksesi väärin kirjoitetun sanan. Jos sana on oikein mutta sitä ei löydy sanakirjasta, voit lisätä sen sanakirjaan klikkaamalla "+ Add to dictionary". Tämän jälkeen sovellus tunnistaa sen oikein kirjoitetuksi session ajan.
