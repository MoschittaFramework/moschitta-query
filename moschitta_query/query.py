from typing import List, Union


class Query:
    def __init__(self):
        self._select: List[str] = []
        self._from: str = ""
        self._where: List[str] = []
        self._join: List[str] = []
        self._order_by: List[str] = []
        self._group_by: List[str] = []
        self._having: List[str] = []
        self._limit: Union[int, None] = None
        self._offset: Union[int, None] = None

    def select(self, *columns: str) -> "Query":
        self._select.extend(columns)
        return self

    def from_(self, table: str) -> "Query":
        self._from = table
        return self

    def where(self, *conditions: str) -> "Query":
        self._where.extend(conditions)
        return self

    def join(self, table: str, on_clause: str) -> "Query":
        self._join.append(f"JOIN {table} ON {on_clause}")
        return self

    def left_join(self, table: str, on_clause: str) -> "Query":
        self._join.append(f"LEFT JOIN {table} ON {on_clause}")
        return self

    def right_join(self, table: str, on_clause: str) -> "Query":
        self._join.append(f"RIGHT JOIN {table} ON {on_clause}")
        return self

    def order_by(self, *columns: str) -> "Query":
        self._order_by.extend(columns)
        return self

    def group_by(self, *columns: str) -> "Query":
        self._group_by.extend(columns)
        return self

    def having(self, *conditions: str) -> "Query":
        self._having.extend(conditions)
        return self

    def limit(self, count: int) -> "Query":
        self._limit = count
        return self

    def offset(self, start: int) -> "Query":
        self._offset = start
        return self

    def to_sql(self) -> str:
        query = f"SELECT {', '.join(self._select)} FROM {self._from}"
        if self._where:
            query += f" WHERE {' AND '.join(self._where)}"
        if self._join:
            query += " " + " ".join(self._join)
        if self._group_by:
            query += f" GROUP BY {', '.join(self._group_by)}"
        if self._having:
            query += f" HAVING {' AND '.join(self._having)}"
        if self._order_by:
            query += f" ORDER BY {', '.join(self._order_by)}"
        if self._limit is not None:
            query += f" LIMIT {self._limit}"
        if self._offset is not None:
            query += f" OFFSET {self._offset}"
        return query
