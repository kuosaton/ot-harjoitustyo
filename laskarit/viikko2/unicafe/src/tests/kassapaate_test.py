import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaate_luotu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_oikein_edulliset(self):
        # Maksu ei riittävä
        maksu_riittamaton = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(maksu_riittamaton, 100) # Kaikki rahat palautetaan
        self.assertEqual(self.kassapaate.edulliset, 0) # Lounaiden määrä ei kasva
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0) # Kassan raha ei muutu

        # Maksu riittävä, tasaraha
        maksu_tasaraha = self.kassapaate.syo_edullisesti_kateisella(240) 
        self.assertEqual(maksu_tasaraha, 0) # Ei vaihtorahaa
        self.assertEqual(self.kassapaate.edulliset, 1) # Lounaiden määrä kasvanut
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

        # Maksu riittävä, hinnan ylittävää vaihtorahaa
        maksu_ylimaaraista = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(maksu_ylimaaraista, 60) # Vaihtoraha oikein
        self.assertEqual(self.kassapaate.edulliset, 2) # Lounaiden määrä kasvanut
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.8)

    
    def test_kateisosto_toimii_oikein_maukkaat(self):
        # Maksu ei riittävä
        maksu_riittamaton = self.kassapaate.syo_maukkaasti_kateisella(123)
        self.assertEqual(maksu_riittamaton, 123) # Kaikki rahat palautetaan
        self.assertEqual(self.kassapaate.maukkaat, 0) # Lounaiden määrä ei kasva
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0) # Kassan raha ei muutu

        # Maksu riittävä, tasaraha
        maksu_tasaraha = self.kassapaate.syo_maukkaasti_kateisella(400) 
        self.assertEqual(maksu_tasaraha, 0) # Ei vaihtorahaa
        self.assertEqual(self.kassapaate.maukkaat, 1) # Lounaiden määrä kasvanut
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)


        # Maksu riittävä, hinnan ylittävää vaihtorahaa
        maksu_ylimaaraista = self.kassapaate.syo_maukkaasti_kateisella(480)
        self.assertEqual(maksu_ylimaaraista, 80) # Vaihtoraha oikein
        self.assertEqual(self.kassapaate.maukkaat, 2) # Lounaiden määrä kasvanut
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1008)


                
    def test_korttiosto_toimii_oikein_edulliset(self):
        kortti = Maksukortti(100)
        kassa = Kassapaate()

        kassa.syo_edullisesti_kortilla(kortti) # Kortilla liian vähän rahaa

        self.assertEqual(kortti.saldo_euroina(), 1.0) # Kortin saldo ennallaan
        self.assertEqual(kassa.kassassa_rahaa_euroina(), 1000.0) # Kassan saldo ennallaan
        self.assertEqual(kassa.edulliset, 0) # Myytyjä 0


        kassa.lataa_rahaa_kortille(kortti, 140) # Ladataan kortille lisää
        kassa.syo_edullisesti_kortilla(kortti) # Kortilla tasaraha
        self.assertEqual(kortti.saldo_euroina(), 0) # Kortin saldo muutettu oikein
        self.assertEqual(kassa.kassassa_rahaa_euroina(), 1001.4) # Kassan saldo muutettu oikein
        self.assertEqual(kassa.edulliset, 1) # Myytyjä 1

        kassa.lataa_rahaa_kortille(kortti, 300) # Ladataan kortille ylimääräistä
        kassa.syo_edullisesti_kortilla(kortti) 
        self.assertEqual(kortti.saldo_euroina(), 0.6) # Kortin saldo muutettu oikein
        self.assertEqual(kassa.kassassa_rahaa_euroina(), 1004.4) # Kassan saldo ennallaan
        self.assertEqual(kassa.edulliset, 2) # Myytyjä 2

    def test_korttiosto_toimii_oikein_maukkaat(self):
        kortti = Maksukortti(100)
        kassa = Kassapaate()

        kassa.syo_maukkaasti_kortilla(kortti) # Kortilla liian vähän rahaa

        self.assertEqual(kortti.saldo_euroina(), 1.0) # Kortin saldo ennallaan
        self.assertEqual(kassa.kassassa_rahaa_euroina(), 1000.0) # Kassan saldo ennallaan
        self.assertEqual(kassa.maukkaat, 0) # Myytyjä 0


        kassa.lataa_rahaa_kortille(kortti, 300) # Ladataan kortille lisää
        kassa.syo_maukkaasti_kortilla(kortti) # Kortilla tasaraha
        self.assertEqual(kortti.saldo_euroina(), 0) # Kortin saldo muutettu oikein
        self.assertEqual(kassa.kassassa_rahaa_euroina(), 1003.0) # Kassan saldo muutettu oikein
        self.assertEqual(kassa.maukkaat, 1) # Myytyjä 1

        kassa.lataa_rahaa_kortille(kortti, 500) # Ladataan kortille ylimääräistä
        kassa.syo_maukkaasti_kortilla(kortti) 
        self.assertEqual(kortti.saldo_euroina(), 1.0) # Kortin saldo muutettu oikein
        self.assertEqual(kassa.kassassa_rahaa_euroina(), 1008.0) # Kassan saldo ennallaan
        self.assertEqual(kassa.maukkaat, 2) # Myytyjä 2

    def test_kortille_lataus(self):
        kortti = Maksukortti(100)
        kassa = Kassapaate()
        kassa.lataa_rahaa_kortille(kortti, -100)
        kassa.lataa_rahaa_kortille(kortti, 250)
        self.assertEqual(kortti.saldo_euroina(), 3.5)
        self.assertEqual(kassa.kassassa_rahaa_euroina(), 1002.5)