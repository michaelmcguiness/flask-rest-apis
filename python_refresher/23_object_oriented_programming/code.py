# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


# def average(sequence):
#     return sum(sequence) / len(sequence)


# print(average(student["grades"]))

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Rolf", (89, 90, 93, 78, 90))
print(student.name)  # Rolf

# both below do exactly the same thing
print(Student.average(student))
print(student.average())
