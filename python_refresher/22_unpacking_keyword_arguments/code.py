# "**" collects keyword arguments
def named(**kwargs):
    print(kwargs)


named(name="bob", age=25)
# {'name': 'bob', 'age': 25}


def named2(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}
named(**details)
# {'name': 'Bob', 'age': 25}


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)
# (1, 3, 5)
# {'name': 'Bob', 'age': 25}

"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""
