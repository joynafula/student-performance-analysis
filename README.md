# Student Database Management System

**Project type:** Reconstructed learning / portfolio project  
**Level:** Beginner  
**Author:** Wanyonyi Joy Nafula

## Project overview

This is a small command-line application for managing student records. It uses Python for the application logic and SQLite for persistent storage.

This repository is a learning/portfolio implementation. It should not be described as an earlier project unless it accurately matches work previously completed.

## Features

- Add a student record.
- View all student records.
- Search for a student by ID.
- Update a student's details.
- Delete a student record after confirmation.

## Technologies

- Python 3
- SQLite
- Python `sqlite3` module (included in the Python standard library)

## Database design

The application uses one table named `students`.

| Column | Type | Purpose |
|---|---|---|
| `student_id` | INTEGER | Primary key generated automatically |
| `full_name` | TEXT | Student's name; required |
| `age` | INTEGER | Student's age; required |
| `course` | TEXT | Course; required |
| `email` | TEXT | Optional email; must be unique if supplied |

## Project files

- `main.py` — command-line application and database operations.
- `schema.sql` — SQL statement defining the table.
- `students.db` — created automatically when the application runs; not included in the repository.

## How to run

1. Install Python 3.
2. Open a terminal in this folder.
3. Run:

   ```bash
   python main.py
   ```

4. Select an option from the menu.
5. The `students.db` SQLite database is created in this folder automatically.

No third-party Python packages are required.

## SQL operations demonstrated

- `CREATE TABLE` — creates the student table.
- `INSERT` — adds a student.
- `SELECT` — retrieves student records.
- `UPDATE` — changes a student's details.
- `DELETE` — removes a student record.

The application uses parameterised SQL queries (`?` placeholders) rather than building SQL statements by joining user input into query strings.

## Limitations

- This is a local, single-user command-line demonstration.
- It has no login system or role-based access control.
- It does not include a graphical user interface.
- It is not intended for storing real or sensitive student information.

## Possible improvements

- Add input validation for email addresses and other fields.
- Add search by name or course.
- Add a graphical or web interface.
- Add automated tests.
- Add user authentication and appropriate access controls before any real-world deployment.

## Learning objectives

Practise Python functions, loops, conditionals, exception handling, database connections, SQL CRUD operations and parameterised queries.
