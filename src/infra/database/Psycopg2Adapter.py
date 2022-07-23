import psycopg2
from src.infra.database.Connection import Connection


class Psycopg2Adapter(Connection):
    # TODO - Ficar de olho nessa variavel
    connection = None

    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="cccat7",
            user="cccat7",
            password="123456")

    def query(self, statement: str, params: tuple):
        cursor = self.connection.cursor()
        cursor.execute(statement, params)
        self.connection.commit()
        try:
            return cursor.fetchall()
        except psycopg2.ProgrammingError:
            return None

    def save(self, statement: str, params: tuple):
        cursor = self.connection.cursor()
        cursor.execute(statement, params)
        return cursor.fetchone()

    def close(self):
        return self.connection.close()
