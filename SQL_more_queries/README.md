# SQL - MySQL

This project advances into intermediate SQL concepts using **MySQL**. It covers user management, privileges, database constraints, and advanced query techniques such as **Joins**, **Unions**, and **Subqueries**. You will also learn how to model data relationships using Primary and Foreign Keys.

## 📚 Resources

**Read or watch:**

* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
* [MySQL constraints](https://dev.mysql.com/doc/refman/8.0/en/constraints.html)
* [Basic query operation: the join](https://en.wikipedia.org/wiki/Join_(SQL))
* [SQL technique: multiple joins and the distinct keyword](https://www.sqlshack.com/sql-multiple-joins/)
* [SQL technique: join types](https://www.w3schools.com/sql/sql_join.asp)
* [SQL technique: subqueries](https://www.w3schools.com/sql/sql_subqueries.asp)
* [SQL technique: union and minus](https://www.w3schools.com/sql/sql_union.asp)
* [MySQL Cheat Sheet](https://devhints.io/mysql)
* [The Seven Types of SQL Joins](https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/)
* [MySQL Tutorial](https://www.mysqltutorial.org/)
* [SQL Style Guide](https://www.sqlstyle.guide/)
* [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

**Extra resources around relational database model design:**
* Design
* Normalization
* ER Modeling

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to **explain to anyone**, **without the help of Google**:

### General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a **PRIMARY KEY**
* What’s a **FOREIGN KEY**
* How to use `NOT NULL` and `UNIQUE` constraints
* How to retrieve data from multiple tables in one request
* What are **subqueries**
* What are `JOIN` and `UNION`

---

## ⚙️ Requirements

### General
* **Allowed editors:** `vi`, `vim`, `emacs`
* All your files will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0** (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before
* All your files should start by a comment describing the task
* All SQL keywords should be in **uppercase** (`SELECT`, `WHERE`…)
* A `README.md` file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using `wc`

### 📝 SQL File Comments
Your SQL files should follow this comment structure:
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;