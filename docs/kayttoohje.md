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

<img width="939" height="439" alt="image" src="https://github.com/user-attachments/assets/8df44a3c-77f4-437e-9908-fa3d9e4aeb47" />

---

Klikkaa korostettua sanaa nähdäksesi korjausehdotukset. Ehdotukset näkyvät tekstikentän alla järjestettynä lähimmästä vastaavuudesta kauimpaan. Sanojen yleisyys otetaan huomioon ehdotuksissa.

<img width="923" height="500" alt="image" src="https://github.com/user-attachments/assets/436a146b-1cac-43c2-8f46-369ad9ef660c" />

---

Klikkaa ehdotusta korvataksesi väärin kirjoitetun sanan. Jos sana on oikein mutta sitä ei löydy sanakirjasta, voit lisätä sen sanakirjaan klikkaamalla **+ Add to dictionary**. Tämän jälkeen sovellus tunnistaa sen oikein kirjoitetuksi session ajan.

<img width="896" height="438" alt="image" src="https://github.com/user-attachments/assets/76b139b4-09c8-4ee2-979a-f3f9cfbc16cb" />
