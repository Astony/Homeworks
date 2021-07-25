from typing import Generator

"""Generator of FizzBuzz numbers"""


def fizzbuzz(len_out_sequence: int) -> Generator[int, str, None]:
    """Test of fizzbuzz
        Test, that our function generate right sequence:
    >>> list(fizzbuzz(5))
    [1, 2, 'Fizz', 4, 'Buzz']

    Test case when the number is divisible by three and five:
    >>> list(fizzbuzz(20))[14]
    'FizzBuzz'

    Test with wrong attribute
    """
    try:
        for number in range(1, len_out_sequence + 1):
            fizzbuzz_numb = (
                "Fizz" * (not number % 3) + "Buzz" * (not number % 5)
            ) or number
            yield fizzbuzz_numb
    except TypeError:
        print("Wrong input argument")
