import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_levanta_assertionerror_se_nao_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('string')

    def test_bacon_com_ovos_retorna_bacon_com_ovos_se_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = "Bacon com Ovos"
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_retorna_passar_fome_se_nao_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8, 11, 13, 14, 16)
        saida = "Passar Fome"
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_retorna_bacon_se_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18)
        saida = "Bacon"
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_retorna_ovos_se_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = "Ovos"
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)


if __name__ == "__main__":
    unittest.main(verbosity=2)
