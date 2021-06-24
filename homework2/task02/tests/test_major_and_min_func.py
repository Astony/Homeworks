from homework2.task02.major_and_min_func import major_and_minor_elem


def test_of_positive_case():
    assert major_and_minor_elem([1, 1, 1, 1, 1, 5, 6]) == (1, 5)
    assert major_and_minor_elem([1, 1, 1, 1, 1, 5, 5]) == (1, 5)
