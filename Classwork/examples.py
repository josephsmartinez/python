import unittest

def addition(x, y):
    return x + y


def multiplication(x, y):
    return x * y


def subtraction(x, y):
    return x - y


def division(x, y):
    if y != 0:
        return x / y
    else:
        print("Cannot divide by zero")


def factorial(x):
    if x > 0:
        return x * factorial(x - 1)
    else:
        return 1


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range (2, x):
        if (x % i) == 0:
            return False
    return True


def EuclideanDistance(point1, point2):
    a = point2[0] - point1[0]
    b = point2[1] - point1[1]

    a *= a
    b *= b

    c = (a + b) ** (1/2)

    return c


class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 20 + self.ability_scores["con"]


