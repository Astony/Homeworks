def instance_counter_decorator(orig_class):
    class InstanceCounterClass:
        """
        Decorator that contains two additional methods
        for count number of objects of original class and reset that counter
        """

        count = 0

        def __init__(self, *args, **kwargs):
            self.original_class = orig_class(*args, **kwargs)
            InstanceCounterClass.count += 1

        def get_instances_count(self):
            return InstanceCounterClass.count

        def clear_instances_count(self):
            InstanceCounterClass.count = 0

        def __getattr__(self, attribute):
            if attribute not in dir(self.original_class) and super().__getattribute__(
                attribute
            ):
                raise AttributeError("There is not the attribute with such name")
            return self.original_class.__getattribute__(attribute)

    return InstanceCounterClass
