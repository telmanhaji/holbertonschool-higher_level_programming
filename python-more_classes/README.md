# Python - More Classes and Objects

This project expands on the concepts of Object-Oriented Programming (OOP) in Python. It dives deeper into **Class vs. Instance** attributes, magic methods (like `__str__`, `__repr__`, and `__del__`), and the usage of static and class methods.

## 📚 Resources

**Read or watch:**

* **Object Oriented Programming** (*Read everything until the paragraph “Inheritance” (excluded)*)
* **Object-Oriented Programming**
    * *Note: Read ONLY the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The `__init__` Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “`__str__`- and `__repr__`-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”*
* **Class and Instance Attributes**
* **classmethods and staticmethods**
* **Properties vs. Getters and Setters** (*Mainly the last part “Public instead of Private Attributes”*)
* **str vs repr**

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to **explain to anyone**, **without the help of Google**:

### General
* Why Python programming is awesome
* What is **OOP** and "first-class everything"
* What is a class, an object, and an instance
* The difference between a class and an object or instance
* What is an attribute
* What are and how to use **public**, **protected**, and **private** attributes
* What is `self`
* What is a method
* What is the special `__init__` method and how to use it
* **Data Abstraction**, **Data Encapsulation**, and **Information Hiding**
* What is a **property**
* The difference between an attribute and a property in Python
* The Pythonic way to write getters and setters in Python
* What are the special `__str__` and `__repr__` methods and how to use them
* The difference between `__str__` and `__repr__`
* What is a **class attribute**
* The difference between an object attribute and a class attribute
* What is a **class method**
* What is a **static method**
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to objects and classes
* What is and what does `__dict__` contain (of a class and of an instance)
* How Python finds the attributes of an object or class
* How to use the `getattr` function

---

## ⚙️ Requirements

### General
* **Allowed editors:** `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

---

## 📂 Tasks

### 0. Simple rectangle
Write an empty class `Rectangle` that defines a rectangle.
* You are not allowed to import any module.

**File:** `0-rectangle.py`

### 1. Real definition of a rectangle
Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)
* **Private instance attribute:** `width`
    * Property `def width(self):` to retrieve it
    * Property setter `def width(self, value):` to set it
        * `width` must be an integer, otherwise raise a `TypeError` (`width must be an integer`)
        * if `width` < 0, raise a `ValueError` (`width must be >= 0`)
* **Private instance attribute:** `height`
    * Property `def height(self):` to retrieve it
    * Property setter `def height(self, value):` to set it
        * `height` must be an integer, otherwise raise a `TypeError` (`height must be an integer`)
        * if `height` < 0, raise a `ValueError` (`height must be >= 0`)
* **Instantiation:** `def __init__(self, width=0, height=0):`
* You are not allowed to import any module.

**File:** `1-rectangle.py`

### 2. Area and Perimeter
Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)
* **Attributes:** Same as Task 1.
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter.
    * If `width` or `height` is equal to 0, perimeter is equal to 0.
* You are not allowed to import any module.

**File:** `2-rectangle.py`

### 3. String representation
Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)
* **Attributes & Methods:** Same as Task 2.
* `print()` and `str()` should print the rectangle with the character `#`.
    * If `width` or `height` is equal to 0, return an empty string.
* You are not allowed to import any module.

**File:** `3-rectangle.py`

### 4. Eval is magic
Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)
* **Attributes & Methods:** Same as Task 3.
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
* You are not allowed to import any module.

**File:** `4-rectangle.py`

### 5. Detect instance deletion
Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)
* **Attributes & Methods:** Same as Task 4.
* Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted.
* You are not allowed to import any module.

**File:** `5-rectangle.py`

### 6. How many instances
Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)
* **Public class attribute:** `number_of_instances`
    * Initialized to `0`.
    * Incremented during each new instance instantiation.
    * Decremented during each instance deletion.
* **Attributes & Methods:** Same as Task 5.
* You are not allowed to import any module.

**File:** `6-rectangle.py`

### 7. Change representation
Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)
* **Public class attribute:** `print_symbol`
    * Initialized to `#`.
    * Used as the symbol for string representation.
    * Can be any type.
* **Attributes & Methods:** Same as Task 6.
* `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`.
* You are not allowed to import any module.

**File:** `7-rectangle.py`



### 8. Compare rectangles
Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)
* **Static method:** `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area.
    * `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` (`rect_1 must be an instance of Rectangle`).
    * `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` (`rect_2 must be an instance of Rectangle`).
    * Returns `rect_1` if both have the same area value.
* **Attributes & Methods:** Same as Task 7.
* You are not allowed to import any module.

**File:** `8-rectangle.py`

### 9. A square is a rectangle
Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)
* **Class method:** `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`.
* **Attributes & Methods:** Same as Task 8.
* You are not allowed to import any module.

**File:** `9-rectangle.py`

---

## 📋 Repository Information
* **GitHub repository:** `holbertonschool-higher_level_programming`
* **Directory:** `python-more_classes`

