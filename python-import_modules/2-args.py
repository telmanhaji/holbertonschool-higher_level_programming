#!/usr/bin/python3
"""
A script that outputs the number of arguments and the list of arguments.
"""
import sys

if __name__ == "__main__":
    # 1.Calculate the number of arguments
    # subtracts 1 because the first item (index 0) is the script name
    count = len(sys.argv) - 1

    # 2.Handle the grammar (0 arguments)
    if count == 0:
        print("0 arguments.")

    # 3.Handle the grammar (1 argument)
    elif count == 1:
        print("1 argument:")

    # 4.Handle the grammar (2 or more arguments)
    else:
        print("{} arguments:".format(count))

    # 5.Loop
    # If have arguments (count >= 1), it needs to list them.
    # iterates starting from index 1 up to the end.
    if count >= 1:
        for i in range(1, count + 1):
            # Print "Position: Value"
            print("{}: {}".format(i, sys.argv[i]))
