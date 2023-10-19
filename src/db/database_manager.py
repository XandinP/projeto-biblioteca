import cx_Oracle


class DatabaseManager:
    def __init__(self) -> None:
        self.user = "SYSTEM"
        self.password = "32256029"
        self.host = "localhost"
        self.port = "1521"
        self.sid = "XE"
        pass

    def createConnection(self):
        dsn = cx_Oracle.makedsn(self.host, self.port, sid=self.sid)
        self.conn = cx_Oracle.connect(self.user, self.password, dsn)
        self.cursor = self.conn.cursor()

    def execute(self, query: str):
        self.cursor.execute(query)
        self.conn.commit()
        pass

    def insert(self, query: str):
        self.execute(query)
        pass

    def readAll(self, query: str):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def readOne(self, query: str):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def update(self, query: str):
        return self.insert(query)

    def delete(self, query: str):
        return self.insert(query)

    def getCount(self, table: str):
        self.cursor.execute(f"select count(1) from {table}")
        return self.cursor.fetchone()[0]

