import pytest

from homework4.task04.fizzbuzz_generator import fizzbuzz


def test_positive_case():
    """Check the generator gives right sequence"""
    assert list(fizzbuzz(5)) == [1, 2, "Fizz", 4, "Buzz"]


def test_number_that_divides_5_and_3():
    """Check that if number divides on 5 and 3 generator's output is 'fizzbuzz'"""
    assert list(fizzbuzz(20))[14] == "FizzBuzz"


def exception_case_with_wrong_input_attribute(capsys):
    """Check that in case with wrong input attributes function raise TypeError"""
    fizzbuzz("a")
    assert capsys.readouterr().out == "Wrong input argument"
