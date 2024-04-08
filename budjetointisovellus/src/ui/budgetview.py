import main

class UI:
    def __init__(self):
        main.init()
        
    def luo_budjetti(self, nimi):
        budjetti_id = main.createBudget(nimi)
        return budjetti_id

    def luo_kirjaus(self, name: str, summa, budget_id: int, valinta: str):
        return main.createEntry(name, summa, budget_id, valinta)

    def hae_budjetin_sisalto(self, budget_id: int):
        return main.getEntries(budget_id)

    def hae_kaikki_budjetit(self):
        return main.getBudgets()

    def kayttoliittyma(self):
        print(f"Komennot:")
        print(f"Luo budjetti: 1")
        print(f"Lisää budjettiin tulo tai meno: 2")
        print(f"Hae budjetit:: 3")
        print(f"Hae budjetin sisältö: 4")
        print(f"Sulje ohjelma: 0")
        print("")
        while True:
            komento = input("Valitse komento 1, 2, 3, 4 tai 0: ")

            if komento == "1":
                    nimi = str(input("Anna budjetille nimi: "))
                    id = self.luo_budjetti(nimi)
                    print(f"Budjetti {nimi}, tunnus {id} luotu!")

            elif komento == "2":
                while True:
                    id = input("Anna budjetin tunnus: ")
                    nimi = input("Anna kirjaukselle nimi: ")
                    valinta = input("Onko kyseessä tulo (t) vai meno (m)? t/m: ")
                    summa = input("Anna rahasumma: ")

                    if self.luo_kirjaus(nimi, summa, id, valinta):
                        break
                    else:
                        print("Virheellinen syöte!")
                    
            elif komento == "3":
                print(self.hae_kaikki_budjetit())

            elif komento == "4":
                while True:
                    try:
                        id = int(input("Anna budjetin tunnus: "))
                        print(self.hae_budjetin_sisalto(id))
                        break
                    except ValueError:
                        print("Virheellinen syöte!")

            elif komento == "0":
                break

            else:
                print("Anna kelvollinen komento!")

if __name__ == "__main__":
    sovellus = UI()
    sovellus.kayttoliittyma()
