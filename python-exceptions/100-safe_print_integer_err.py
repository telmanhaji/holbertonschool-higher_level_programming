#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    this module prints an integer with "{:d}".format().
    if it fails, prints the error message to stderr.
    """
    try:
        # 1st. it tries to print formatted as an integer
        print("{:d}".format(value))
        return True

    # 2nd. It catches the error and store the message in variable 'e'
    except (ValueError, TypeError) as e:
        # 3rd. it prints to Standard Error
        # it formats it exactly as requested: "Exception: <error message>"
        # file=sys.stderr sends it to the error stream.
        print("Exception: {}".format(e), file=sys.stderr)
        return False
