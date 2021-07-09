from homework5.task02.default_func import custom_sum_default, print_result_default
from homework5.task02.func_with_class_decorator import Saver, custom_sum, print_result


def test_without_Saver():
    """
    Test for case without class-decorator. Attributes of wrapped function
    have attributes of wrapper function
    """
    assert (
        custom_sum_default.__doc__
        == "Function-wrapper which print result of an original function"
    )
    assert custom_sum_default.__name__ == "wrapper"


def test_with_Saver():
    """
    Test for case with class-decorator. Attributes of wrapped function
    have attributes of original function
    """
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"
    assert str(custom_sum.original_func)[1:20] == "function custom_sum"
