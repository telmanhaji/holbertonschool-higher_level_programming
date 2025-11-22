#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    This module prints the first x elements of a list and only integers.
    """
    count = 0

    # iterating x times
    for i in range(x):
        try:
            # it enforces integer formatting.
            # if my_list[i] is a string, this raises ValueError/TypeError.
            # if i is out of bounds, this raises IndexError.
            print("{:d}".format(my_list[i]), end="")

            # if successful, increments the counter
            count += 1

        except (ValueError, TypeError):
            # It catches ONLY type errors (junk data) and ignore them.
            pass

        # note: it does NOT catch IndexError.
        # if x is too big, the script is supposed to crash (traceback).

    print()
    return count
