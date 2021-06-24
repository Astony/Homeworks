from typing import Sequence


def fib_generator():
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1+fib2


def check_fibonacci(inp_seq):
    gen = fib_generator()
    for element in inp_seq:
        if element != next(gen):
            return False
    return True
