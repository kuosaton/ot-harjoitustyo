## Viikko 3
- Aloitettu projektin toteutus
- Luotu luokat Budget ja Interface
  - Budget sisältää toiminnallisuudet, Interface kutsuu Budgetia
- Tekstikäyttöliittymä, ei pysyvää tallennusta
- Testattu, että Budget alustaa sanakirjan odotetusti

## Viikko 4
- Toteutettu graafinen käyttöliittymä, luotu luokat main, GUI, StartView, BudgetView
- Sovelluksen toiminnallisuus rajoittuu tällä hetkellä budjetin luomiseen ja tulojen/menojen lisäämiseen. Tieto säilyy vain istunnon suorituksen ajan
- Muokattu invoke-komennot toimimaan uusilla muutoksilla, `poetry run invoke start` ajaa nyt tiedoston main.py, joka käynnistää graafisen käyttöliittymän
- Korjattu testikattavuusraportin luonnin estänyt ongelma
- Lisätty invoke-komento `poetry run invoke lint`

## Viikko 5

- Laajennettu graafisen käyttöliittymän toiminnallisuutta, muutoksia luokkiin Budget, BudgetView, StartView
  - Budjettinäkymä näyttää nyt kirjausten rahamäärien summat (menot, tulot, total)
  - Luotuja kirjauksia voi poistaa klikkaamalla
  - Budjettiin lisättävät kirjaukset alustetaan nyt merkkijonon sijasta sisäkkäisenä sanakirjana ja niille annetaan id-luku poistamista varten
  - Käyttäjäsyötteitä käsittelevät funktiot tarkistavat syötteen oikeellisuuden ennen suoritusta
- Laajennettu testejä kattamaan koko Budget-luokka
