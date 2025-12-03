#!/usr/bin/python3
"""
Module that defines a function add_integer which adds two integers.

Example:
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
    ...
TypeError: b must be an integer
>>> add_integer(None)
Traceback (most recent call last):
    ...
TypeError: a must be an integer
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First number to add.
        b (int or float, optional): Second number to add. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        int: Sum of a and b as integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if a != a:  # NaN check
            raise ValueError("a cannot be NaN")
        if a > 1e308 or a < -1e308:  # Infinity approx check
            raise OverflowError("cannot convert float infinity to integer")
        a = int(a)
    if isinstance(b, float):
        if b != b:  # NaN check
            raise ValueError("b cannot be NaN")
        if b > 1e308 or b < -1e308:  # Infinity approx check
            raise OverflowError("cannot convert float infinity to integer")
        b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
