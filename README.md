# Budjetointisovellus
Sovelluksen avulla käyttäjän on mahdollista kirjata tuloja ja menoja seuratakseen rahatilannettaan.

## Dokumentaatio
- [Vaatimusmäärittely](budjetointisovellus/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](budjetointisovellus/dokumentaatio/tuntikirjanpito.md)
- [Changelog](budjetointisovellus/dokumentaatio/changelog.md)

## Komentorivitoiminnot
### Suoritus
Ohjelma voidaan suorittaa seuraavasti:
```
poetry run invoke start
```
### Testaus
Ohjelmaa voidaan testata seuraavasti:
```
poetry run invoke test
```
### Testikattavuusraportti
Kattavuusraportti luodaan ja avataan automaattisesti selaimeen seuraavalla komennolla:
```
poetry run invoke coverage-report
```
