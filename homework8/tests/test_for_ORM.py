import os
import sqlite3

import pytest

from homework8.task02.DataBaseClass import TableData


def test_of_len_method(create_db):
    """Check len of TableData's instance"""
    with TableData(create_db, "presidents") as presidents:
        assert len(presidents) == 3


def test_get_item_method(create_db):
    """Check the method of getting item from db in case when item exists"""
    with TableData(create_db, "presidents") as presidents:
        assert presidents["Obama"] == ("Obama", "America", 2)


def test_contains_method(create_db):
    """Check contain method"""
    with TableData(create_db, "presidents") as presidents:
        assert "Putin" in presidents
        assert not "West" in presidents


def test_iteration_method(create_db):
    """Check that iteration protocol is working via list comprehension"""
    with TableData(create_db, "presidents") as presidents:
        presidents_name_list = [president["name"] for president in presidents]
        assert presidents_name_list == ["Trump", "Obama", "Putin"]


def test_not_existing_db():
    """Check if db doesn't exists in a directory it will caused Error instead of creating new db"""
    with pytest.raises(IOError, match=f"No such db"):
        with TableData("abacaba", "president") as presidents:
            print("hello")


def test_wrong_arguments(create_db):
    """Check that it will be an error then we input wrong argument"""
    with TableData(create_db, "presidents") as presidents:
        assert presidents["Murphy"] == []
