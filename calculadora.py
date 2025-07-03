def soma(x, y):
    # doctests
    """
    Soma dois números.
    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 10)
    Traceback (most recent call last):
    ...
    AssertionError: x must be a number
    """
    assert isinstance(x, (int, float)), "x must be a number"
    assert isinstance(y, (int, float)), "y must be a number"
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
