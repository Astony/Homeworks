import pytest

from homework9.task02.suppressor_class import Suppressor
from homework9.task02.suppressor_gen import suppressor_gen


def test_positive_cases():
    """Test suppressor funcs in case with matching errors"""
    with Suppressor(IndexError):
        assert [][2]
    with suppressor_gen(IndexError):
        assert [][2]


def test_negative_cases():
    """Test suppressor funcs in case with unmatching errors"""
    with pytest.raises(IndexError):
        with Suppressor(ValueError):
            [][2]
    with pytest.raises(IndexError):
        with suppressor_gen(ValueError):
            [][2]
