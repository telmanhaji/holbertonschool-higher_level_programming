#!/usr/bin/python3
# 1-calculation.py
"""This module imports 4 functions from calculator_1.py
and displays the results of calculations.
"""

# The "guard" block. Code inside only runs
# when the script is executed directly.
if __name__ == "__main__":

    # 1. Import all the functions we need
    #    This follows the "no *" and "use once" rules
    from calculator_1 import add, sub, mul, div

    # 2. Assign the variables on separate lines
    a = 10
    b = 5

    # 3. Call each function and display the result
    #    We use the .format() method to pass the checker
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
