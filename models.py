"""Models for the student management system.

Has the Person base class, the Student class, and the error
raised when someone tries to set a bad grade.
"""

from abc import ABC, abstractmethod


class InvalidGradeError(ValueError):
    """Raise if grade is out of range"""


GRADE_ORDER = "FDCBA"


class Person(ABC):
    """Base class for a person, has a name and a roll number."""

    def __init__(self, name, number):
        self._name: str = name
        self._roll_number: int = number

    @abstractmethod
    def display_info(self):
        print(f"name: {self._name}")
        print(f"ID_number: {self._roll_number}")

    @property
    def roll_number(self):
        return self._roll_number

    @property
    def name(self):
        return self._name


class Student(Person):
    """A Person with a letter grade (A-F), inherits name and roll number."""

    @staticmethod
    def validate_grade(grade):
        if not isinstance(grade, str) or len(grade) != 1 or grade.upper() not in GRADE_ORDER:
            raise InvalidGradeError(grade)

        return grade.upper()

    @staticmethod
    def grade_rank(letter):
        return GRADE_ORDER.index(letter)

    def __init__(self, name, number, grade):
        super().__init__(name, number)
        self._grade = self.validate_grade(grade)
        

    def display_info(self):
        super().display_info()
        print(f"Student grade: {self._grade}")

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        self._grade = self.validate_grade(new_grade)



    def __str__(self):
        return f"{self._name} (#{self._roll_number}) - grade: {self._grade}"

    def __repr__(self):
        return f"Student(name={self._name!r}, number={self._roll_number!r}, grade={self._grade!r})"

    def __lt__(self, other):
        return isinstance(other, Student) and (
            self.grade_rank(self._grade) < self.grade_rank(other._grade)
        )

    def __eq__(self, other):
        return isinstance(other, Student) and self._roll_number == other._roll_number

    def __hash__(self):
        return hash(self._roll_number)

