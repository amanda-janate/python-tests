# Primitivo
from typing import Any, NewType, Callable, Sequence, Iterable
numero: int = 10

# Sequencias
lista: list[int] = [1, 2, 3]
lista2: list[int | str] = [1, 2, 3, "cuatro"]
tupla: tuple[int, int, int] = (1, 2, 3)

# Dict e sets
my_dict = dict[str, str | int]
# pessoa: dict[str, str | int] = {"name": "Amanda", "idade": 30}
pessoa: my_dict = {"name": "Amanda", "idade": 30}
pessoa2: dict[str, Any] = {"name": "Amanda", "idade": 30}

# Criando tipagem
UserId = NewType("UserId", int)
user = UserId(10)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(a: int, b: int) -> int:
    return a + b


print(retorna_funcao(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade


def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]
