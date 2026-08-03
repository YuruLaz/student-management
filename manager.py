"""Manager module for the student management system.

Has the StudentManager class, which keeps a list of Student objects
and lets you add, view, search, and update them.
"""

from models import Student


class StudentManager:
    """Keeps a list of students and manages operations on them."""

    def __init__(self):
        self._students: list[Student] = []

    @property
    def students(self):
        return list(self._students)

    def add_student(self, student: Student):
        """Add student if roll number is unique, return False otherwise."""
        if student in self._students:
            return False

        self._students.append(student)
        return True

    def view_all(self):
        if not self._students:
            print("No students yet")
            return

        for student in self._students:
            student.display_info()
            print("-" * 20)

    def find_by_roll(self, roll_number):
        for student in self._students:
            if student.roll_number == roll_number:
                return student

        return None

    def update_grade(self, roll_number, new_grade):
        student = self.find_by_roll(roll_number)
        if student is None:
            return False

        student.grade = new_grade
        return True

    def delete_student(self, roll_number):
        student = self.find_by_roll(roll_number)
        if student is None:
            return False

        self._students.remove(student)
        return True
