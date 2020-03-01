# add = lambda x, y: x + y
def add(x, y): return x + y


print(add(5, 7))


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
print(doubled)  # [2, 6, 10, 18]
doubled = list(map(double, sequence))
print(doubled)  # [2, 6, 10, 18]
doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)  # [2, 6, 10, 18]
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)  # [2, 6, 10, 18]
