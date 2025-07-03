import unittest
from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_retorna_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_retorna_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_general(self):
        x_y_saidas = (
            (10, 20, 30),
            (-10, 20, 10),
            (0, 0, 0),
            (1.5, 2.5, 4.0),
            (-1.5, -2.5, -4.0),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_str_int_retorna_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma('10', 10)

    def test_soma_int_str_retorna_assertion_error(self):
        with self.assertRaises(AssertionError):
            soma(10, '10')


if __name__ == "__main__":
    unittest.main(verbosity=2)
