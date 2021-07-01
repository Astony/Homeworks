from functools import reduce

"""
Transform the input number into list of chars and then we raise
 each digit to a power equal to their number and find the sum
 """


def is_armstrong_number(number: int) -> bool:
    digits_pow = [pow(int(i), len(str(number))) for i in str(number)]
    return sum(digits_pow) == number
