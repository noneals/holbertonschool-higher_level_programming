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

    # تحقق من نوع a
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    # تحقق من نوع b
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # تحقق من NaN و Infinity لـ a
    if isinstance(a, float):
        if a != a:  # NaN
            raise ValueError("a cannot be NaN")
        if a > 1e308 or a < -1e308:  # Infinity تقريبية
            raise OverflowError("cannot convert float infinity to integer")

    # تحقق من NaN و Infinity لـ b
    if isinstance(b, float):
        if b != b:
            raise ValueError("b cannot be NaN")
        if b > 1e308 or b < -1e308:
            raise OverflowError("cannot convert float infinity to integer")

    # تحويل إلى int وجمع
    return int(a) + int(b)
