from typing import Sequence

"""Generator of fibonacci numbers step by step"""


def fib_generator():
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


"""Compare numbers from input sequence with numbers
which created by generator"""


def check_fibonacci(inp_seq: Sequence[int]) -> bool:
    if len(inp_seq) > 0:
        gen = fib_generator()
        for element in inp_seq:
            if element != next(gen):
                return False
        return True
    return False
