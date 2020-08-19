from typing import Any


from enum import Enum


class Type:
    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def __eq__(self, other) -> bool:
        return self.as_tuple() == other.as_tuple()


class Z(Type, Enum):
    Boolean = 0

    def __repr__(self):
        return str(self.name)

    def as_tuple(self):
        return (self.value,)


class B(Type):
    def __repr__(self):
        return "%s -> %s" % (repr(self.left), repr(self.right))

    def as_tuple(self):
        return (self.left.as_tuple(), self.right.as_tuple())

    def __init__(self, left: Type, right: Type) -> None:
        self.left = left
        self.right = right
