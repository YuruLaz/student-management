from abc import ABC, abstractmethod


class InvalidGradeError(ValueError):
    """Raise if grade is out of range"""


class Person(ABC):
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

    @staticmethod
    def validate_grade(grade):
        if not isinstance(grade, int) or not 0 <= grade <= 100:
            raise InvalidGradeError(grade)

        return grade


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
        return isinstance(other, Student) and self._grade < other._grade

    def __eq__(self, other):
        return isinstance(other, Student) and self._roll_number == other._roll_number

    def __hash__(self):
        return hash(self._roll_number)

