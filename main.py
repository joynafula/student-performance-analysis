"""
Student Database Management System
A simple command-line CRUD application using Python's built-in sqlite3 module.

Run:
    python main.py

The SQLite database file (students.db) is created automatically in this folder.
"""

import sqlite3
from pathlib import Path

DATABASE_FILE = Path(__file__).with_name("students.db")


def connect():
    """Open a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_FILE)


def create_table():
    """Create the students table if it does not already exist."""
    with connect() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                age INTEGER NOT NULL,
                course TEXT NOT NULL,
                email TEXT UNIQUE
            )
        """)
    print("Database is ready.")


def add_student():
    """Collect details and insert a student record."""
    name = input("Full name: ").strip()
    age_text = input("Age: ").strip()
    course = input("Course: ").strip()
    email = input("Email (optional): ").strip() or None

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        age = int(age_text)
        if age <= 0:
            print("Age must be a positive number.")
            return

        with connect() as connection:
            connection.execute(
                """INSERT INTO students (full_name, age, course, email)
                   VALUES (?, ?, ?, ?)""",
                (name, age, course, email)
            )
        print("Student added successfully.")

    except ValueError:
        print("Please enter a valid whole number for age.")
    except sqlite3.IntegrityError:
        print("That email address is already in use.")


def view_students():
    """Display all student records."""
    with connect() as connection:
        records = connection.execute(
            """SELECT student_id, full_name, age, course, email
               FROM students ORDER BY student_id"""
        ).fetchall()

    if not records:
        print("No student records found.")
        return

    print("\nID | Name | Age | Course | Email")
    print("-" * 65)
    for record in records:
        print(" | ".join(str(value) if value is not None else "-" for value in record))


def search_student():
    """Find a student by their database ID."""
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    with connect() as connection:
        record = connection.execute(
            """SELECT student_id, full_name, age, course, email
               FROM students WHERE student_id = ?""",
            (student_id,)
        ).fetchone()

    if record:
        print("ID | Name | Age | Course | Email")
        print(" | ".join(str(value) if value is not None else "-" for value in record))
    else:
        print("Student not found.")


def update_student():
    """Update a student's name, age, course and email."""
    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    print("Enter the new details.")
    name = input("New full name: ").strip()
    age_text = input("New age: ").strip()
    course = input("New course: ").strip()
    email = input("New email (optional): ").strip() or None

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        age = int(age_text)
        if age <= 0:
            print("Age must be a positive number.")
            return

        with connect() as connection:
            cursor = connection.execute(
                """UPDATE students
                   SET full_name = ?, age = ?, course = ?, email = ?
                   WHERE student_id = ?""",
                (name, age, course, email, student_id)
            )

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            print("Student updated successfully.")

    except ValueError:
        print("Please enter a valid whole number for age.")
    except sqlite3.IntegrityError:
        print("That email address is already in use.")


def delete_student():
    """Delete a student record by ID after confirmation."""
    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    confirmation = input("Are you sure you want to delete this record? (y/n): ").lower()
    if confirmation != "y":
        print("Deletion cancelled.")
        return

    with connect() as connection:
        cursor = connection.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student deleted successfully.")


def show_menu():
    """Display the application menu."""
    print("\nSTUDENT DATABASE MANAGEMENT SYSTEM")
    print("1. Add student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Update student")
    print("5. Delete student")
    print("0. Exit")


def main():
    create_table()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please choose 0 to 5.")


if __name__ == "__main__":
    main()
