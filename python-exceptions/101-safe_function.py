#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    this module executes a function safely.
    if it fails, prints the error to stderr and returns None.
    """
    try:
        # 1st. the magic execution
        # it calls the function 'fct'.
        # it uses *args to unpack whatever arguments were passed in.
        result = fct(*args)

        # 2nd. it returns the result if successful
        return result

    except Exception as e:
        # 3rd. catch EVERYTHING
        # "exception" is the parent class of almost all errors
        # (ValueError, ZeroDivisionError, IndexError, etc.)

        # 4th. it prints to Standard Error
        print("Exception: {}".format(e), file=sys.stderr)

        # 5th. it returns None to signal failure
        return None
