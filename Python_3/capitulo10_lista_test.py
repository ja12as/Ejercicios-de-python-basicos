def suma(li):
    """Devuelve la suma de todos los elementos de la lista
    >>> suma([1, 2, 3])
    6
    """
    total = 0
    for ele in li:
        total += ele
    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
