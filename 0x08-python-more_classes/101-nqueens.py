#!/usr/bin/python3
"""
This module solves the N-Queens problem using backtracking.

"""
import sys


def is_safe(board, row, col, N):
    """
    Check for queen in same column or diagonals.

    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    def solve(board, row):
        if row == N:
            solution = [(i, board[i].index(1)) for i in range(N)]
            solutions.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
