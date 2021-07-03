"""Generator of FizzBuzz numbers"""


def fizzbuzz(lenfizzbuzzlist):
    """Test of fizzbuzz
    >>> list(fizzbuzz(16))
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    """
    for number in range(1, lenfizzbuzzlist):
        fizzbuzznumb = ("Fizz" * (not number % 3) + "Buzz" * (not number % 5)) or number
        yield fizzbuzznumb
