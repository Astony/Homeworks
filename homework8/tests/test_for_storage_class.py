import pytest

from homework8.task01.KeyValueStorage_class import KeyValueStorage


def test_with_valid_attrs_and_vals(create_file_with_valid_attr_val):
    """Check that attributes of instances behave as collection's items and as attributes"""
    test_class = KeyValueStorage(create_file_with_valid_attr_val)
    assert test_class.name == "kek"
    assert test_class["last_name"] == 2


def test_with_invalid_attribute_in_file(create_file_with_invalid_attr_val):
    """Check that invalid name for an attribute in a txt file raises ValueError"""
    with pytest.raises(ValueError, match="Invalid name for attribute"):
        test_class = KeyValueStorage(create_file_with_invalid_attr_val)


def test_case_with_attribute_clash(create_file_with_clash_attr):
    """Check that in case of attribute clash existing built-in attributes take precedence"""
    test_class = KeyValueStorage(create_file_with_clash_attr)
    assert (
        str(test_class["__class__"])
        == "<class 'homework8.task01.KeyValueStorage_class.KeyValueStorage'>"
    )
