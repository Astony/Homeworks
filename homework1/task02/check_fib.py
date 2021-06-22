from math import sqrt
from typing import Sequence


def check_fibonacci(x: Sequence[int]) -> bool:
    if len(x) != 0:
        if sqrt(5 * (x[0] ** 2) - 4) % 1 == 0 or sqrt(5 * (x[0] ** 2) + 4) % 1 == 0:
            fib1 = fib2 = 1
            while fib2 != x[0]:
                fib = fib1 + fib2
                fib1 = fib2
                fib2 = fib
            for i in range(len(x)):
                if x[i] == 1 and x[i] == x[i + 1]:
                    continue
                elif x[i] == fib2:
                    fib = fib1 + fib2
                    fib1 = fib2
                    fib2 = fib
                else:
                    return False
            return True
        else:
            return False
    else:
        return False
