#!/usr/bin/python3

def matrix_divided(matrix, div):
    '''
    "Divide all elements of a matrix by a divisor and return a new matrix."
    Paramètres:
    matrice (list of list of int/float): La matrice à diviser.
    div (int/float): Le diviseur.

    Retours:
    "New matrix with elements divided and rounded to 2 decimals."

    Exceptions:
    TypeError: Si matrix pas une liste de listes d'entiers ou de flottants.
    TypeError: Si chaque ligne de la matrice n'a pas la même taille.
    TypeError: Si div n'est pas un nombre (entier ou flottant).
    ZeroDivisionError: Si div est égal à 0.
    '''
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
