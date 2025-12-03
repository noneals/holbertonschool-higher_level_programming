import math

def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if math.isnan(a):
            raise ValueError("a cannot be NaN")
        if math.isinf(a):
            raise OverflowError("cannot convert float infinity to integer")

    if isinstance(b, float):
        if math.isnan(b):
            raise ValueError("b cannot be NaN")
        if math.isinf(b):
            raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
