# Vaatimusmäärittely

## Sovelluksen tarkoitus

Käyttäjä voi luoda sovelluksessa budjetin ja seurata rahavirtaansa jollakin ajanjaksolla (esim. kuukausi). Käyttäjä voi luoda budjettiin menoja ja tuloja.

## Käyttäjät

Sovelluksella on yksi käyttäjärooli, normaali käyttäjä.

## Käyttöliittymä

Sovelluksessa on alustavasti kaksi eri näkymää:

1. Aloitusnäkymä
- Sovellus aukeaa aloitusnäkymään, eli overview-näkymään kaikista budjeteista.
  - Tämä voi muuttua myöhemmin, ks. jatkokehitysideoita-kohdan mahdollisuus useammalle käyttäjälle.
- Käyttäjä voi navigoida tästä spesifisen budjetin näkymään

2. Budjetin sisäinen näkymä
- Käyttäjä näkee budjetin sisältämät menot ja tulot ja voi luoda niitä
- Näkymä sisältää menojen ja tulojen määrät sekä niiden yhteisen summan

## Suunnitellut toiminnallisuudet

Perusversio tarjoaa seuraavat toiminnallisuudet:

- Budjetin luominen
  - Budjetille annetaan luotaessa nimi, esimerkiksi "Rauno Rupikonnan tammikuun budjetti"
- Menojen ja tulojen luominen budjettiin
  - Luotaessa määritellään, onko luotava asia meno vai tulo, ja annetaan sille
  nimi ja rahamäärä
  - Sovellus tarkistaa, että annettu rahamäärä on kelvollinen (positiivinen luku)
- Sovellus laskee ja näyttää budjetin rahatilanteen eli tulojen ja menojen summan
- Budjetin tai menon/tulon poisto

## Jatkokehitysideoita
- Menojen ja tulojen määrien värikoodaus käyttöliittymässä (menot punaisella, tulot vihreällä) 
- Mahdollisuus asettaa päivämäärä menoa tai tuloa luotaessa
  - Auttaisi paremmin hahmottamaan rahan liikkumisen kuun mittaan 
- Tuki usealle käyttäjälle
  - Sovelluksen käyttöliittymän aloitusnäkymä vaihtuisi kirjautumisnäkymäksi 
  - Tämä voisi olla jo perustoteutuksessa, mutta mielestäni on olennaisempaa priorisoida ensin riittävä käytettävyys yhden käyttäjän kohdalla
- Tulon tai menon määrittely kiinteäksi
  - Kiinteät tulot, kuten palkka tai opintotuki, tai kiinteät menot, kuten vuokra, olisi mahdollista kopioida seuraavan kuun budjettia luodessa käytön kätevöittämiseksi
- Budjetin sisältöä (budjetin nimi, menon nimi tai rahamäärä, tulon nimi tai rahamäärä) voisi muokata
  - Käyttötarkoitus: Käyttäjä tekee esimerkiksi kirjoitusvirheen menon nimessä tai rahamäärässä
- Säästöt-kategorian lisäys
  - Säästöt ovat menoja, jotka jaettaisiin omaan kategoriaansa rahavirtojen tarkemman seuraamisen saavuttamiseksi. Esim. Nordnet-kuukausisäästösumma, käteispuskuriin menevä kuukausittainen summa
  - Käyttäjä pystyisi näkemään, kuinka suuri osuus tuloista menee säästöihin ja muihin menoihin (esim. ei-säästöjen
    osuus tuloista: 86%
  - Käyttäjä voisi luoda säästötavoitteen, esim. säästöjen osuus min. 10% tuloista. Sovellus kertoo, onko säästötavoite saavutettu
