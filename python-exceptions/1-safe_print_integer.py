#!/usr/bin/python3
def safe_print_integer(value):
    """
    This module prints an integer with "{:d}".format().
    returns true if successful, false otherwise.
    """
    try:
        # the dangerous operation
        # It attempts to format the input as a decimal integer (:d)
        print("{:d}".format(value))

        # if the line above succeeded, it reaches this line:
        return True

    except (ValueError, TypeError):
        # if 'value' was a string (ValueError) or None (TypeError),
        # it jumps here immediately.
        # it returns False to indicate the print failed.
        return False
