import os
import sqlite3


def open_close_conn(method):
    """Decorator that opens and closes connection"""

    def wrapper(self, *args):
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            result = method(self, cursor, *args)
            return result
        except Exception as err:
            print(f"Something has gone wrong. It has caused the {err}")
        finally:
            conn.commit()
            conn.close()

    return wrapper


class TableData:
    """
    Class allows to get a length of db, get some element from db
         and also it has method to add some element to db
    """

    def __init__(self, database, table):
        if not os.path.exists(database):
            raise IOError("No such db")
        self.database = database
        self.table = table
        self.iteration_step = 1

    @open_close_conn
    def len_of_database(self, cursor):
        cursor.execute(f"""SELECT COUNT(name) FROM {self.table}""")
        return cursor.fetchone()[0]

    @open_close_conn
    def search_element(self, cursor, name):
        cursor.execute(f"""SELECT * FROM {self.table} WHERE name='{name}'""")
        result = cursor.fetchone()
        if not result:
            raise ValueError("'There is no such element in db'")
        return result

    @open_close_conn
    def search_element_while_iterating(self, cursor):
        cur = cursor.execute(
            f"""SELECT * FROM {self.table} 
        WHERE id = {self.iteration_step}"""
        )
        item = cur.fetchone()
        self.iteration_step += 1
        return {"name": item[0], "country": item[1]}

    @open_close_conn
    def additem(self, cursor, item):
        cursor.executemany(f"INSERT INTO {self.table} VALUES (?, ?, ?)", item)

    def __len__(self):
        return self.len_of_database()

    def __getitem__(self, item):
        return self.search_element(item)

    def __iter__(self):
        return self

    def __next__(self):
        length = self.len_of_database()
        while self.iteration_step <= length:
            return self.search_element_while_iterating()
        self.iteration_step = 0
        raise StopIteration

    def __contains__(self, item):
        try:
            return bool(self.search_element(item))
        except ValueError:
            return False
