# Python - Server-Side Rendering

Server-side rendering (SSR) is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML. This contrasts with client-side rendering, where the browser builds the web page using JavaScript and dynamic data.

Through this project, you will learn how to implement SSR using **Python** and **Flask**, leveraging the **Jinja** templating engine to create dynamic, efficient, and SEO-friendly web applications.



## 📚 Resources

**Read or watch:**

* [MDN Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Introduction)
* [Templating Engines in Web Development](https://www.freecodecamp.org/news/what-are-templating-engines-and-how-do-they-work/)
* [Flask Official Documentation](https://flask.palletsprojects.com/)
* [Python JSON Documentation](https://docs.python.org/3/library/json.html)
* [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
* [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
* [Jinja2 Documentation](https://jinja.palletsprojects.com/)

---

## 🎯 Learning Objectives


* Understand the concepts of **server-side rendering** and how it differs from client-side rendering.
* Learn the benefits of using server-side rendering in web development.
* Implement SSR in Python using the **Flask framework**.
* Utilize **Jinja templating engine** to dynamically generate HTML pages.
* Read and display data from various sources including **JSON**, **CSV**, and **SQLite databases**.
* Handle dynamic content and user inputs in web applications.

---

## 🚀 What to Expect

In this project, you will build a Flask application that serves web pages using server-side rendering techniques. You will start by creating basic templates and gradually move towards integrating dynamic content from multiple data sources. By the end of the project, you will have a comprehensive understanding of SSR, templating, and how to build efficient, scalable web applications.

---

## 📂 Tasks

### 0. Creating a Simple Templating Program
Create a Python function that generates personalized invitation files from a template with placeholders and a list of objects.
* **Function:** `generate_invitations(template, attendees)`
* **Logic:** Replace placeholders (`{name}`, `{event_title}`, etc.) with actual data.
* **Output:** Generate sequential files (`output_1.txt`, `output_2.txt`, etc.).
* **Error Handling:** Manage empty inputs, missing data, and invalid types.

**File:** `task_00_intro.py`

### 1. Creating a Basic HTML Template in Flask
Build a basic Flask application that serves a web page using a Jinja template.
* **Setup:** Install Flask and create `task_01_jinja.py`.
* **Templates:** Create `index.html`, `about.html`, and `contact.html`.
* **Inheritance:** Use `header.html` and `footer.html` for consistent layout.
* **Routes:** Implement routes for `/`, `/about`, and `/contact`.

**File:** `task_01_jinja.py`

### 2. Creating a Dynamic Template with Loops and Conditions
Enhance your Flask application by integrating dynamic content using Jinja’s loop and conditional constructs.
* **Data:** Read from `items.json`.
* **Template:** Create `items.html` to display a list of items.
* **Logic:** Use `{% for %}` loops and `{% if %}` conditions (e.g., display "No items found" if the list is empty).
* **Route:** `/items`.

**File:** `task_02_logic.py`

### 3. Displaying Data from JSON or CSV Files
Build a feature to read and display product data from different formats based on a query parameter.
* **Data Sources:** `products.json` and `products.csv`.
* **Route:** `/products?source=json` or `/products?source=csv`.
* **Filtering:** Support optional `id` parameter to filter results.
* **Error Handling:** Display error messages for invalid sources or missing product IDs.

**File:** `task_03_files.py`

### 4. Extending Dynamic Data Display to Include SQLite
Extend the application to fetch and display data from a SQLite database.
* **Database:** Create and populate `products.db`.
* **Logic:** Handle `source=sql` query parameter.
* **Consistency:** Use the same `product_display.html` template for JSON, CSV, and SQL data.
* **Interaction:** Use the `sqlite3` module to query the database.

**File:** `task_04_db.py`

---

## 📋 Repository Information
* **GitHub repository:** `holbertonschool-higher_level_programming`
* **Directory:** `python-server_side_rendering`