import os
import sqlite3

import pytest

from homework8.task02.DataBaseClass import TableData

file = "test_file.txt"


"""
All fixtures create file, write some rows inside, 
  send file in tests func and then delete file
"""


@pytest.fixture()
def create_file_with_valid_attr_val():
    with open(file, "w+") as test_file:
        test_file.write("name=kek\nlast_name=2")
    yield file
    os.remove(file)


@pytest.fixture()
def create_file_with_invalid_attr_val():
    with open(file, "w+") as test_file:
        test_file.write("1=invalid_attribute")
    yield file
    os.remove(file)


@pytest.fixture()
def create_file_with_clash_attr():
    with open(file, "w+") as test_file:
        test_file.write("__class__=boo")
    yield file
    os.remove(file)


@pytest.fixture
def presidents():
    conn = sqlite3.connect("example.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE presidents (name, country, id)""")
    presidents = [
        ("Trump", "America", 1),
        ("Obama", "America", 2),
        ("Putin", "Russia", 3),
    ]
    cur.executemany("INSERT INTO presidents VALUES (?, ?, ?)", presidents)
    conn.commit()
    conn.close()
    president = TableData("example.db", "presidents")
    yield president
    president = None
    os.remove("example.db")
