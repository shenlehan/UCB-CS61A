def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        if n % 2 == 0:
            print(n)
            n /= 2
        else:
            print(n)
            n = n * 3 + 1
    print(n)