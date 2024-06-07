import pytest

from moschitta_query.expressions import Column, Literal, Operation


def test_column():
    col = Column("age")
    assert str(col) == "age"


def test_literal():
    lit = Literal(21)
    assert str(lit) == "21"

    lit_str = Literal("test")
    assert str(lit_str) == "'test'"


def test_operation():
    col = Column("age")
    lit = Literal(21)
    op = Operation(col, ">", lit)
    assert str(op) == "age > 21"
