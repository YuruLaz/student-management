"""Entry point for the student management system.

Runs a menu-driven console loop that lets the user add students,
view them all, find one by roll number, and update a grade.
"""

from models import Student, InvalidGradeError
from manager import StudentManager
from storage import load_students, save_students


MENU = """
1. Add new student
2. View all students
3. Find student by roll number
4. Update student grade
5. Delete student
6. Exit
"""


def prompt_int(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a whole number.")


def prompt_name(prompt):
    """Keep asking until the user types a non-empty name."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Name can't be empty.")


def add_student(manager):
    """Ask for name/roll number/grade and add a new student."""
    name = prompt_name("Name: ")
    roll_number = prompt_int("Roll number: ")
    grade = input("Grade (A-F): ")

    try:
        student = Student(name, roll_number, grade)
    except InvalidGradeError:
        print(f"'{grade}' is not a valid grade (must be A, B, C, D, or F).")
        return

    if not manager.add_student(student):
        print(f"A student with roll number {roll_number} already exists.")
        return

    save_students(manager.students)
    print("Student added.")


def find_student(manager):
    """Ask for a roll number and show that student's info if found."""
    roll_number = prompt_int("Roll number to find: ")
    student = manager.find_by_roll(roll_number)

    if student is None:
        print("No student with that roll number.")
        return

    student.display_info()


def update_grade(manager):
    """Ask for a roll number and a new grade, then apply the update."""
    roll_number = prompt_int("Roll number to update: ")
    new_grade = input("New grade (A-F): ")

    try:
        updated = manager.update_grade(roll_number, new_grade)
    except InvalidGradeError:
        print(f"'{new_grade}' is not a valid grade (must be A, B, C, D, or F).")
        return

    if updated:
        save_students(manager.students)
        print("Grade updated.")
    else:
        print("No student with that roll number.")


def delete_student(manager):
    """Ask for a roll number and delete that student."""
    roll_number = prompt_int("Roll number to delete: ")
    deleted = manager.delete_student(roll_number)

    if deleted:
        save_students(manager.students)
        print("Student deleted.")
    else:
        print("No student with that roll number.")


def main():
    """Run the menu loop until the user chooses to exit."""
    manager = StudentManager()
    for student in load_students():
        manager.add_student(student)

    while True:
        print(MENU)
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(manager)
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            find_student(manager)
        elif choice == "4":
            update_grade(manager)
        elif choice == "5":
            delete_student(manager)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Not a valid option, try again.")


if __name__ == "__main__":
    main()
