def bacon_com_ovos(n):
    assert isinstance(n, int), "Input must be a positive integer"

    if n % 3 == 0 and n % 5 == 0:
        return "Bacon com Ovos"

    if n % 3 == 0:
        return "Bacon"
    if n % 5 == 0:
        return "Ovos"

    return "Passar Fome"
