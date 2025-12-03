#!/usr/bin/python3
"""
Module that defines a function add_integer which adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First number to add.
        b (int or float, optional): Second number to add. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.
        ValueError: If a or b is NaN.
        OverflowError: If a or b is infinity.

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
        b=int(b)
    return a + b
