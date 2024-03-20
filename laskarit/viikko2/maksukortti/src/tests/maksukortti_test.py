import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")


    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(self.kortti.saldo_euroina(), 7.5)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(self.kortti.saldo_euroina(), 35.0)

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(self.kortti.saldo_euroina(), 150.0)

    # Tehtava 3: lisaa testeja

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_negatiivinen_lataus_ei_muuta_saldoa(self):
        kortti = Maksukortti(100)
        kortti.lataa_rahaa(-2000)

        self.assertEqual(kortti.saldo_euroina(), 1.0)

    def test_maukkaan_osto_tasarahalla(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 0.0)

    def test_edullisen_osto_tasarahalla(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 0.0)
        
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
        kortti.syo_maukkaasti()

        if kortti.saldo_euroina == 1.0:
            return True
        return False

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        if kortti.saldo_euroina == 2.0:
            return True
        return False

    