from functools import reduce


def is_armstrong(number: int) -> bool:
    digits_pow = [pow(int(i), len(str(number))) for i in str(number)]
    return reduce(lambda res, x: res + x, digits_pow) == number
