from homework5.task02.decorated_func import (
    custom_sum,
    print_result,
    save_orig_func_info,
)
from homework5.task02.default_func import custom_sum_def, print_result_def


def test_without_Saver():
    """
    Test for case without class-decorator. Attributes of wrapped function
    have attributes of wrapper function
    """
    assert (
        custom_sum_def.__doc__
        == "Function-wrapper which print result of an original function"
    )
    assert custom_sum_def.__name__ == "wrapper"


def test_with_Saver():
    """
    Test for case with class-decorator. Attributes of wrapped function
    have attributes of original function
    """
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"
    assert "orig_func" in custom_sum.__dict__
