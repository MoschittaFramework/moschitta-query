from typing import Union
import sqlite3
import psycopg2
import mysql.connector


class DatabaseConnection:
    def __init__(self, db_url: str, db_type: str = 'sqlite'):
        """
        Initialize the DatabaseConnection with a database URL and type.
        :param db_url: The URL of the database.
        :param db_type: The type of the database ('sqlite', 'postgresql', or 'mysql').
        """
        self.db_url = db_url
        self.db_type = db_type.lower()
        self.connection = None

    def __enter__(self):
        """
        Enter the runtime context related to this object.
        """
        if self.db_type == 'sqlite':
            self.connection = sqlite3.connect(self.db_url)
        elif self.db_type == 'postgresql':
            self.connection = psycopg2.connect(self.db_url)
        elif self.db_type == 'mysql':
            self.connection = mysql.connector.connect(self.db_url)
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context related to this object.
        """
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str, params: Union[tuple, None] = None):
        """
        Execute a query on the database.
        :param query: The SQL query to execute.
        :param params: The parameters to bind to the query.
        """
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            conn.commit()

    def fetch_all(self, query: str, params: Union[tuple, None] = None):
        """
        Fetch all results from a query.
        :param query: The SQL query to execute.
        :param params: The parameters to bind to the query.
        :return: A list of all fetched results.
        """
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchall()

    def fetch_one(self, query: str, params: Union[tuple, None] = None):
        """
        Fetch one result from a query.
        :param query: The SQL query to execute.
        :param params: The parameters to bind to the query.
        :return: The first fetched result.
        """
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchone()
