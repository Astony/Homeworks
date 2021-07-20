import pytest

from homework7.task01.find_occurrences import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

over_multiply_struct = {1: (2, 3, [4, 5, [6, 7, {8: {9: "RED"}}]])}

wrong_input_value = 13

empty_structure = ()


@pytest.mark.parametrize(
    "structure, result",
    [
        (example_tree, 6),
        (over_multiply_struct, 1),
        (wrong_input_value, 0),
        (empty_structure, 0),
    ],
)
def test_positive_case(structure, result):
    """Check various cases of input structure"""
    assert find_occurrences(structure, "RED") == result
