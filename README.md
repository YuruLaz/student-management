# Student Management System

Console app for the IT-Step backend midterm. Demonstrates OOP principles
(inheritance, encapsulation, polymorphism) through a simple menu-driven
system for managing students.

## Structure

- `models.py` — `Person` (abstract base class) and `Student(Person)`.
  Validated letter grade (A-F), encapsulated attributes via properties.
- `manager.py` — `StudentManager`, holds the list of students and handles
  add/view/find/update/delete operations.
- `main.py` — the menu loop (entry point).
- `storage.py` — saves/loads students to `data/students.txt` so data
  survives between runs.

## Running it

```
python main.py
```

Menu options: add a student, view all students, find a student by roll
number, update a student's grade, delete a student, or exit.

## Notes

- Grade is a single letter: A, B, C, D, or F.
- Roll numbers must be unique whole numbers; adding a duplicate is rejected.
- Student data is saved automatically after every add/update/delete.
