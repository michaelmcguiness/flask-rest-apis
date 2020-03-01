t = 5, 11  # don't always need parentheses for tuples
x, y = t
print(x, y)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
print(list(student_attendance.items()))
for student, attendance in student_attendance.items():
    print(f"{student} : {attendance}")

people = [("Bob", 42, "Mechanic"), ("James", 24,
                                    "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person = ("Bob", 42, "Mechanic")
name, _, profession = person  # _ for ignoring variables
print(name, profession)

head, *tail = [1, 2, 3, 4, 5]
print(head)  # 1
print(tail)  # [2, 3, 4, 5]

*head, tail = [1, 2, 3, 4, 5]
print(head)  # [1, 2, 3, 4]
print(tail)  # 5
