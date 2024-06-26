# Moschitta Query Documentation

The `moschitta-query` package provides a Fluent Query Builder for the Moschitta Framework, enabling developers to generate SQL queries programmatically using a fluent interface.

## Installation

You can install `moschitta-query` via pip:

```bash
pip install moschitta-query
```

Or use it with Poetry:

```bash
poetry add moschitta-query
```

## Usage

### Basic Query Construction

To use `moschitta-query`, you need to initialize an instance of the `Query` class.

```python
from moschitta_query.query import Query

# Create a basic select query
query = Query().select('id', 'name').from_('users')
print(query.to_sql())
# Output: SELECT id, name FROM users
```

### Adding Conditions

You can add conditions to your query using the `where` method.

```python
# Add a where clause to the query
query = Query().select('*').from_('users').where('age > 21')
print(query.to_sql())
# Output: SELECT * FROM users WHERE age > 21
```

### Joining Tables

Perform joins using the `join` method.

```python
# Perform an inner join with another table
query = Query().select('users.id', 'users.name', 'orders.total').from_('users') \
               .join('orders', 'users.id = orders.user_id')
print(query.to_sql())
# Output: SELECT users.id, users.name, orders.total FROM users JOIN orders ON users.id = orders.user_id
```

### Ordering Results

Specify the order of the result set using the `order_by` method.

```python
# Order the result set by a column
query = Query().select('name').from_('users').order_by('name')
print(query.to_sql())
# Output: SELECT name FROM users ORDER BY name
```

## API Reference

### `moschitta_query.query.Query`

- `select(*columns: str) -> Query`: Specifies the columns to select in the query.
- `from_(table: str) -> Query`: Specifies the table to select data from.
- `where(*conditions: str) -> Query`: Adds conditions to filter the result set.
- `join(table: str, on_clause: str) -> Query`: Performs an inner join with another table.
- `left_join(table: str, on_clause: str) -> Query`: Performs a left outer join with another table.
- `right_join(table: str, on_clause: str) -> Query`: Performs a right outer join with another table.
- `order_by(*columns: str) -> Query`: Specifies the columns to order the result set by.
- `group_by(*columns: str) -> Query`: Groups the result set by the specified columns.
- `having(*conditions: str) -> Query`: Adds conditions to filter the grouped result set.
- `limit(count: int) -> Query`: Limits the number of rows returned by the query.
- `offset(start: int) -> Query`: Specifies the starting offset for the result set.
- `to_sql() -> str`: Returns the constructed SQL query as a string.


---

## Connecting to a Database

To connect to a database, initialize an instance of the `DatabaseConnection` class with the database URL and type. Supported database types are `'sqlite'`, `'postgresql'`, and `'mysql'`.

```python
from moschitta_query import DatabaseConnection

# Connect to an SQLite database
sqlite_url = 'sqlite:///example.db'
with DatabaseConnection(sqlite_url, 'sqlite') as conn:
    conn.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')

# Connect to a PostgreSQL database
postgresql_url = 'postgresql://username:password@localhost:5432/mydatabase'
with DatabaseConnection(postgresql_url, 'postgresql') as conn:
    conn.execute_query('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(50))')

# Connect to a MySQL database
mysql_url = 'mysql://username:password@localhost:3306/mydatabase'
with DatabaseConnection(mysql_url, 'mysql') as conn:
    conn.execute_query('CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))')
```

### Executing Queries

Once connected, you can execute SQL queries using the `execute_query`, `fetch_all`, and `fetch_one` methods of the `DatabaseConnection` class.

```python
# Insert data into the users table
with DatabaseConnection(sqlite_url, 'sqlite') as conn:
    conn.execute_query("INSERT INTO users (name) VALUES ('Alice')")
    
# Fetch all users from the table
with DatabaseConnection(sqlite_url, 'sqlite') as conn:
    users = conn.fetch_all("SELECT * FROM users")
    print(users)
```

### Handling Connection Context

The `DatabaseConnection` class is designed to be used within a context manager (`with` statement), ensuring that the connection is properly established and closed.

```python
# Connect to the database and execute queries within a context
with DatabaseConnection(sqlite_url, 'sqlite') as conn:
    # Execute queries or perform database operations
    ...
```

## Contributing

Contributions to `moschitta-query` are welcome! You can contribute by opening issues for bugs or feature requests, submitting pull requests, or helping improve the documentation.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
