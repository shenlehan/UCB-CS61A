from operator import mod, floordiv

def divide_exact(x, y):
    """
    Returns the quotient and remainder of dividing x by y.
    >>> q, r = divide_exact(123, 4)
    >>> q
    30
    >>> r
    3
    """
    return floordiv(x, y), mod(x, y)

# use python3 -m doctest -v quotient_and_remainder.py to run the doctests
# if `-v` is not used, only failed tests will be printed
print(divide_exact(123, 4))