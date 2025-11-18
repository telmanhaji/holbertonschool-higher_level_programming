# Python: Data Structures - Lists and Tuples

This project focuses on understanding and manipulating Python lists, strings, and tuples, which are fundamental data structures in high-level programming. The tasks involve creating functions to perform common operations like accessing elements, modifying lists, printing in different orders, and working with multi-dimensional data structures (matrices) and sequences.

---

## Learning Objectives

Upon completing this project, you will be proficient in explaining:

### General Concepts
* What are lists and how to effectively use them.
* The differences and similarities between strings and lists.
* The most common methods of lists and their usage.
* How to utilize lists as stacks and queues.
* What are list comprehensions and how to use them.
* What are tuples and how to use them.
* When to use tuples versus lists.
* What constitutes a sequence in Python.
* The concepts of tuple packing and sequence unpacking.
* The purpose and usage of the `del` statement.

---

## Project Requirements

### Python Scripts
* Editors: `vi`, `vim`, or `emacs`.
* Environment: Interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
* File Endings: All files must end with a new line.
* Shebang: The first line of all files must be `#!/usr/bin/python3`.
* Documentation: A `README.md` file is mandatory at the root of the project folder.
* Style: Code must adhere to `pycodestyle` (version 2.7.*).
* Permissions: All files must be executable.
* Length Check: File lengths will be tested using `wc`.

### Repository Details
* GitHub Repository: `holbertonschool-higher_level_programming`
* Project Directory: `python-data_structures`

---

## Mandatory Tasks Summary

| Task # | File Name | Function Prototype | Description | Constraints |
| :---: | :--- | :--- | :--- | :--- |
| 0 | `0-print_list_integer.py` | `def print_list_integer(my_list=[]):` | Prints all integers of a list, one per line, using `str.format()`. | No module import, no casting to string. |
| 1 | `1-element_at.py` | `def element_at(my_list, idx):` | Retrieves an element at a specific index, returning `None` for negative or out-of-range indices. | No module import, no `try/except`. |
| 2 | `2-replace_in_list.py` | `def replace_in_list(my_list, idx, element):` | Replaces an element at a specific index. Returns the original list unchanged for invalid indices. | No module import, no `try/except`. |
| 3 | `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):` | Prints all integers of a list in reverse order, one per line, using `str.format()`. | No module import, no casting to string. |
| 4 | `4-new_in_list.py` | `def new_in_list(my_list, idx, element):` | Replaces an element in a copy of the list, ensuring the original list is not modified. | Returns a copy of the original list for invalid indices. No module import, no `try/except`. |
| 5 | `5-no_c.py` | `def no_c(my_string):` | Removes all occurrences of characters 'c' and 'C' from a string. | No module import, no `str.replace()`. |
| 6 | `6-print_matrix_integer.py` | `def print_matrix_integer(matrix=[[]]):` | Prints a matrix (list of lists) of integers. | No module import, no casting to string, use `str.format()`. |
| 7 | `7-add_tuple.py` | `def add_tuple(tuple_a=(), tuple_b=()):` | Adds two tuples, returning a new tuple with 2 integers. Handles tuples of different sizes by padding missing values with 0 or truncating to the first two elements. | No module import. |
| 8 | `8-multiple_returns.py` | `def multiple_returns(sentence):` | Returns a tuple containing the length of a string and its first character. First character is `None` if the string is empty. | No module import. |
| 9 | `9-max_integer.py` | `def max_integer(my_list=[]):` | Finds and returns the biggest integer of a list. Returns `None` if the list is empty. | No module import, no built-in `max()`. |
| 10 | `10-divisible_by_2.py` | `def divisible_by_2(my_list=[]):` | Creates a new list of the same size with `True` or `False` indicating if the corresponding element in the original list is a multiple of 2. | No module import. |
| 11 | `11-delete_at.py` | `def delete_at(my_list=[], idx=0):` | Deletes the item at a specific position. Returns the same list if the index is invalid. | No module import, no built-in `pop()`. |
| 12 | `12-switch.py` | *No prototype* | Completes the given source code to switch the values of variables `a` and `b`. | Code must be exactly 5 lines long. |

