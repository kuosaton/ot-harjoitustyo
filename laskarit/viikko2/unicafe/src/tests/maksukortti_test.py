import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

# Tehtava 6: takaisin testeihin
        
    def test_kortin_saldo_alussa_oikein(self):
        kortti = Maksukortti(400)
        self.assertEqual(kortti.saldo_euroina(), 4.0)


    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        kortti = Maksukortti(0)
        kortti.lataa_rahaa(200)

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        kortti = Maksukortti(500)
        kortti.ota_rahaa(400)

        if kortti.saldo_euroina == 1.0:
            return True
        return False

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        kortti.ota_rahaa(300)

        if kortti.saldo_euroina == 2.0:
            return True
        return False

    

    def test_tulostus_oikein(self):
        kortti = Maksukortti(1000)
        vastaus = str(kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")