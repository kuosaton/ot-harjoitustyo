# Budjetointisovellus
Sovelluksen avulla käyttäjän on mahdollista luoda ja nimetä budjetti, kirjata siihen tuloja ja menoja sekä seurata rahatilannettaan. 

## Python-versio
> [!NOTE]
> Sovellus on testattu versiolla `Python 3.10.12` käyttäen [Cubbli](https://helpdesk.it.helsinki.fi/ohjeet/muut-ohjeet/cubbli-helsingin-yliopistossa)-käyttöjärjestelmän fuksiläppäriä sekä [virtuaalityöasemaa](https://vdi.helsinki.fi/), eikä välttämättä toimi oikein, jos käytetty versio on vanhempi kuin `Python 3.8`. 

## Dokumentaatio
- [Vaatimusmäärittely](budjetointisovellus/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](budjetointisovellus/dokumentaatio/tuntikirjanpito.md)
- [Changelog](budjetointisovellus/dokumentaatio/changelog.md)

## Komentorivitoiminnot

### Suoritus

Ohjelman käyttöliittymä voidaan käynnistää seuraavasti:
```
poetry run invoke start
```

### Testaus
Ohjelman testit voidaan suorittaa seuraavasti:
```
poetry run invoke test
```

### Testikattavuusraportti

Ohjelman testikattavuusraportti voidaan luoda seuraavalla komennolla, jolloin se avautuu automaattisesti selaimeen:
```
poetry run invoke coverage-report
```
