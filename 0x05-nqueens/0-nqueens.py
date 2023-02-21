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

    # Initialize the board
    board = [-1] * n

    # Define the helper function to check if a queen can be placed
    # at a given row and column
    def can_place_queen(row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    # Define the recursive function to solve the N queens problem
    def nqueens_helper(row):
        if row == n:
            print(" ".join(str(i) for i in board))
            return
        for col in range(n):
            if can_place_queen(row, col):
                board[row] = col
                nqueens_helper(row + 1)
                board[row] = -1

    # Solve the problem
    nqueens_helper(0)


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
