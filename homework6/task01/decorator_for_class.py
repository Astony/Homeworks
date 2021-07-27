from typing import Type


def instance_counter_decorator(cls: Type) -> Type:
    """Decorator that adds additional methods for decorated class"""
    cls.created_instances_counter = 0

    def __new__(self):
        instance = super(cls, cls).__new__(cls)
        cls.created_instances_counter += 1
        return instance

    @classmethod
    def get_instances_count(cls: Type) -> int:
        return cls.created_instances_counter

    @classmethod
    def clear_instances_count(cls: Type) -> None:
        cls.created_instances_counter = 0

    cls.__new__ = __new__
    cls.get_instances_count = get_instances_count
    cls.clear_instances_count = clear_instances_count
    return cls
