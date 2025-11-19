#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Outputs a matrix of integers.
    """
    # 1st. The Outer Loop: Go through every row in the matrix
    for row in matrix:
        # 2nd. The Inner Loop: Go through every number in the current row
        # We use range(len(row)) so we know the index (position) of each number
        for i in range(len(row)):

            # 3rd. Check if we are at the very last number of the row
            if i != len(row) - 1:
                # If NOT the last number, print with a space at the end
                print("{:d}".format(row[i]), end=" ")
            else:
                # If it IS the last number, print normally (no space suffix)
                # But we use end="" to avoid the default newline here,
                # because we handle the newline manually after the loop.
                print("{:d}".format(row[i]), end="")

        # 4th. After finishing all columns in a row, print a New Line
        print()
