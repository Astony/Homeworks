import sqlite3


def open_close_conn(method):
    def wrapper(self, *args):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        result = method(self, cursor, *args)
        conn.commit()
        conn.close()
        return result

    return wrapper


class TableData:
    def __init__(self, database, table):
        self.database = database
        self.table = table
        self.iteration_step = 0

    @open_close_conn
    def len_of_database(self, cursor):
        cursor.execute(f"""SELECT COUNT(name) FROM {self.table}""")
        return cursor.fetchone()[0]

    @open_close_conn
    def search_element(self, cursor, name):
        cursor.execute(f"""SELECT * FROM {self.table} WHERE name='{name}'""")
        return cursor.fetchone()

    @open_close_conn
    def search_all_elements(self, cursor):
        cur = cursor.execute(f"""SELECT * FROM {self.table}""")
        len = self.len_of_database()
        while self.iteration_step < len:
            item = cur.fetchall()[self.iteration_step]
            self.iteration_step += 1
            return {"name": item[0], "country": item[1]}

    @open_close_conn
    def additem(self, cursor, item):
        cursor.executemany(f"INSERT INTO {self.table} VALUES (?, ?)", item)

    def __len__(self):
        return self.len_of_database()

    def __getitem__(self, item):
        return self.search_element(item)

    def __iter__(self):
        return self

    def __next__(self):
        result = self.search_all_elements()
        if result:
            return result
        else:
            self.iteration_step = 0
            raise StopIteration

    def __contains__(self, item):
        try:
            return bool(self.search_element(item))
        except TypeError:
            return False
