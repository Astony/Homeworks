import os
import sqlite3

import pytest

from homework8.task02.DataBaseClass import TableData


@pytest.fixture
def presidents():
    conn = sqlite3.connect("example.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE presidents (name, country)""")
    presidents = [("Trump", "America"), ("Obama", "America"), ("Putin", "Russia")]
    cur.executemany("INSERT INTO presidents VALUES (?, ?)", presidents)
    conn.commit()
    conn.close()
    president = TableData("example.db", "presidents")
    yield president
    president = None
    os.remove("example.db")


def test_of_len_method(presidents):
    assert len(presidents) == 3


def test_get_item_method(presidents):
    assert presidents["Obama"] == ("Obama", "America")


def test_contains_method(presidents):
    assert "Putin" in presidents


def test_iteration_method(presidents):
    presidents_name_list = [president["name"] for president in presidents]
    assert presidents_name_list == ["Trump", "Obama", "Putin"]


def test_update_data(presidents):
    presidents.additem([("Savrushkin", "Russia")])
    assert presidents["Savrushkin"] == ("Savrushkin", "Russia")
