# Budjetointisovellus
Sovelluksen avulla käyttäjän on mahdollista luoda ja nimetä budjetti, kirjata siihen tuloja ja menoja sekä seurata rahatilannettaan. 

## Python-versio
> [!NOTE]
> Sovellus on testattu versiolla `Python 3.10.12` käyttäen [Cubbli](https://helpdesk.it.helsinki.fi/ohjeet/muut-ohjeet/cubbli-helsingin-yliopistossa)-käyttöjärjestelmän fuksiläppäriä sekä [virtuaalityöasemaa](https://vdi.helsinki.fi/), eikä välttämättä toimi oikein, jos käytetty versio on vanhempi kuin `Python 3.8`. 

## Dokumentaatio
- [Vaatimusmäärittely](budjetointisovellus/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](budjetointisovellus/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](budjetointisovellus/dokumentaatio/tuntikirjanpito.md)
- [Changelog](budjetointisovellus/dokumentaatio/changelog.md)

## Asennus

1. Lataa projektin lähdekoodi:
    - Navigoi [release](https://github.com/kuosaton/ot-harjoitustyo/releases)-näkymän viimeisimpään releaseen ja valitse Assets-osiosta *Source code* ladattavaksi.

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
> Jos raportti ei avaudu automaattisesti tai haluat muuten vain avata sen itse, löydät raportin tarvittaessa *htmlcov*-kansiosta. Tallennuspaikka ilmoitetaan komentorivillä luomisen jälkeen tämän tapaisesti: `Wrote HTML report to htmlcov/index.html`.

### Pylint
Pylint-tarkistus voidaan suorittaa komennolla:
```
poetry run invoke lint
```
Tarkistus on määritelty tiedostossa [.pylintrc](budjetointisovellus/.pylintrc).
