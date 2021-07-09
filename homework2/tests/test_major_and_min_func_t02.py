import pytest

from homework2.task02.major_and_min_func import major_and_minor_elem


def test_of_positive_case():
    """Test simple case"""
    assert major_and_minor_elem([1, 1, 1, 1, 1, 5, 5]) == (1, 5)


def test_negative_case():
    """How it was write in annotation, when input list contains several rarest number,
    we should take smallest from them"""
    assert not major_and_minor_elem([1, 1, 1, 1, 1, 5, 6, 7]) == (1, 7)
    assert major_and_minor_elem([1, 1, 1, 1, 1, 5, 6, 7]) == (1, 5)


def test_of_equal_numbers_case():
    """Test for case of equal numbers in input list"""
    assert major_and_minor_elem([1, 1, 1, 1, 1]) == (1, 1)


def test_of_different_type_of_list_elem():
    """Test of case, when list contains elements of different types"""
    with pytest.raises(TypeError):
        major_and_minor_elem([1, 2, 3, (1,)])
