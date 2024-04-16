# Arkkitehtuurikuvaus

Sovelluksen tähänastisen toteutuksen arkkitehtuurikuvaus.

## Rakenne

Ohjelman rakenne on seuraavanlainen. Pakkaus *src* sisältää ohjelman käynnistyksestä vastaavan luokan *main*, sekä sovelluksen käyttämän budjetti-tietokohteen luokan *Budget*. Pakkaus *ui* sisältää ohjelman käyttöliittymästä vastaavat luokat *GUI*, *StartView* ja *BudgetView*.

Pakkauskaavio:

![Pakkauskaavio](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/f9283cae-ff1d-4f20-94cf-04d6c7e650b3)

Luokkakaavio:

![Luokkakaavio](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/f40f41e8-92c5-43dc-9d8b-15793d4f5a50)

Kiinteät viivat kuvaavat luokkien välisiä pysyviä yhteyksiä, ja katkoviivat ei-pysyviä riippuvuuksia luokkien välillä. Luokkien *main* ja *GUI* välillä on pysyvä yhteys. *GUI*:n ja sen alaluokkien *StartView*, *BudgetView* välillä on ei-pysyvä riippuvuus. *BudgetView*:n ja *Budget*:n välillä on pysyvä yhteys, sillä *BudgetView* on tarkasteltavan budjetin graafinen näkymä.

## Käyttöliittymä

Ohjelman käyttöliittymä sisältää kaksi näkymää:
1. Aloitusnäkymä
2. Budjettinäkymä

Nämä ovat eriytetty omiin luokkiinsa, ja niiden näyttämisestä vastaa luokka *GUI*. Käyttäjä voi luoda aloitusnäkymässä budjetin. Tällöin siirrytään budjettinäkymään, eli budjetin sisäiseen näkymään, jossa käyttäjä voi lisätä budjettiin tuloja tai menoja.

## Toiminnallisuudet

Esitetään sovelluksen käytöstä esimerkkitilanne sekvenssiokaavioilla. 

> [!NOTE]
> Tämän dokumentin sekvenssikaavioissa sovelluksen käyttöliittymään eli luokkiin `GUI`, `StartView`, `BudgetView` viitataan yhteisesti termillä `UI` kaavion yksinkertaistamiseksi.

### Budjetin luominen

1. Sovellus käynnistyy suorittamalla tiedosto `main.py`.
2. Luokka `main` käynnistää Tkinter-ikkunan ja alustaa graafisen käyttöliittymän luokan `GUI`.
3. `GUI` alustaa luokan `StartView`.
4. Sovellus avautuu aloitusnäkymään, jossa käyttäjä voi luoda budjetin. Esimerkkinä, käyttäjä luo budjetin nimisyötteellä "Oktoberfest".
5. `StartView` käsittelee syötteen ja välittää sen `GUI`:lle.
6. `GUI` alustaa nimisyötteellä luokan `BudgetView`, joka alustaa `Budget`-luokan olion `Oktoberfest`. `BudgetView` on siis riippuvainen luokasta `Budget`
8. Sovellus siirtyy budjettinäkymään, tässä tapauksessa budjetin `Oktoberfest` sisäiseen näkymään.


Sekvenssikaavio:

```mermaid
sequenceDiagram
  actor User
  participant UI
  User->>UI: start program
  UI->>UI: show_start_view()
  User->>UI: click "Create budget" button, input "Oktoberfest"
  UI->>UI: handle_budget_creation("Oktoberfest")
  UI->>UI: show_budget_view("Oktoberfest")
  UI->>UI: initialize_budget("Oktoberfest")
  participant Oktoberfest
  UI->>Oktoberfest: Budget("Oktoberfest")
```

### Kirjausten lisääminen budjettiin
1. Kun budjetti on luotu, käyttäjä voi lisätä siihen kirjauksia. Esimerkkitapauksessa olkoon käyttäjä reissunsa alussa, ja lisää budjettiin `Oktoberfest` tulomerkinnän `matkakassa`.
2. `BudgetView` lisää tulon `Oktoberfest`:n sanakirjaan.
3. `BudgetView` hakee sanakirjan sisällön ja esittää sen käyttöliittymässä. Sisältö tulee näkyviin omassa kehyksessään `entries_frame`, kun budjettiin luodaan ensimmäinen kirjaus.
4. Käyttäjä lisää menokirjauksen `nakit ja muusi`. `BudgetView` lisää menon sanakirjaan.
5. `BudgetView` hakee sanakirjan sisällön ja päivittää sisältönäkymän poistamalla vanhan kehyksen ja luomalla uuden. Sovellus luo/päivittää budjetin sisällön kehyksen, kun uusi kirjaus luodaan.

Sekvenssikaavio:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Oktoberfest
  User->>UI: click "Create entry" button
  UI->>UI: handle_entry_creation()
  UI->>Oktoberfest: add_income(matkakassa, 400)
  UI->>UI: create_entries_list()
  UI->>Oktoberfest: entries["Income"]
  Oktoberfest-->>UI: matkakassa, 400
  UI->>Oktoberfest: entries["Expense"]
  Oktoberfest-->>UI: None
  User->>UI: click "Create entry" button
  UI->>UI: handle_entry_creation()
  UI->>Oktoberfest: add_expense(nakit ja muusi, 4.80)
  UI->>UI: create_entries_list()
  UI->>Oktoberfest: entries["Income"]
  Oktoberfest-->>UI: matkakassa, 400
  UI->>Oktoberfest: entries["Expense"]
  Oktoberfest-->>UI: nakit ja muusi, 4.80
```