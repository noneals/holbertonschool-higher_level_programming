#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with all values divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If rows are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """

    # Validate matrix type
    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Validate each element is a number
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    # Validate same row size
    row_len = len(ma_
