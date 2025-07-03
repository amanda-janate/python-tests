import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_dados(self):
        resposta = requests.get('https://api.example.com/dados')

        if resposta.ok:
            self.dados_obtidos = True
            return "Dados obtidos com sucesso!"

        self.dados_obtidos = False
        return "ERROR 404!"
