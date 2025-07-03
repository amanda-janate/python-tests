from unittest.mock import patch
import unittest
from src.pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa("João", "Silva")

        self.p2 = Pessoa("Maria", "Oliveira")

    def test_pessoa_attr_nome_tem_valor_certo(self):
        self.assertEqual(self.p1.nome, "João")

        self.assertEqual(self.p2.nome, "Maria")

    def test_pessoa_attr_nome_str(self):
        self.assertIsInstance(self.p1.nome, str)

        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrenome_tem_valor_certo(self):
        self.assertEqual(self.p1.sobrenome, "Silva")

        self.assertEqual(self.p2.sobrenome, "Oliveira")

    def test_pessoa_attr_sobrenome_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)

        self.assertFalse(self.p2.dados_obtidos)

    def test_pessoa_obter_dados_sucesso_OK(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.ok = True
            self.assertEqual(self.p1.obter_dados(),
                             "Dados obtidos com sucesso!")
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_dados(),
                             "Dados obtidos com sucesso!")
            self.assertTrue(self.p2.dados_obtidos)

    def test_pessoa_obter_dados_falha_404(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.ok = False
            self.assertEqual(self.p1.obter_dados(),
                             "ERROR 404!")
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_dados(),
                             "ERROR 404!")
            self.assertFalse(self.p2.dados_obtidos)

    def test_pessoa_obter_dados_sucesso_falha_seq(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.ok = True
            self.assertEqual(self.p1.obter_dados(),
                             "Dados obtidos com sucesso!")
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_dados(),
                             "Dados obtidos com sucesso!")
            self.assertTrue(self.p2.dados_obtidos)

            mock_get.return_value.ok = False
            self.assertEqual(self.p1.obter_dados(),
                             "ERROR 404!")
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_dados(),
                             "ERROR 404!")
            self.assertFalse(self.p2.dados_obtidos)


if __name__ == "__main__":
    unittest.main(verbosity=2)
