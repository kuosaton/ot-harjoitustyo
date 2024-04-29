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

Sovellus aukeaa aloitusnäkymään, jossa käyttäjä syöttää budjetille haluamansa nimen ja luo budjetin. Mikäli budjetille on jo olemassa tallennustiedosto, kyseinen tiedosto ja sen sisältö ladataan. Muussa tapauksessa nimellä luodaan uusi tiedosto.

Annettu syöte tarkistetaan, eli jos syöte on tyhjä, sovellus ei tee mitään.

![Screenshot from 2024-04-29 19-06-50](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/dcac5fc6-719b-484b-8ba5-15d25cf10a27)


## Budjetti

Budjetin luotuaan käyttäjä viedään budjettinäkymään, jossa käyttäjä voi luoda budjettiin kirjauksia haluamillaan syötteillä. Syötettä varten pyydetään nimi, rahamäärä sekä kirjauksen tyyppi (meno/tulo), joka valitaan toggle-napilla.

Annettu syöte jälleen tarkistetaan. Jos jokin syötteistä on tyhjä tai annettu rahasyöte ei ole kelvollinen luku, sovellus ei tee mitään.

Jos annetaan kokonaan uusi nimi tai yhtään budjettia ei ole vielä löyty, budjetin näkymä avautuu seuraavanlaisena ilman sisältönäkymää.

Esimerkkikuvassa annetulla nimisyötteellä "testi2" ei löytynyt olemassa olevaa tiedostoa.

![Screenshot from 2024-04-29 19-10-39](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/2179ec91-2f3a-4eab-abb3-7ddf6e7446d5)


Kun ensimmäinen kirjaus on luotu budjettiin "testi2", näkymä avaa budjetin sisällön näkymän. Tämä alinäkymä näyttää budjetin sisällön sekä rahamäärien summat.

![Screenshot from 2024-04-29 19-12-35](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/74e1f72b-c58a-4436-ae4f-e8263183ed26)


Esimerkkikuvassa annetulla nimisyötteellä "testi" vuorostaan löytyi käyttäjän hakemistosta olemassa oleva tiedosto kuvakaappauksessa näkyvine merkintöineen, joten ne ladattiin suoraan budjetin sisältönäkymään.

![Screenshot from 2024-04-29 19-09-14](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/f2506928-a851-4d0d-b9f3-895ece0e36ce)


Jos luo menoksi tarkoitetun kirjauksen vahingossa tulona, ei hätää – luodun kirjauksen voi poistaa klikkaamalla sitä.

![sovellus_poisto_1_1](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/9d705833-9392-48d0-bd5c-e0541d6ba55e)
![sovellus_poisto_1_2](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/8b208328-a5ce-44b0-98d3-a415a2177327)

Aina, kun budjetin sisältöön tehdään muutoksia, sovellus päivittää näkymän. Näytetty sisältö ja rahamäärien lasketut summat pysyvät ajan tasalla.

Kirjauksen poisto on hyödyllinen ominaisuus myös luotaessa vahingossa ylimääräisiä kirjauksia.

![sovellus_poisto_1](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/16deb139-979a-4f90-a503-ffa9cffa2083)
![sovellus_poisto_2](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/8e962067-e16c-48c6-a941-43ce7760d48a)

## Paluu aloitusnäkymään

Klikkaamalla "Return to overview"-nappia käyttäjä palaa aloitusnäkymään, ja luotu budjetti sulkeutuu. Budjetin viimeisin muokkaus on tallennettu, ja voidaan avata uudelleen syöttämällä kyseisen budjetin nimi. 
