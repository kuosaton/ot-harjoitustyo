class Budjetti:
    def __init__(self):
        self.nimi = ""
        self.budjetti = {}
        self.budjetti["Menot"] = []
        self.budjetti["Tulot"] = []

    def nimea_budjetti(self, nimi: str):
        self.nimi = nimi

    def lisaa_tulo(self, nimi: str, summa: float):
        self.budjetti["Tulot"].append((nimi, summa))
    
    def lisaa_meno(self, nimi: str, summa: float):
        self.budjetti["Menot"].append((nimi, summa))

    def laske_tulot(self):
        palautus = 0
        for tulo in self.budjetti["Tulot"]:
            palautus += tulo[1]
        return palautus

    def laske_menot(self):
        palautus = 0
        for meno in self.budjetti["Menot"]:
            palautus += meno[1]
        return palautus

    def laske_summa(self):
        tulot = self.laske_tulot()
        menot = self.laske_menot()
        summa = tulot - menot

        return f"tulot {tulot}€ - menot {menot}€ = {summa}€"

    def hae_sisalto(self):
        return self.budjetti


    def hae_tulot(self):
        palautus = []
        for tulo in self.budjetti["Tulot"]:
            palautus.append(tulo)

        return palautus

    def hae_menot(self):
        palautus = []
        for meno in self.budjetti["Menot"]:
            palautus.append(meno)

        return palautus
