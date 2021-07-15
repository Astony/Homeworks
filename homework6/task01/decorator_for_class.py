from typing import Any, Type


def instance_counter_decorator(orig_class: Type) -> Type:
    class InstanceCounterClass:
        """
        Decorator that contains two additional methods
        for count number of objects of original class and reset that counter
        """

        count = 0

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            self.original_class = orig_class(*args, **kwargs)
            InstanceCounterClass.count += 1

        def get_instances_count(self) -> int:
            return InstanceCounterClass.count

        def clear_instances_count(self) -> None:
            InstanceCounterClass.count = 0

        def __getattr__(self, attribute: Any) -> Any:
            return getattr(self.original_class, attribute)

    return InstanceCounterClass
