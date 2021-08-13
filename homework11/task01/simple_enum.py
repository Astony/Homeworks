from typing import ClassVar, Dict, Tuple


class SimpleEnum(type):
    """Metaclass for creating simple enum classes"""

    def __new__(cls, name: str, bases: Tuple, namespace: Dict) -> ClassVar:
        new_namespace = {value: value for value in tuple(namespace.values())[-1]}
        return super().__new__(cls, name, bases, new_namespace)
