import os
import sqlite3


class TableData:
    """
    Class allows to get a length of db, get some element from db
         and also it has method to add some element to db
    """

    @staticmethod
    def validating_db(database: str) -> str:
        if os.path.exists(database):
            return database
        raise IOError("No such db")

    @staticmethod
    def validating_table(table: str) -> str:
        if len(table) < 15 and " " not in table and table.isidentifier():
            return table
        raise ValueError("Invalid tables name")

    def __init__(self, database, table):
        self.database = TableData.validating_db(database)
        self.table = TableData.validating_table(table)
        self.iteration_step = 1

    def __enter__(self):
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, *args, **kwargs):
        self.conn.close()

    def __len__(self):
        self.cursor.execute(f"""SELECT COUNT(name) FROM {self.table}""")
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        self.cursor.execute(f"""SELECT * FROM {self.table} WHERE name='%s';""" % item)
        result = self.cursor.fetchone()
        return result if result else []

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor.execute(
            f"""SELECT * FROM {self.table} limit {self.iteration_step} - 1, {self.iteration_step}"""
        )
        item = self.cursor.fetchone()
        if item:
            self.iteration_step += 1
            return {"name": item[0], "country": item[1]}
        self.iteration_step = 0
        raise StopIteration

    def __contains__(self, item):
        try:
            return bool(self.__getitem__(item))
        except ValueError:
            return False
