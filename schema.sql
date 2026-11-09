-- Student Database Management System
-- SQLite schema. The Python application also creates this table automatically.

CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL,
    email TEXT UNIQUE
);
