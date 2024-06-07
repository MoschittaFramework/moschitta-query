import unittest
import os
import sqlite3
from moschitta_query.helpers import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up a temporary database for testing.
        """
        cls.db_url = 'test_database.db'
        cls.connection = DatabaseConnection(cls.db_url)

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the temporary database after tests are done.
        """
        os.remove(cls.db_url)

    def test_connection_establishment(self):
        """
        Test that the connection to the database is established and closed properly.
        """
        with self.connection as conn:
            self.assertIsNotNone(conn)
            self.assertTrue(hasattr(conn, 'execute'))
        
        # Check the status of the connection using a method that raises an exception if closed
        with self.assertRaises(sqlite3.ProgrammingError):
            conn.execute('SELECT 1')

    def test_execute_query(self):
        """
        Test executing a query on the database.
        """
        with self.connection as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
            conn.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 25))
            conn.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 30))
            conn.commit()

            cursor = conn.execute('SELECT * FROM users')
            rows = cursor.fetchall()
            self.assertEqual(len(rows), 2)

    def test_fetch_all(self):
        """
        Test fetching all results from a query.
        """
        with self.connection as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
            conn.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Charlie', 35))
            conn.commit()

            rows = self.connection.fetch_all('SELECT * FROM users')
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[2][1], 'Charlie')

    def test_fetch_one(self):
        """
        Test fetching a single result from a query.
        """
        with self.connection as conn:
            row = self.connection.fetch_one('SELECT * FROM users WHERE name = ?', ('Alice',))
            self.assertIsNotNone(row)
            self.assertEqual(row[1], 'Alice')

if __name__ == '__main__':
    unittest.main()
