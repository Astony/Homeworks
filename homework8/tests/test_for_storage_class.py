import pytest

from homework8.task01.KeyValueStorage_class import KeyValueStorage


@pytest.mark.parametrize("text", ["name=kek\nlast_name=2"])
def test_with_valid_attrs_and_vals(create_file_with_text):
    """Check that attributes of instances behave as collection's items and as attributes"""
    test_class = KeyValueStorage(create_file_with_text)
    assert test_class.name == "kek"
    assert test_class["last_name"] == 2


@pytest.mark.parametrize("text", ["name=kek\nlast_name=2"])
def test_with_nonexisting_attr(create_file_with_text):
    """Check that ValueError would be raise in case with non existing attribute"""
    test_class = KeyValueStorage(create_file_with_text)
    with pytest.raises(ValueError, match="No such key"):
        test_class["wrong_attribute"]


@pytest.mark.parametrize("text", ["__class__=boo"])
def test_case_with_attribute_clash(create_file_with_text):
    """Check that in case of attribute clash existing built-in attributes take precedence"""
    test_class = KeyValueStorage(create_file_with_text)
    assert (
        str(test_class["__class__"])
        == "<class 'homework8.task01.KeyValueStorage_class.KeyValueStorage'>"
    )
