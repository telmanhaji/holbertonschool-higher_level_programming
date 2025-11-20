#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    # uses list() to convert the map iterators back into real lists.
    # Step 1 (outer): map through 'matrix'. each item is a 'row'.
    # Step 2 (inner): map through 'row'. each item is 'x'. square 'x'.
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
