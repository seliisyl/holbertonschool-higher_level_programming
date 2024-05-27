#!/usr/bin/python3
"""
   function file for pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
    n (int): The number of rows in Pascal's triangle.

    Returns:
    List[List[int]]:list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Start the new row with a 1
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # End the new row with a 1
        triangle.append(new_row)

    return triangle
