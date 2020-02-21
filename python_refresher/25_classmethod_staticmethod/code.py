class ClassTest:
    def instance_method(self):
        # used for most things (actions that use data inside object)
        # also used for modifying data inside self
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        # used as factories
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        # used to place a method inside a class
        print("Called static_method")


test = ClassTest()
test.instance_method()
# Called instance_method of <__main__.ClassTest object at 0x104c71fa0>

ClassTest.class_method()
# Called class_method of <class '__main__.ClassTest'>

ClassTest.static_method()
# Called static_method


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)


print(Book.TYPES)  # ('hardcover', 'paperback')

book = Book("Harry Potter", "hardcover", 1500)
print(book.name)  # Harry Potter
print(book)  # <Book Harry Potter, hardcover, weighing 1500g>

heavy = Book.hardcover("Harry Potter", 1500)
# <Book Harry Potter, hardcover, weighing 1600g>

light = Book.paperback("Python 101", 600)
# <Book Harry Potter, hardcover, weighing 1600g>

print(heavy)
print(light)
