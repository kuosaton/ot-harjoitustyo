# Budjetointisovellus
Sovelluksen avulla käyttäjän on mahdollista luoda ja nimetä budjetti, kirjata siihen tuloja ja menoja sekä seurata rahatilannettaan. 

## Python-versio
> [!NOTE]
> Sovellus on testattu versiolla `Python 3.10.12` käyttäen [Cubbli](https://helpdesk.it.helsinki.fi/ohjeet/muut-ohjeet/cubbli-helsingin-yliopistossa)-käyttöjärjestelmän fuksiläppäriä sekä [virtuaalityöasemaa](https://vdi.helsinki.fi/). 

## Dokumentaatio
- [Vaatimusmäärittely](budjetointisovellus/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](budjetointisovellus/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](budjetointisovellus/dokumentaatio/tuntikirjanpito.md)
- [Changelog](budjetointisovellus/dokumentaatio/changelog.md)

## Asennus

1. Lataa projektin lähdekoodi:
- Navigoi osion [release](https://github.com/kuosaton/ot-harjoitustyo/releases) viimeisimpään releaseen.
- Valitse releasen Assets-osiosta *Source code*-tiedosto ladattavaksi.
- Pura pakattu projektin sisältö ja siirry projektin hakemiston kansioon /budjetointisovellus/.
      
2. Asenna riippuvuudet komennolla:

```
poetry install
```

Tämän jälkeen voit siirtyä alla oleviin komentorivitoimintoihin ohjelman käyttämiseksi.

## Komentorivitoiminnot

### Suoritus
Ohjelma voidaan käynnistää seuraavasti:
```
poetry run invoke start
```
### Testaus
Testit voidaan suorittaa seuraavasti:
```
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportti voidaan luoda seuraavasti:
```
poetry run invoke coverage-report
```
Luotu raportti avautuu automaattisesti selaimeen. 

> [!TIP]
> Jos komennon suoritus virtuaalityöasemalla tyssää virheeseen `database is locked`, siirrä tai lataa projektin sisältö hakemistoon `/tmp`. [Ohje](https://ohjelmistotekniikka-hy.github.io/python/toteutus#sqlite-tietokanta-lukkiutuminen-virtuaality%C3%B6asemalla)

### Pylint
Pylint-tarkistus voidaan suorittaa komennolla:
```
poetry run invoke lint
```
Tarkistus on määritelty tiedostossa [.pylintrc](budjetointisovellus/.pylintrc).
