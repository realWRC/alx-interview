#!/usr/bin/python3
""""A module to answer alx-interview questions"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid.
    """
    perimeter = 0
    rows = len(grid)
    colms = len(grid[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(colms):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
