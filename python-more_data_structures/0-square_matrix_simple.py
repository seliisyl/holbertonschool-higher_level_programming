#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # check matrice is empty
    if not matrix:
        return []

    # Créenvelle matrice pour stocker les valeurs carr�
    result = []

    # Parcourir chaque ligne de la matrice
    for row in matrix:
        new_row = []
        # Parcourir chaque é�t de la ligne et calculer son carr�
        for num in row:
            new_row.append(num ** 2)
        # Ajt la ligne avec les valeurs carrée la nvelle matrice
        result.append(new_row)

    return result
