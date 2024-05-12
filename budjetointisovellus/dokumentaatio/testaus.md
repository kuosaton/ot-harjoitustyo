# Testausdokumentti

Ohjelman toimintaa on testattu automatisoidusti unittest-yksikkötesteillä sekä manuaalisesti järjestelmätason testeillä.

## Yksikkötestaus

Budjetointisovelluksen sovelluslogiikasta vastaa luokka Budget, jota testataan luokalla TestBudget. Tällöin alustetaan Budget-olio ja tarkistetaan sen alustuvan odotetusti. Tämän jälkeen testataan Budget-luokan toiminnallisuuksien toimivan ja palauttavan odotetun kaltaisia syötteitä.

## Testikattavuus

![coverage_report](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/7b929ebd-8295-4a6c-bd04-86b436c651c5)

Sovelluksen testikattavuus on 100%. Käyttöliittymän luokkia ei testata eikä täten huomioida.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus tehtiin manuaalisesti.

### Asennus

Sovellus on ladattu ja asennettu [käyttöohjetta](kayttoohje.md) seuraamalla sekä Linux-ympäristössä (Cubbli-käyttöjärjestelmän fuksiläppäri ja virtuaalityöasema) että Windows-ympäristössä (Windows 11 -käyttöjärjestelmän tietokone). 

Sovelluksen on myös tarkistettu toimivan odotetusti näissä ympäristöissä, lisää toiminnallisuuksien testaamisesta alla.

### Toiminnallisuudet

Kaikkien [vaatimusmäärittelyssä](vaatimusmaarittely.md) ja käyttöohjeessa esitettyjen toiminnallisuuksien on testattu toimivan odotetusti monenlaisilla syötteillä, niin kelvollisilla kuin kelvottomillakin (esim. tyhjä syöte, ei-numeerinen rahasyöte). 

Odotetusti toimiminen tarkoittaa tässä tapauksessa sitä, että ohjelma ei käsittele virheellisiä syötteitä, ja kelvollisen syötteen käsitellessä päivittää budjetin odotetusti ja palauttaa oikein lasketut meno/tulo/total -rahasummat. 

Ohjelman on testattu toimivan oikein budjetin kirjauksia poistettaessa, eikä mene sekaisin, vaikka käyttäjä kuinka rämpyttäisi menemään budjettikirjausten luontien ja poistojen kanssa. Budjetin sisältö ja ohjelman esittämät rahasummat pysyvät oikeellisina.

Testatessa on kokeiltu sekä olemassaolevan budjettitiedoston lataamista että uuden budjetin luomista ja muokkaamista.

## Sovellukseen jääneet laatuongelmat

1. Sovellus ei tämänhetkisessä toiminnallisuustilassaan ilmoita käyttäjälle annetun syötteen olevan virheellinen, vaan on tekemättä mitään.
- Tätä voisi vielä parantaa hiukan. Käyttäjäkokemuksen kannalta olisi selkeämpää, jos sovellus ilmoittaisi käyttäjälle tämän antaman syötteen olevan ei-kelvollinen.

3. Koska ohjelman tämänhetkisessä versiossa budjetin tallentamisen tiedostoon hoitaa käyttöliittymän luokka BudgetView eikä käyttöliittymää huomioida testaamisessa, asettaa tämä pienen kuolleen kulman
   automatisoidun testikattavuuden kokonaisvaltaiseen arviointiin.
- Tämä seikka on pyritty huomioimaan kokonaisvaltaisilla manuaalisilla järjestelmätestauksilla, jossa on kokeiltu monipuolisesti erilaisia testitilanteita budjettien tallentamisen ja lataamisen
   suhteen.
