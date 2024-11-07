#!/usr/bin/python3
"""
The N queens problem solutions
"""

import sys


def solve_nqueens(N):
    """
    Solves the N queens problem.
    """
    solutions = []
    state = []

    def is_safe(row, col):
        for r, c in enumerate(state):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def dfs(row):
        """
        Depth first search algorithim
        """
        if row == N:
            solution = [[i, c] for i, c in enumerate(state)]
            solutions.append(solution)
            return
        for col in range(N):
            if is_safe(row, col):
                state.append(col)
                dfs(row + 1)
                state.pop()

    dfs(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
