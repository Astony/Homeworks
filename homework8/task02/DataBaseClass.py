import sqlite3


def open_close_conn(method):
    def wrapper(self, *args):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        result = method(self, cursor, *args)
        conn.close()
        return result

    return wrapper


class DBConnector:
    def __init__(self, database, table):
        self.database = database
        self.table = table
        self.iteration = 0

    @open_close_conn
    def len_of_database(self, cursor):
        cursor.execute("""SELECT COUNT(name) FROM presidents""")
        return cursor.fetchone()[0]

    @open_close_conn
    def search_element(self, cursor, name):
        cursor.execute(f"""SELECT name FROM presidents WHERE name='{name}'""")
        return cursor.fetchone()

    @open_close_conn
    def search_all_elements(self, cursor):
        cur = cursor.execute("""SELECT * FROM presidents""")
        len = self.len_of_database()
        while self.iteration < len:
            item = cur.fetchall()[self.iteration]
            self.iteration += 1
            return item[0]

    @open_close_conn
    def additem(self, cursor, item):
        cur = cursor.execute(f"""INSERT INTO name VALUES ('{item}')""")





class TableData:
    def __init__(self, database, table):
        self.connector = DBConnector(database, table)

    def __len__(self):
        return self.connector.len_of_database()

    def __getitem__(self, item):
        return self.connector.search_element(item)[0]

    def __iter__(self):
        return self

    def __next__(self):
        result = self.connector.search_all_elements()
        if result:
            return result
        else:
            self.connector.iteration = 0
            raise StopIteration


    def __contains__(self, item):
        try:
            return bool(self.connector.search_element(item))
        except TypeError:
            return False

    def add(self, item):






presidents1 = TableData("example.db", "presidents")
presidents2 = TableData("example.db", "presidents")

for i in presidents1:
    print(i)
for i in presidents2:
    print(i)

