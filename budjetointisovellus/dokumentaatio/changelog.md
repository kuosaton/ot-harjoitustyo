## Viikko 3

- Aloitettu projektin toteutus
- Luotu luokat Budget ja Interface
- Budget sisältää toiminnallisuudet, Interface kutsuu Budgetia
- Tekstikäyttöliittymä, ei pysyvää tallennusta
- Testattu, että Budget alustaa sanakirjan odotetusti

## Viikko 4
- Toteutettu graafinen käyttöliittymä, luotu luokat UI, StartView, BudgetView
- GUI:n toiminnallisuus rajoittuu alkuun budjetin luomiseen ja tulojen/menojen lisäämiseen
- Tieto säilyy vain istunnon suorituksen ajan, tavoitteena tulevaisuudessa toteuttaa pysyvä tallennus
- Muokattu invoke-komennot toimimaan uusilla muutoksilla, `poetry run invoke start` ajaa nyt tiedoston main.py, joka käynnistää graafisen käyttöliittymän
- Budget-luokan funktioita tiivistetty ja muokattu hieman (esim. Sanakirja alustetaan nyt suoraan Income- ja Expense-listoineen)
