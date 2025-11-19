#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples.
    """
    # 1st. Sanitization step (the "padding" trick)
    # We create temporary variables (a and b).
    # We add (0, 0) to the end of whatever we received.
    # This ensures the tuple has AT LEAST 2 items.
    # Example: If tuple_a was (1,), 'a' becomes (1, 0, 0).
    a = tuple_a + (0,0)
    b = tuple_b + (0,0)

    # 2nd. Calculation step
    # Now we can safely access index [0] and [1] without fear of an IndexError.
    # Even if the original tuple was huge (1, 2, 3, 4), accessing [0] and [1]
    # automatically ignores the extra stuff (3, 4).
    sum_1 = a[0] + b[0]
    sum_2 = a[1] + b[1]

    # 3rd. Return step
    # Packaging the two sums into a new tuple and return it
    return (sum_1, sum_2)
