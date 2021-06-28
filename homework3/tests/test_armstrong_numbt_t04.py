from homework3.task04.armstrong_number import is_armstrong


def test_armstrong_numb():
    assert is_armstrong(153)
    assert is_armstrong(9)
    assert not is_armstrong(27)
