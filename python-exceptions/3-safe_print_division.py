#!/usr/bin/python3
def safe_print_division(a, b):
    """
    This module divides 2 integers and prints the result.
    """
    try:
        # 1st. it attempts the division
        result = a / b
    except ZeroDivisionError:
        # 2nd. it catches the specific error if b is 0
        result = None
    finally:
        # 3rd. this block executes NO MATTER WHAT.
        # whether the division worked or failed, it prints the status here.
        print("Inside result: {}".format(result))

    # 4th. It returns the value to the main program
    return result
