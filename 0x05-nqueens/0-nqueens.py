#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


def solve_nqueens(n):
    # Check that n is an integer greater or equal to 4
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the arrays to keep track of occupied columns and diagonals
    cols = [False] * n
    diag1 = [False] * (2*n - 1)
    diag2 = [False] * (2*n - 1)

    # Define the recursive function to solve the N queens problem
    def nqueens_helper(row, positions):
        if row == n:
            print(" ".join(str(p[1]) for p in positions))
            return
        for col in range(n):
            if not cols[col] and not diag1[row+col] and not diag2[row-col+n-1]:
                cols[col] = diag1[row+col] = diag2[row-col+n-1] = True
                nqueens_helper(row + 1, positions + [(row, col)])
                cols[col] = diag1[row+col] = diag2[row-col+n-1] = False

    # Solve the problem
    nqueens_helper(0, [])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(n)
