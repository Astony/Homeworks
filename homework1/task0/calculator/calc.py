"""bit logical multiplication to check if power the number is 2"""


def check_power_of_2(number: int) -> bool:
    return not (bool(number & (number - 1))) and number != 0
