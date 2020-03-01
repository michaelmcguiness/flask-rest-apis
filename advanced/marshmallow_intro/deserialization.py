from marshmallow import Schema, fields


class BookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    description = fields.Str()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


incoming_book_data = {
    "title": "Clean Code",
    "author": "Bob Martin",
}

book_schema = BookSchema()
book = book_schema.load(incoming_book_data)
book_obj = Book(**book)

print(book)
# {'title': 'Clean Code', 'author': 'Bob Martin', 'description': 'A book about writing cleaner code.'}

print(book_obj)  # <__main__.Book object at 0x104c30e50>
