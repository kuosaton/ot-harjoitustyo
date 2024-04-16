# Arkkitehtuuri 

Sovelluksen tämänhetkinen arkkitehtuuri.

## Budjetin luominen

1. Sovellus käynnistyy suorittamalla tiedosto main.py. Tämä alustaa graafisen käyttöliittymän emoluokan GUI, joka vuorostaan alustaa luokan StartView.
2. Sovellus aukeaa aloitusnäkymään, jossa käyttäjä voi luoda budjetin. Tässä esimerkissä käyttäjä luo budjetin "Tammikuun budjetti". Tällöin alustetaan luokka BudgetView, jonka yhteydessä alustetaan luokka Budget. 
3. Sovellus siirtyy budjetin sisäiseen näkymään. Budget-luokka alustaa sanakirjan, joka sisältää tyhjät listat "Income" ja "Expense". 

```mermaid
sequenceDiagram
  actor User
  participant UI
  User->>UI: start program
  UI->>UI: show_start_view()
  User->>UI: click "Create budget" button
  UI->>UI: handle_budget_creation("Tammikuun budjetti")
  UI->>UI: show_budget_view("Tammikuun budjetti")
  participant Tammikuun budjetti
  UI->>Tammikuun budjetti: initialize_budget("Tammikuun budjetti")
```

## Kirjausten lisääminen budjettiin
Kun budjetti on luotu, käyttäjä voi lisätä siihen kirjauksia. Esimerkissä käyttäjä syöttää Tammikuun budjetin tulokirjauksen `palkka, 2000`, ja tämän jälkeen menokirjauksen `nakit ja muusi, 4.80`. 
Budjetin sisältö tulee näkyviin omassa kehyksessään `entries_frame`, kun budjettiin luodaan ensimmäinen kirjaus. Sovellus luo/päivittää budjetin sisällön kehyksen, kun uusi kirjaus luodaan.

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant Tammikuun budjetti
  User->>UI: click "Create entry" button
  UI->>UI: handle_entry_creation()
  UI->>Tammikuun budjetti: add_income(palkka, 2000)
  UI->>UI: create_entries_list()
  UI->>Tammikuun budjetti: entries["Income"]
  Tammikuun budjetti->>UI: palkka, 2000
  UI->>Tammikuun budjetti: entries["Expense"]
  Tammikuun budjetti->UI: None
  User->>UI: click "Create entry" button
  UI->>UI: handle_entry_creation()
  UI->>Tammikuun budjetti: add_income(nakit ja muusi, 4.80)
  UI->>UI: create_entries_list()
  UI->>Tammikuun budjetti: entries["Income"]
  Tammikuun budjetti->>UI: palkka, 2000
  UI->>Tammikuun budjetti: entries["Expense"]
  Tammikuun budjetti->>UI: nakit ja muusi, 4.80
```
