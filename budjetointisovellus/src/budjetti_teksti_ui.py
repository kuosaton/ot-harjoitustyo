from budjetti import Budjetti

class Kayttoliittyma:
    def __init__(self):
        self.budjetti = Budjetti()

    def ohje(self):
        print(f"Komennot:")
        print(f"1: Nimeä budjetti")
        print(f"2: Lisää budjettiin tulo")
        print(f"3: Lisää budjettiin meno")
        print(f"4: Hae budjetin tulot")
        print(f"5: Hae budjetin menot")
        print(f"6: Laske budjetin tulot ja menot yhteen")
        print(f"7: Hae budjetin sisältö")
        print(f"0: Sulje sovellus")
        print("")

    def start(self):
        print(f"Tervetuloa budjettisovellukseen!")
        print("")
        self.ohje()

        while True:
            komento = input("Anna komento syöttämällä luku 0-7: ")

            if komento == "1":
                nimi = str(input("Anna budjetille nimi: "))
                self.budjetti.nimea_budjetti(nimi)
                print("Budjetin nimi on nyt", self.budjetti.nimi)

            elif komento == "2":
                nimi = str(input("Anna tuloerälle nimi/kuvaus: "))
                summa = float(input("Anna tuloerälle rahasumma: "))
                self.budjetti.lisaa_tulo(nimi, summa)
                print("Tuloerä lisätty!")

            elif komento == "3":
                nimi = str(input("Anna menoerälle nimi/kuvaus: "))
                summa = float(input("Anna menoerälle rahasumma: "))
                self.budjetti.lisaa_meno(nimi, summa)
                print("Menoerä lisätty!")

            elif komento == "4":
                print(self.budjetti.laske_tulot())

            elif komento == "5":
                print(self.budjetti.laske_menot())

            elif komento == "6":
                print(self.budjetti.laske_summa())

            elif komento == "7":
                print(self.budjetti.hae_sisalto())

            elif komento == "0":
                break

            else:
                print("Syötettä ei tunnistettu :(")
                self.ohje()

if __name__ == "__main__":
    sovellus = Kayttoliittyma()
    sovellus.start()