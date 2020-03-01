# str and repr are sometimes called "Magic Methods" bc they're called automatically
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    # goal of repr method is to be unambiguous
    # should return a string that allows us to recreate the
    # object very easily. (used in python debugger)
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"


bob = Person("Bob", 35)
print(bob)
