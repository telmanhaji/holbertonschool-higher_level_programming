# SQL - Introduction

This project introduces the fundamentals of **Relational Databases** using **MySQL**. It covers the basics of **SQL** (Structured Query Language), including Data Definition Language (DDL) and Data Manipulation Language (DML). You will learn how to create databases, manage tables, and perform various operations on data such as insertion, selection, updates, and deletion.



[Image of relational database model diagram]


## 📚 Resources

**Read or watch:**

* What is Database & SQL?
* Install MySQL (MySQL Server)
* A Basic MySQL Tutorial
* Basic SQL statements: DDL and DML
* Basic queries: SQL and RA
* SQL technique: functions
* SQL technique: subqueries
* What makes the big difference between a backtick and an apostrophe?
* MySQL Cheat Sheet
* MySQL 8.0 SQL Statement Syntax

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to **explain to anyone**, **without the help of Google**:

### General
* What’s a **database**
* What’s a **relational database**
* What does **SQL** stand for
* What’s **MySQL**
* How to create a database in MySQL
* What does **DDL** and **DML** stand for
* How to `CREATE` or `ALTER` a table
* How to `SELECT` data from a table
* How to `INSERT`, `UPDATE` or `DELETE` data
* What are **subqueries**
* How to use MySQL functions



---

## ⚙️ Requirements

### General
* **Allowed editors:** `vi`, `vim`, `emacs`
* All your files will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0** (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in **uppercase** (`SELECT`, `WHERE`…)
* A `README.md` file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using `wc`

### 📝 Comments Example
Your SQL files should look like this:
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
💻 Installation & Setup (Sandbox)
If working on Ubuntu 20.04/22.04 containers:

Install MySQL Server:

Bash

$ sudo apt update
$ sudo apt install -y mysql-server
Start the Service:

Bash

$ service mysql start
Connect:

Bash

$ mysql -uroot -p
📂 Tasks
0. List databases
Write a script that lists all databases of your MySQL server.

File: 0-list_databases.sql

1. Create a database
Write a script that creates the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 already exists, your script should not fail.

You are not allowed to use the SELECT or SHOW statements.

File: 1-create_database_if_missing.sql

2. Delete a database
Write a script that deletes the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 doesn’t exist, your script should not fail.

You are not allowed to use the SELECT or SHOW statements.

File: 2-remove_database.sql

3. List tables
Write a script that lists all the tables of a database in your MySQL server.

The database name will be passed as argument of mysql command.

File: 3-list_tables.sql

4. First table
Write a script that creates a table called first_table in the current database in your MySQL server.

Description:

id: INT

name: VARCHAR(256)

The database name will be passed as an argument of the mysql command.

If the table first_table already exists, your script should not fail.

You are not allowed to use the SELECT or SHOW statements.

File: 4-first_table.sql

5. Full description
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command.

You are not allowed to use the DESCRIBE or EXPLAIN statements.

File: 5-full_table.sql

6. List all in table
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

All fields should be printed.

The database name will be passed as an argument of the mysql command.

File: 6-list_values.sql

7. First add
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

New row: id = 89, name = "Best School"

The database name will be passed as an argument of the mysql command.

File: 7-insert_value.sql

8. Count 89
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command.

File: 8-count_89.sql

9. Full creation
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and adds multiple rows.

Description:

id: INT

name: VARCHAR(256)

score: INT

The database name will be passed as an argument to the mysql command.

If the table second_table already exists, your script should not fail.

You are not allowed to use the SELECT and SHOW statements.

Records to create:

id = 1, name = “John”, score = 10

id = 2, name = “Alex”, score = 3

id = 3, name = “Bob”, score = 14

id = 4, name = “George”, score = 8

File: 9-full_creation.sql

10. List by best
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order).

Records should be ordered by score (top first).

The database name will be passed as an argument of the mysql command.

File: 10-top_score.sql

11. Select the best
Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order).

Records should be ordered by score (top first).

The database name will be passed as an argument of the mysql command.

File: 11-best_score.sql

12. Cheating is bad
Write a script that updates the score of Bob to 10 in the table second_table.

You are not allowed to use Bob’s id value, only the name field.

The database name will be passed as an argument of the mysql command.

File: 12-no_cheating.sql

13. Score too low
Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command.

File: 13-change_class.sql

14. Average
Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

The result column name should be average.

The database name will be passed as an argument of the mysql command.

File: 14-average.sql

15. Number by score
Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

The result should display:

the score

the number of records for this score with the label number

The list should be sorted by the number of records (descending).

The database name will be passed as an argument to the mysql command.

File: 15-groups.sql

16. Say my name
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Don’t list rows where the name column does not contain a value.

Results should display the score and the name (in this order).

Records should be listed by descending score.

The database name will be passed as an argument to the mysql command.

File: 16-no_link.sql
