# Viikko 3

### Mitä olen tehnyt tällä viikolla?
Tutustuin Damerau-Levenshtein-etäisyyteen ja toteutin algoritmin ensimmäisen version. Lisäsin check-endpointin, jolla mahdollistetaan sanojen reaaliaikainen tarkastus. Lisäsin myös joitain tyylejä ja vaihdoin yksittäisen input-kentän textareaksi, johon käyttäjä voi kirjoittaa enemmän tekstiä kerrallaan. Jos sanaa ei löydy triestä, se merkitään punaisella värillä.
Lopuksi lisäsin Pylint sekä Codecov -workflowt, jotka ajetaan automaattisesti mainiin pushaamisen yhteydessä, ja tulokset näytetään READMEn badgessa. Kirjoitin myös puuttuvat testit, korjasin Pylintin huomiot, ja aloitin testausraportin kirjoittamisen.

### Miten ohjelma on edistynyt?
Ohjelma on edistynyt aikataulussa.

### Mitä opin tällä viikolla / tänään?
Opin hahmottamaan Damerau-Lehvensteinin toiminnan paremmin.

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Ei mikään toistaiseksi. Mallinsin Damerau-Levenshteinin tuottamaa matriisia kynällä ja paperilla, jolloin se oli helpompi hahmottaa.

### Mitä teen seuraavaksi?
Alan suunnittelemaan sitä, miten yhdistän trien ja etäisyyksien laskennan. En vielä tiedä tarkasti, miten trien rakennetta voi hyödyntää sanaston läpikäyntiin sen sijaan, että vertaisi jokaista sanaa yksi kerrallaan etäisyyksiä laskiessa. Trien kokonaisia haaroja voi varmastikin hylätä kerralla kun huomataan, että mikään yksittäisen noden alla olevista sanoista ei enää voisi olla tarpeeksi lähellä korjattavaa sanaa.

---

### Käytetty aika
7h