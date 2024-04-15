## Viikko 3

- Aloitettu projektin toteutus
- Luotu luokat Budget ja Interface
  - Budget sisältää toiminnallisuudet, Interface kutsuu Budgetia
- Tekstikäyttöliittymä, ei pysyvää tallennusta
- Testattu, että Budget alustaa sanakirjan odotetusti

## Viikko 4
- Toteutettu graafinen käyttöliittymä, luotu luokat GUI, StartView, BudgetView
- Sovelluksen toiminnallisuus rajoittuu tällä hetkellä budjetin luomiseen ja tulojen/menojen lisäämiseen
  - Tieto säilyy vain istunnon suorituksen ajan, tavoitteena tulevaisuudessa toteuttaa pysyvä tallennus
- Muokattu invoke-komennot toimimaan uusilla muutoksilla, `poetry run invoke start` ajaa nyt tiedoston main.py, joka käynnistää graafisen käyttöliittymän
- Korjattu testikattavuusraportin luonnin estänyt ongelma
