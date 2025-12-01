# Python - Network #1

This project introduces the foundations of networking in Python. You will learn how to fetch internet resources, manipulate data from external services, and handle HTTP requests using both the standard `urllib` library and the more user-friendly `requests` package.

## 📚 Resources

**Read or watch:**

* [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/user/quickstart/)
* [Requests package](https://requests.readthedocs.io/en/latest/)

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to **explain to anyone**, **without the help of Google**:

### General
* How to fetch internet resources with the Python package `urllib`
* How to decode `urllib` body response
* How to use the Python package `requests` *(#requestsiswaysimplerthanurllib)*
* How to make HTTP `GET` request
* How to make HTTP `POST`/`PUT`/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

---

## ⚙️ Requirements

### General
* **Allowed editors:** `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style
* All your files must be executable
* The length of your files will be tested using `wc`
* **Documentation:** All modules, classes, and methods must have docstrings.
    * `python3 -c 'print(__import__("my_module").__doc__)'`
* You must use `get` to access dictionary values by key (to avoid exceptions if the key doesn’t exist).
* Your code should not be executed when imported (use `if __name__ == "__main__":`).

### 🛡️ Intranet Firewall Note
The intranet is hosted behind a firewall. To allow your requests to bypass it, you need to add a specific header to your requests:
```python
{'cfclearance': 'true'}
📂 Tasks
0. What's my status? #0
Write a Python script that fetches https://intranet.hbtn.io/status.

Package: You must use urllib.

Output: The body of the response must be displayed in a specific format (see example).

Constraint: You must use a with statement.

File: 0-hbtn_status.py

1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the X-Request-Id variable found in the header of the response.

Packages: urllib and sys.

Constraint: You must use a with statement.

File: 1-hbtn_header.py

2. POST an email #0
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8).

Parameter: The email must be sent in the email variable.

Packages: urllib and sys.

Constraint: You must use a with statement.

File: 2-post_email.py

3. Error code #0
Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8).

Error Handling: Manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code.

Packages: urllib and sys.

Constraint: You must use a with statement.

File: 3-error_code.py

4. What's my status? #1
Write a Python script that fetches https://intranet.hbtn.io/status.

Package: You must use requests.

Output: Display the body of the response (see example).

File: 4-hbtn_status.py

5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.

Packages: requests and sys.

File: 5-hbtn_header.py

6. POST an email #1
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

Parameter: The email must be sent in the variable email.

Packages: requests and sys.

File: 6-post_email.py

7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response.

Error Handling: If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code.

Packages: requests and sys.

File: 7-error_code.py

8. Search API
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

Parameter: The letter must be sent in the variable q.

Logic:

If no argument is given, set q="".

If the response body is properly JSON formatted and not empty, display [<id>] <name>.

If JSON is invalid, display Not a valid JSON.

If JSON is empty, display No result.

Packages: requests and sys.

File: 8-json_api.py

9. My GitHub!
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.

Auth: You must use Basic Authentication with a personal access token as the password.

Arguments: The first argument is your username, the second is your password (PAT).

Packages: requests and sys.

File: 10-my_github.py

📋 Repository Information
GitHub repository: holbertonschool-higher_level_programming

Directory: python-network_1
