from typing import Any


from enum import Enum
from .types import Type


class Term:
    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def __eq__(self, other: Any) -> bool:
        return type(self) == type(other) and self.as_tuple() == other.as_tuple()


class Variable(Term):
    def as_tuple(self):
        return (self.varname,)

    def __init__(self, varname: str) -> None:
        self.varname = varname


class Application(Term):
    def as_tuple(self):
        return (self.left.as_tuple(), self.right.as_tuple())

    def __init__(self, left: Term, right: Term) -> None:
        self.left = left
        self.right = right


class Abstraction(Term):
    def as_tuple(self):
        return (self.var.as_tuple(), self.term.as_tuple())

    def __init__(self, var: Variable, inner: Term) -> None:
        self.var = var
        self.inner = inner


class Annotation(Term):
    def as_tuple(self):
        return (self.term.as_tuple(), self.ttype.as_tuple())

    def __init__(self, term: Term, ttype: Type) -> None:
        self.term = term
        self.ttype = ttype


class Condition(Term):
    def as_tuple(self):
        return (self.test.as_tuple(), self.yes.as_tuple(), self.no.as_tuple())

    def __init__(self, test: Term, yes: Term, no: Term) -> None:
        self.test = test
        self.yes = yes
        self.no = no


class BLiteral(Term, Enum):
    T = 0
    F = 1
    def as_tuple(self):
        return (self.value,)
