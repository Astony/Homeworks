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
def create_file_with_text(text: str):
    with open(file, "w+") as test_file:
        test_file.write(text)
    yield file
    os.remove(file)


@pytest.fixture
def create_db():
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
    yield "example.db"
    os.remove("example.db")
