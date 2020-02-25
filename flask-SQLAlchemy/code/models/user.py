import sqlite3

# this class is a helper that we use to store some data of the user
# and has methods that allow us to easily retrieve user objects from database
# a model is an internal representation of an entity
# whereas a resource is an external representation of an entity
# models give us more functionality without polluting the resource


class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        # parameters always have to be in form of a tuple
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            # using cls is better than hardcoding "User" classname
            user = cls(*row)
            # pass row as set of positional arguments instead of cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
