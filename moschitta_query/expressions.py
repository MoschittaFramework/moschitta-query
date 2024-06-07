from typing import Union


class Column:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name


class Literal:
    def __init__(self, value: Union[int, float, str]):
        self.value = value

    def __str__(self) -> str:
        if isinstance(self.value, str):
            return f"'{self.value}'"
        return str(self.value)


class Operation:
    def __init__(self, left: "Column", operator: str, right: "Literal"):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self) -> str:
        return f"{self.left} {self.operator} {self.right}"
