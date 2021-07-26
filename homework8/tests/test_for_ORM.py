import os
import sqlite3

import pytest

from homework8.task02.DataBaseClass import TableData


def test_of_len_method(presidents):
    """Check len of TableData's instance"""
    assert len(presidents) == 3


def test_get_item_method(presidents):
    """Check the method of getting item from db in case when item exists"""
    assert presidents["Obama"] == ("Obama", "America", 2)


def test_contains_method(presidents):
    """Check contain method"""
    assert "Putin" in presidents
    assert not "West" in presidents


def test_iteration_method(presidents):
    """Check that iteration protocol is working via list comprehension"""
    presidents_name_list = [president["name"] for president in presidents]
    assert presidents_name_list == ["Trump", "Obama", "Putin"]


def test_update_data(presidents):
    """Check that after case when db has changed, all changes are available permanently"""
    presidents.additem([("Savrushkin", "Russia", 4)])
    assert presidents["Savrushkin"] == ("Savrushkin", "Russia", 4)


def test_not_existing_db():
    """Check if db doesn't exists in a directory it will caused Error instead of creating new db"""
    with pytest.raises(IOError, match=f"No such db"):
        presidents = TableData("wrongPath", "presidents")


def test_wrong_arguments(presidents, capsys):
    """Check that it will be an error then we input wrong argument"""
    presidents["abacaba"]
    assert capsys.readouterr().out.startswith("Something has gone wrong.")
