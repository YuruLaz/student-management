"""Storage module for the student management system.

Has functions to save students to a text file and load them back,
so student data survives between runs of the program.
"""

import os

from models import Student, InvalidGradeError

DEFAULT_FILE = "data/students.txt"


def save_students(students, filepath=DEFAULT_FILE):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w") as file:
        for student in students:
            file.write(f"{student.name},{student.roll_number},{student.grade}\n")


def load_students(filepath=DEFAULT_FILE):
    """Read students from filepath, skip bad lines, return [] if missing."""
    students = []

    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                name, roll_number, grade = line.split(",")

                try:
                    students.append(Student(name, int(roll_number), grade))
                except InvalidGradeError:
                    continue

    except FileNotFoundError:
        return []

    return students
