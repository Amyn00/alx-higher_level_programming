#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): The divisor
    Return:
        New matrix
    """

    # matrix must be a list of lists of integers or floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Each row of the matrix must be of the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # div must be a number (integer or float)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    # div can’t be equal to 0, otherwise raise a ZeroDivisionError
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # All elements of the matrix should be divided by div, rounded to 2 decimal
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # Retruns new matrix
    return new_matrix
