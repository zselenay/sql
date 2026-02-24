# Simple Library Management System (SQLite3)

This Python script demonstrates how to create and manage a basic relational database for a library using the built-in `sqlite3` module. It sets up the database schema, populates it with sample data, and runs SQL queries to extract meaningful information using table joins.

##  Features

* **Relational Database Design:** Implements Foreign Keys to link members, books, and their loan records.
* **Idempotent Data Insertion:** Uses `INSERT OR IGNORE` to ensure that running the script multiple times does not create duplicate entries.
* **SQL Joins:** Demonstrates how to connect multiple tables (`books`, `members`, and `loans`) to find specific insights, such as unreturned books.
* **Sorting:** Uses `ORDER BY` to sort loan records chronologically.

##  Database Schema


The script creates a local SQLite database named `library.db` consisting of three tables:

* **`books`**: Stores book details (`id`, `title`, `author`, `genre`, `year`).
* **`members`**: Stores library member details (`id`, `name`).
* **`loans`**: Tracks which member borrowed which book and when (`id`, `members_id`, `books_id`, `loan_date`, `return_date`).

##  How to Run

1. Ensure you have Python installed on your system (no external libraries are required since `sqlite3` is built-in).
2. Download or clone this repository.
3. Open your terminal and run the script:
   ```bash
   python library_db.py
