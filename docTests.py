def fak(n):
    """
    >>> fak(1)
    1
    >>> fak(4)
    24
    >>> fak(0)
    111

    :param n:
    :return:
    """
    num = 1
    while n > 1:
        num *= n
        n -= 1
    return num


if __name__ == '__main__':
    import doctest
    doctest.testmod()
