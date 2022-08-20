def prime_factors(n):
    """
    Print the prime factors of n in non-decreasing order.
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    i = 2
    while n != 1:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i += 1

