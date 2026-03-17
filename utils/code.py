import math

def up_fist(msg):
    """First letter is up"""
    if msg:
        return msg[0].upper() + msg[1:]
    else:
        return msg


def calculate_logarithm(number):
    if number <= 0:
        raise ValueError("Логарифм можно вычислить только для положительных чисел")
    return math.log(number)