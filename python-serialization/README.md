# Python - Serialization

## 📝 Introduction

This project is designed to enhance your understanding and practical skills in handling data in real-world applications. You will learn to manipulate and manage data effectively, preparing you for advanced topics in software development, distributed computing, and data persistence.

### Key Concepts

#### 🧩 What is Marshaling?
Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is crucial in scenarios such as remote procedure calls (RPC), where objects need to be represented in a standard format across different computing platforms.

#### 📦 What is Serialization?
Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network.
* **Serialization:** Preserves the state of an object to recreate it later.
* **Deserialization:** The reverse process of reconstructing the object from the serialized format.

## 🎯 Learning Objectives

By the end of this project, you should be able to:
* Articulate the differences and similarities between marshaling and serialization.
* Implement serialization in a practical programming task.
* Understand how serialized data can be used in web applications, databases, and network communications.
* Evaluate the performance implications of different serialization formats, like **JSON**, **XML**, and **binary formats** (Pickle).

## 📚 Resources

* [Real Python Serialization](https://realpython.com/python-serialization/)
* [Real Python: Working With JSON Data in Python](https://realpython.com/python-json/)
* [Python’s pickle documentation](https://docs.python.org/3/library/pickle.html)
* [Corey Schafer on Pickle](https://www.youtube.com/watch?v=2Tw39kP415)
* [CSV to JSON in Python](https://www.geeksforgeeks.org/convert-csv-to-json-using-python/)
* [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
* [Socket Programming Guide](https://docs.python.org/3/howto/sockets.html)

---

## 📂 Tasks

### 0. Basic Serialization
Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

**Instructions:**
Write a Python module named `task_00_basic_serialization.py` with the following functions:

* `def serialize_and_save_to_file(data, filename):`
    * **data:** A Python Dictionary with data.
    * **filename:** The filename of the output JSON file. If the output file already exists it should be replaced.
* `def load_and_deserialize(filename):`
    * **filename:** The filename of the input JSON file.
    * **Returns:** A Python Dictionary with the deserialized JSON data from the file.

**File:** `task_00_basic_serialization.py`

### 1. Pickling Custom Classes
Learn how to serialize and deserialize custom Python objects using the `pickle` module.


**Instructions:**
1.  Create a custom Python class named `CustomObject` with attributes: `name` (string), `age` (integer), `is_student` (boolean).
2.  Add a method `display` to print attributes in the format:
    ```text
    Name: John
    Age: 25
    Is Student: True
    ```
3.  Implement two methods within this class:
    * `serialize(self, filename)`: Uses `pickle` to save the current instance to the provided filename.
    * `@classmethod deserialize(cls, filename)`: Uses `pickle` to load and return an instance of `CustomObject` from the filename.
4.  **Error Handling:** Handle exceptions for non-existent or malformed files (return `None`).

**File:** `task_01_pickle.py`

### 2. Converting CSV Data to JSON Format
Gain experience in reading data from one format (CSV) and converting it into another format (JSON).

**Instructions:**
1.  Import `csv` and `json` modules.
2.  Define `convert_csv_to_json(csv_filename)`.
3.  Use `csv.DictReader` to convert each row into a dictionary.
4.  Serialize the list of dictionaries to `data.json`.
5.  **Returns:** `True` if successful, `False` if exceptions occur (e.g., file not found).

**Example Output:**
```json
[
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"}
]