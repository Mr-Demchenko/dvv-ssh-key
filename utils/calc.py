def add(x:int, y:int):
    return x+y


def subtract(x:int, y:int):
    return x - y


def multiply(x:int, y:int):
    return x*y


def divide(x:int, y:int):
    if y == 0:
        raise ZeroDivisionError('Деление на 0 запрещено')
    return x/y
