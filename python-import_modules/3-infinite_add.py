#!/usr/bin/python3
"""
This module adds all arguments and outputs the result.
"""

if __name__ == "__main__":
    import sys

    # 1.Creating the 'bucket' (accumulator problem)
    total = 0

    # 2.Loop through arguments, skipping the first one ("program name")
    #    sys.argv[1:] creates a new list without the "program name"
    for arg in sys.argv[1:]:
        # 3. Convert the string to an int and add it to total
        total += int(arg)

    # 4.Outputs the final result
    print("{}".format(total))
