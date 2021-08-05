import pytest

from homework6.task01.decorator_for_class import instance_counter_decorator


@instance_counter_decorator
class TestClass1:
    attribute1 = 1

    def foo(self):
        return True


@instance_counter_decorator
class TestClass2:
    attribute2 = 2

    def boo(self):
        return True


foo_class1 = TestClass1()
foo_class2 = TestClass1()
boo_class1 = TestClass2()


def test_count_instances_method():
    """
    Check that objects of the same class have equal counter's value
    before and after using reset method and also
    that object of another class has different counter
    """
    assert foo_class2.get_instances_count() == foo_class1.get_instances_count() == 2


def test_clear_instances_method():
    assert foo_class2.clear_instances_count() == 2
    assert foo_class2.get_instances_count() == foo_class1.get_instances_count() == 0
    assert boo_class1.get_instances_count() == 1


def test_non_existing_attribute():
    """
    Check that if we try to call methods or attributes that define neither in original class
    nor in decorator class we get AttributeError
    """
    with pytest.raises(AttributeError):
        foo_class2.non_existing_method()
        foo_class2.non_existing_attribute


def test_attribute_of_original_class():
    """Check that methods and attributes of original class work correct"""
    assert foo_class2.foo()
    assert foo_class2.attribute1 == 1
