# Arkkitehtuuri 

Sovelluksen tämänhetkisen toiminnallisuuden arkkitehtuurikuvaus.


## Budjetin luominen

1. Sovellus käynnistyy suorittamalla tiedosto `main.py`, jonka luokka `main` käynnistää Tkinter-ikkunan ja alustaa graafisen käyttöliittymän `GUI`-emoluokan.
2. `GUI` alustaa alaluokan `StartView`. Sovellus avautuu aloitusnäkymään, jossa käyttäjä voi luoda budjetin. Esimerkkinä, käyttäjä luo budjetin nimisyötteellä "Oktoberfest".
3. `StartView` käsittelee syötteen ja palauttaa sen `GUI`:lle.
4. `GUI` alustaa alaluokan `BudgetView` nimisyötteen kera. `BudgetView` alustaa `Budget`-luokan olion `Oktoberfest`. 
5. Sovellus siirtyy budjetin `Oktoberfest` sisäiseen näkymään.


> [!NOTE]
> Esitetyissä sekvenssikaavioissa luokkiin `GUI`, `StartView`, `BudgetView` viitataan yhteisesti termillä `UI`, joka esittää käyttöliittymää kokonaisuudessaan.
> Alla esitetty pakkauskaavio havainnollistaa tätä rakennetta.

Pakkauskaavio:

![Screenshot from 2024-04-16 13-35-55](https://github.com/kuosaton/ot-harjoitustyo/assets/120479105/d8d7d427-4781-40f4-a2bf-cef202e5ffe5)


Sekvenssikaavio:

```mermaid
sequenceDiagram
  actor User
  create participant UI
  User->>UI: start program
  UI->>UI: show_start_view()
  User->>UI: click "Create budget" button
  UI->>UI: handle_budget_creation("Oktoberfest")
  UI->>UI: show_budget_view("Oktoberfest")
  UI->>UI: initialize_budget("Oktoberfest")
  create participant Oktoberfest
  UI->>Oktoberfest: Budget("Oktoberfest")
```

## Kirjausten lisääminen budjettiin
Kun budjetti on luotu, käyttäjä voi lisätä siihen kirjauksia. Esimerkissä käyttäjä syöttää Tammikuun budjetin tulokirjauksen `matkakassa, 800`, ja tämän jälkeen menokirjauksen `nakit ja muusi, 4.80`. 
Budjetin sisältö tulee näkyviin omassa kehyksessään `entries_frame`, kun budjettiin luodaan ensimmäinen kirjaus. Sovellus luo/päivittää budjetin sisällön kehyksen, kun uusi kirjaus luodaan.

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
