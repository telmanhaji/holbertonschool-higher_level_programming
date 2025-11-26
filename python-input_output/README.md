# Python - Input/Output

This project delves into the mechanics of input and output in Python. It covers reading from and writing to files, understanding the concept of file cursors, and mastering serialization and deserialization using JSON.

## 📚 Resources

* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* **Dive Into Python 3:** Chapter 11. Files (until “11.4 Binary Files” (included))
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* **Learn to Program 8:** Reading / Writing Files
* **Automate the Boring Stuff with Python:** (ch. 8 p 180-183 and ch. 14 p 326-333)
* **sys package**

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to **explain to anyone**, **without the help of Google**:

### General
* Why Python programming is awesome
* How to **open** a file
* How to **write** text in a file
* How to **read** the full content of a file
* How to **read** a file line by line
* How to **move the cursor** in a file
* How to make sure a file is **closed** after using it
* What is and how to use the `with` statement
* What is **JSON**
* What is **serialization**
* What is **deserialization**
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure
* How to access command line parameters in a Python script


---

## ⚙️ Requirements

### Python Scripts
* **Allowed editors:** `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

### Python Test Cases
* **Allowed editors:** `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* All your test files should be text files (extension: `.txt`)
* All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
* **Documentation:** All modules, classes, and functions should have documentation strings.
* *We strongly encourage you to work together on test cases so that you don’t miss any edge cases.*

---

## 📂 Tasks

### 0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout.
* **Prototype:** `def read_file(filename=""):`
* You must use the `with` statement.
* You don’t need to manage file permissions or file doesn't exist exceptions.
* You are not allowed to import any module.

**File:** `0-read_file.py`

### 1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns the number of characters written.
* **Prototype:** `def write_file(filename="", text=""):`
* You must use the `with` statement.
* You don’t need to manage file permission exceptions.
* Your function should create the file if it doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module.

**File:** `1-write_file.py`

### 2. Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
* **Prototype:** `def append_write(filename="", text=""):`
* If the file doesn’t exist, it should be created.
* You must use the `with` statement.
* You don’t need to manage file permissions or file doesn't exist exceptions.
* You are not allowed to import any module.

**File:** `2-append_write.py`

### 3. To JSON string
Write a function that returns the JSON representation of an object (string).
* **Prototype:** `def to_json_string(my_obj):`
* You don’t need to manage exceptions if the object can’t be serialized.

**File:** `3-to_json_string.py`

### 4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string.
* **Prototype:** `def from_json_string(my_str):`
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.

**File:** `4-from_json_string.py`

### 5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation.
* **Prototype:** `def save_to_json_file(my_obj, filename):`
* You must use the `with` statement.
* You don’t need to manage exceptions if the object can’t be serialized.
* You don’t need to manage file permission exceptions.

**File:** `5-save_to_json_file.py`

### 6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”.
* **Prototype:** `def load_from_json_file(filename):`
* You must use the `with` statement.
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.
* You don’t need to manage file permissions / exceptions.

**File:** `6-load_from_json_file.py`

### 7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file.
* You must use your function `save_to_json_file` from `5-save_to_json_file.py`.
* You must use your function `load_from_json_file` from `6-load_from_json_file.py`.
* The list must be saved as a JSON representation in a file named `add_item.json`.
* If the file doesn’t exist, it should be created.
* You don’t need to manage file permissions / exceptions.

**File:** `7-add_item.py`

### 8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
* **Prototype:** `def class_to_json(obj):`
* `obj` is an instance of a Class.
* All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean.
* You are not allowed to import any module.

**File:** `8-class_to_json.py`

### 9. Student to JSON
Write a class `Student` that defines a student by:
* **Public instance attributes:** `first_name`, `last_name`, `age`.
* **Instantiation:** `def __init__(self, first_name, last_name, age):`
* **Public method:** `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`).
* You are not allowed to import any module.

**File:** `9-student.py`

### 10. Student to JSON with filter
Write a class `Student` that defines a student by: (based on `9-student.py`)
* **Public instance attributes:** `first_name`, `last_name`, `age`.
* **Instantiation:** `def __init__(self, first_name, last_name, age):`
* **Public method:** `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance:
    * If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
    * Otherwise, all attributes must be retrieved.
* You are not allowed to import any module.

**File:** `10-student.py`

### 11. Student to disk and reload
Write a class `Student` that defines a student by: (based on `10-student.py`)
* **Public instance attributes:** `first_name`, `last_name`, `age`.
* **Instantiation:** `def __init__(self, first_name, last_name, age):`
* **Public method:** `def to_json(self, attrs=None):` (Same as task 10).
* **Public method:** `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
    * You can assume `json` will always be a dictionary.
    * A dictionary key will be the public attribute name.
    * A dictionary value will be the value of the public attribute.
* You are not allowed to import any module.

**File:** `11-student.py`

### 12. Pascal's Triangle
**Technical interview preparation:**
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
* Returns an empty list if `n <= 0`.
* You can assume `n` will be always an integer.
* You are not allowed to import any module.

**File:** `12-pascal_triangle.py`
