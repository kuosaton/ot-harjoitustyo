# Vaatimusmäärittely

Tehdyt toiminnallisuudet on merkitty täytetyllä checkmark:lla, tekemättömät täyttämättömällä.

## Sovelluksen tarkoitus

Käyttäjä voi luoda sovelluksessa budjetin ja seurata rahavirtaansa jollakin ajanjaksolla (esim. kuukausi). Käyttäjä voi luoda budjettiin menoja ja tuloja.

## Käyttäjät

- [x] Sovelluksella on yksi käyttäjärooli, normaali käyttäjä.

## Käyttöliittymä

Sovelluksessa on alustavasti kaksi eri näkymää:

- [x] 1. Aloitusnäkymä
  - [x] Näkymässä voi luoda uuden budjetin
  - [x] Näkymässä voi luoda useamman budjetin ja budjetteihin voi siirtyä

- [x] 2. Budjetin sisäinen näkymä
  - [x] Käyttäjä näkee budjetin sisältämät menot ja tulot ja voi luoda niitä
  - [x] Näkymä sisältää menojen ja tulojen määrät sekä niiden yhteisen summan

## Suunnitellut toiminnallisuudet

Perusversio tarjoaa seuraavat toiminnallisuudet:

- [x] Budjetin luominen
  - [x] Budjetille annetaan luotaessa nimi, esimerkiksi "Rauno Rupikonnan tammikuun budjetti"
- [x] Menojen ja tulojen luominen budjettiin
  - [x] Luotaessa määritellään, onko luotava kirjaus meno vai tulo, ja annetaan sille nimi ja rahamäärä
  - [x] Sovellus tarkistaa, että annetut syötteet ovat kelvollisia
- [x] Sovellus laskee ja näyttää budjetin rahatilanteen eli tulojen ja menojen summan
- [x] Budjetin tai menon/tulon poisto
- [x] Kirjausten pysyvä tallennus

## Jatkokehitysideoita
- Menojen ja tulojen määrien värikoodaus käyttöliittymässä (menot punaisella, tulot vihreällä) 
- Mahdollisuus asettaa päivämäärä menoa tai tuloa luotaessa
  - Auttaisi paremmin hahmottamaan rahan liikkumista kuun mittaan 
- Budjetin sisältöä (budjetin nimi, menon nimi tai rahamäärä, tulon nimi tai rahamäärä) voisi muokata
  - Esimerkkikäyttötarkoitus: Käyttäjä tekee kirjoitusvirheen 
- Säästöt-kategoria
  - Säästöt ovat menoja, jotka jaettaisiin omaan kategoriaansa rahavirtojen tarkemman seuraamisen saavuttamiseksi. Esim. Nordnet-kuukausisäästösumma, käteispuskuriin menevä kuukausittainen summa
  - Käyttäjä pystyisi näkemään, kuinka suuri osuus tuloista menee säästöihin ja muihin menoihin (esim. ei-säästöjen
    osuus tuloista: 86%
  - Käyttäjä voisi luoda säästötavoitteen, esim. säästöjen osuus min. 10% tuloista. Sovellus kertoo, onko säästötavoite saavutettu
