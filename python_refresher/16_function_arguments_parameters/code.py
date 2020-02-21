def add(x, y):
    result = x + y
    print(result)


add(5, 3)


# Positional arguments (position affects value of relevant parameter)
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")


say_hello(surname="Smith", name="Bob")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")


# use keyword arguments to make your code more readable
divide(dividend=15, divisor=0)
