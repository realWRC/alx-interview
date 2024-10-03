#!/usr/bin/python3
"""Contains function that prints pascals triangle"""


def pascal_triangle(n):
    """Return Pascal's triangle of size n."""

    if n <= 0:
        return []
    triangle = []
    for rowNumb in range(n):
        row = [1]
        if triangle:
            lastRow = triangle[-1]
            for i in range(len(lastRow) - 1):
                row.append(lastRow[i] + lastRow[i + 1])
            row.append(1)
        triangle.append(row)
    return triangle
