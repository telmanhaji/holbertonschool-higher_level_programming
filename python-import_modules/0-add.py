#!/usr/bin/python3
# mandatory comment for file 0-add.py
"""this module for task "0. Import a simple function from a simple file"."""
"""It`s imports the 'add' function and prints the result of 1 + 2."""

# This 'if' block is the "guard".
# The code inside it will NOT run if this file is imported.
if __name__ == "__main__":
    # 1. Import the function
    #    I do this INSIDE the guard
    from add_0 import add

    # 2. Assigning the variables
    a = 1
    b = 2

    # 3. Call the function and display the result
    #    I use f-string as required in task 0.
    print(f"{a} + {b} = {add(a, b)}")
