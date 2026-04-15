# Viikko 4

### Mitä olen tehnyt tällä viikolla?
Lisäsin suggest-endpointin, joka palauttaa korjausehdotukset. Toin korjausehdotukset näkyville käyttöliittymään sanaa klikkaamalla. Järjestin ehdotukset lähimmästä kauimpaan ja rajoitin näytettävien ehdotusten määrän max 5 kappaleeseen. Kirjoitin alustavan toteutusdokumentin. Lisäsin testin, joka mittaa kuinka kauan kestää löytää ehdotukset annetulle väärinkirjoitetulle sanalle. Optimoin ehdotusten hakua trie-pohjaisella karsinnalla. Aiempi toteutus kävi läpi sanakirjan jokaisen sanan yksi kerrallaan, kun taas nykyinen versio karsii kokonaisia trien haaroja. Päivitin myös toteutusdokumentin vastaamaan tämänhetkistä toteutusta.

### Miten ohjelma on edistynyt?
Ehdotusten hakuun tuli suuri parannus 0.91 sekunnista 0.01 sekuntiin. Tämä oli päätavoitteena, joten ohjelma on edistynyt ihan hyvin.

### Mitä opin tällä viikolla / tänään?
Opin miten ehdotusten laatua voi parantaa.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Ei mikään tällä hetkellä.

### Mitä teen seuraavaksi?
Optimoin algoritmia ja parannan trieä siten, että jokaista sanaa ei tarvitse vertailla yksi kerrallaan. Vaihdan todennäköisesti sanalistan sellaiseksi, joka sisältää yleisyystiedon, jotta ehdotukset olisivat osuvampia.

---

### Käytetty aika
6h