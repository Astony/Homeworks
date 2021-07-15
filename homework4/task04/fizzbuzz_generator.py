from typing import Generator

"""Generator of FizzBuzz numbers"""


def fizzbuzz(len_out_sequence: int) -> Generator[int]:
    """Test of fizzbuzz
        Test, that our function generate right sequence:
    >>> list(fizzbuzz(6))
    [1, 2, 'Fizz', 4, 'Buzz']

    Test case when the number is divisible by three and five:
    >>> list(fizzbuzz(20))[14]
    'FizzBuzz'
    """
    for number in range(1, len_out_sequence):
        fizzbuzz_numb = (
            "Fizz" * (not number % 3) + "Buzz" * (not number % 5)
        ) or number
        yield fizzbuzz_numb
