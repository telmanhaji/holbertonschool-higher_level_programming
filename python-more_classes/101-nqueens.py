#!/usr/bin/python3
"""
this module solves the N-Queens problem using backtracking.
it demonstrates constraint solving logic used in symbolic execution.
"""
import sys


def is_safe(board, row, col):
    """
    checks if a queen can be placed at board[row][col].

    args:
        board (list): the current state of the board (list of [row, col]).
        row (int): the current row we are trying to place a queen in.
        col (int): the current column we are trying to place a queen in.

    returns:
        bool: true if safe, false if attacked.
    """
    # it iterates through all previously placed queens
    for queen in board:
        q_row = queen[0]
        q_col = queen[1]

        # column checking: are they in the same column?
        if q_col == col:
            return False

        # diagonal check:
        # absolute difference in rows == absolute difference in columns
        # means they are on the same diagonal.
        if abs(q_row - row) == abs(q_col - col):
            return False

    return True


def solve_nqueens(n, row, board):
    """
    recursively solves the N-Queens problem.

    args:
        n (int): the size of the board.
        row (int): the current row we are placing.
        board (list): the list of placed queens so far.
    """
    # base case: if we have placed 'n' queens, we found a solution!
    if row == n:
        print(board)
        return

    # recursive step: try every column in the current row
    for col in range(n):
        if is_safe(board, row, col):
            # if safe, place the queen temporarily
            board.append([row, col])

            # recurse: try to place a queen in the next row
            solve_nqueens(n, row + 1, board)

            # backtrack: remove the queen and try the next column
            board.pop()


def main():
    """
    Main entry point for the N-Queens solver.
    Handles argument validation.
    """
    # argument validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # start the solver
    # we start at row 0 with an empty board list
    solve_nqueens(n, 0, [])


if __name__ == "__main__":
    main()

