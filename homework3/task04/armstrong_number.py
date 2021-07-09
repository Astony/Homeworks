"""
Transform the input number into list of chars and then we raise
 each digit to a power equal to their number and find the sum
 """


def is_armstrong_number(number: int) -> bool:
    if number > 0:
        digits_pow = [pow(int(i), len(str(number))) for i in str(number)]
        return sum(digits_pow) == number
    else:
        list_of_numbs = ["-" + i for i in str(number)[1:]]
        digits_pow = [pow(int(i), len(list_of_numbs)) for i in list_of_numbs]
        return sum(digits_pow) == number
