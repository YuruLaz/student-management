"""Storage module for the student management system.

Has functions to save students to a text file and load them back,
so student data survives between runs of the program.
"""

import csv
import os

from models import Student, InvalidGradeError

DEFAULT_FILE = "data/students.txt"


def save_students(students, filepath=DEFAULT_FILE):
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for student in students:
            writer.writerow([student.name, student.roll_number, student.grade])


def load_students(filepath=DEFAULT_FILE):
    """Read students from filepath, skip bad rows, return [] if missing."""
    students = []

    try:
        with open(filepath, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue

                try:
                    name, roll_number, grade = row
                    students.append(Student(name, int(roll_number), grade))
                except (ValueError, InvalidGradeError):
                    print(f"Skipping bad row in {filepath}: {row}")
                    continue

    except FileNotFoundError:
        return []

    return students
