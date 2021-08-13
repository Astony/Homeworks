from homework11.task01.simple_enum import SimpleEnum


def test_positive_case1():
    """Test that simple enum class that was created with SimpleEnum metaclass has attributes which was tupled"""

    class ColorsEnum(metaclass=SimpleEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert all(
        element in ColorsEnum.__dict__.keys()
        for element in ("RED", "BLUE", "ORANGE", "BLACK")
    )
