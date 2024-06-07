import pytest

from moschitta_query.query import Query


def test_select_query():
    query = Query().select("id", "name").from_("users").to_sql()
    assert query == "SELECT id, name FROM users"


def test_where_clause():
    query = Query().select("*").from_("users").where("age > 21").to_sql()
    assert query == "SELECT * FROM users WHERE age > 21"


def test_order_by_clause():
    query = Query().select("name").from_("users").order_by("name").to_sql()
    assert query == "SELECT name FROM users ORDER BY name"
