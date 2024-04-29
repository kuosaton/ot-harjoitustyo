# Käyttöohje

## Asennus

1. Lataa projektin lähdekoodi:
- Navigoi osion [release](https://github.com/kuosaton/ot-harjoitustyo/releases) viimeisimpään releaseen.
- Valitse releasen Assets-osiosta *Source code*-tiedosto ladattavaksi.
- Pura pakattu projektin sisältö ja siirry projektin hakemiston kansioon /budjetointisovellus/.
      
2. Asenna riippuvuudet komennolla:

```
poetry install
```

## Käynnistäminen 

### Suoritus
Ohjelma voidaan käynnistää seuraavasti:
```
poetry run invoke start
```

## Aloitus

Sovellus aukeaa aloitusnäkymään, jossa käyttäjä syöttää budjetille haluamansa nimen ja luo budjetin.

Annettu syöte tarkistetaan, eli jos syöte on tyhjä, sovellus ei tee mitään.

![sovellus_aloitus](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/6a75fe45-4798-45dc-94b9-a61070f6c5cc)

## Budjetti

Budjetin luotuaan käyttäjä viedään budjettinäkymään, jossa käyttäjä voi luoda budjettiin kirjauksia haluamillaan syötteillä. Syötettä varten pyydetään nimi, rahamäärä sekä kirjauksen tyyppi (meno/tulo), joka valitaan toggle-napilla.

Annettu syöte jälleen tarkistetaan. Jos jokin syötteistä on tyhjä tai annettu rahasyöte ei ole kelvollinen luku, sovellus ei tee mitään.

![Screenshot from 2024-04-29 17-34-39](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/05cadf64-e6a0-4cb0-a333-10653d26f343)

Kun ensimmäinen kirjaus on luotu, näkymä avaa budjetin sisällön näkymän. Tämä alinäkymä näyttää budjetin sisällön sekä rahamäärien summat.

![Screenshot from 2024-04-29 17-35-20](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/8dc6524a-2322-43bb-93cf-9f38d4b99e3c)

Jos luo menoksi tarkoitetun kirjauksen vahingossa tulona, ei hätää – luodun kirjauksen voi poistaa klikkaamalla sitä.

![sovellus_poisto_1_1](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/9d705833-9392-48d0-bd5c-e0541d6ba55e)
![sovellus_poisto_1_2](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/8b208328-a5ce-44b0-98d3-a415a2177327)

Aina, kun budjetin sisältöön tehdään muutoksia, sovellus päivittää näkymän. Näytetty sisältö ja rahamäärien lasketut summat pysyvät ajan tasalla.

Kirjauksen poisto on hyödyllinen ominaisuus myös luotaessa vahingossa ylimääräisiä kirjauksia.

![sovellus_poisto_1](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/16deb139-979a-4f90-a503-ffa9cffa2083)
![sovellus_poisto_2](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/8e962067-e16c-48c6-a941-43ce7760d48a)

## Paluu aloitusnäkymään

Klikkaamalla "Return to overview"-nappia käyttäjä palaa aloitusnäkymään, ja luotu budjetti sulkeutuu. 
