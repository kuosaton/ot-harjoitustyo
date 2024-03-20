# Vaatimusmäärittely

## Sovelluksen tarkoitus

Käyttäjä voi luoda sovelluksessa budjetin ja seurata rahavirtaansa jollakin ajanjaksolla. Käyttäjä lisää budjettiin
menoja ja tuloja.

## Käyttäjät

Sovelluksella on yksi käyttäjärooli, normaali käyttäjä.

## Suunnitellut toiminnallisuudet

Perusversio tarjoaa seuraavat toiminnallisuudet:

- Budjetin luominen
  - Budjetille annetaan luotaessa nimi, esimerkiksi "Rauno Rupikonnan tammikuun budjetti"
- Menojen ja tulojen luominen budjettiin
  - Luotaessa määritellään, onko luotava asia meno vai tulo, ja annetaan sille
  nimi ja rahamäärä
  - Sovellus tarkistaa, että annettu rahamäärä on positiivinen luku
- Sovellus näyttää budjetin rahatilanteen eli tulojen ja menojen summan
- Menoja ja tuloja voi poistaa budjetista
- Budjetin voi poistaa

## Jatkokehitysideoita
- Mahdollisuus antaa menolle tai tulolle luotaessa päivämäärä
  - Auttaisi paremmin hahmottamaan rahan liikkumisen kuun mittaan 
- Mahdollisuus useammalle käyttäjälle
  - Tämä voisi olla jo perustoteutuksessa, mutta mielestäni on olennaisempaa
  priorisoida ensin riittävä käytettävyys yhden käyttäjän kohdalla. Budjetoinnissa on hyödyllistä pystyä tekemään useammalle kuulle omat budjettinsa
- Tulon tai menon määrittely kiinteäksi
  - Kiinteät tulot, kuten palkka tai opintotuki, tai kiinteät menot, kuten vuokra, olisi mahdollista kopioida
    seuraavan kuun budjettiin
- Budjetin sisältöä (budjetin nimi, menon nimi tai rahamäärä, tulon nimi tai rahamäärä) voisi muokata
  - Käyttötarkoitus: Käyttäjä tekee esimerkiksi kirjoitusvirheen menon nimessä tai rahamäärässä
- Säästöt-kategorian lisäys: säästöt ovat menoja, mutta ne jaettaisiin omaan kategoriaansa rahavirtojen tarkemman
  seuraamisen saavuttamiseksi
  - Esim. Nordnet-kuukausisäästösumma, käteispuskuriin menevä kuukausittainen summa
  - Käyttäjä pystyisi näkemään, kuinka suuri osuus tuloista menee säästöihin ja muihin menoihin (esim. ei-säästöjen
    osuus tuloista: 86%
    - Käyttäjä voisi luoda säästötavoitteen, esim. säästöjen osuus min. 10% tuloista. Sovellus kertoo, onko säästötavoite saavutettu
