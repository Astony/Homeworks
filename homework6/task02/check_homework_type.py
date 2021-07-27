from typing import ClassVar, Type


class InvalidError(Exception):
    """This is my personal error for check_homework_type method"""


def check_homework_type(some_obj: ClassVar, homework_class: Type) -> "Homework":
    if isinstance(some_obj, homework_class):
        return some_obj
    else:
        raise InvalidError("Argument should has Homeworks class type")
