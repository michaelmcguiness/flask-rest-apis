from typing import List


class Student:
    # don't use mutable default values for parameters
    # def __init__(self, name: str, grades: List[int] = []):  # this is bad!
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)  # [90]
print(rolf.grades)  # [90]
