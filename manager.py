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
        """Read-only access to the list of students."""
        return self._students

    def add_student(self, student: Student):
        """Add a Student object to the list.

        Returns True if added, False if a student with that roll
        number already exists (roll numbers must be unique).
        """
        if self.find_by_roll(student.roll_number) is not None:
            return False

        self._students.append(student)
        return True

    def view_all(self):
        """Print details of every student, or a message if there are none."""
        if not self._students:
            print("No students yet.")
            return

        for student in self._students:
            student.display_info()
            print("-" * 20)

    def find_by_roll(self, roll_number):
        """Return the Student with this roll number, or None if not found."""
        for student in self._students:
            if student.roll_number == roll_number:
                return student

        return None

    def update_grade(self, roll_number, new_grade):
        """Find a student by roll number and update their grade.

        Returns True if a student was found and updated, False if no
        student with that roll number exists. Raises InvalidGradeError
        (via the grade setter) if new_grade isn't a valid letter.
        """
        student = self.find_by_roll(roll_number)
        if student is None:
            return False

        student.grade = new_grade
        return True

    def delete_student(self, roll_number):
        """Remove the student with this roll number.

        Returns True if a student was found and removed, False if no
        student with that roll number exists.
        """
        student = self.find_by_roll(roll_number)
        if student is None:
            return False

        self._students.remove(student)
        return True
