import pytest

from homework3.task03.filter_func import Filter, make_filter

data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

"""
We check 2 cases when the desired combination
 is in the list and one case when the required
  combination does not exist 
"""


@pytest.mark.parametrize(
    "result, test_input",
    [
        ([data[0]], {"name": "Bill"}),
        ([data[1]], {"kind": "parrot"}),
        ([], {"name": "Bill", "kind": "parrot"}),
    ],
)
def test_filter(result, test_input):
    assert make_filter(**test_input).apply(data) == result


def test_of_invalid_input():
    with pytest.raises(TypeError):
        make_filter('name').apply(data)
        print("Invalid input data")