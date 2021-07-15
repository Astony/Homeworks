from typing import ClassVar, Type


def check_homework_type(some_obj: ClassVar, homework_class: Type) -> bool:
    if isinstance(some_obj, homework_class):
        return True
    else:
        raise AttributeError("Argument should has Homeworks class type")
