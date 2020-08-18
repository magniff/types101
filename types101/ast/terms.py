from enum import Enum
from .types import Type


class Term:
    pass


class Variable(Term):
    def __init__(self, varname: str) -> None:
        self.varname = varname


class Application(Term):
    def __init__(self, left: Term, right: Term) -> None:
        self.left = left
        self.right = right


class Abstraction(Term):
    def __init__(self, var: Variable, inner: Term) -> None:
        self.var = var
        self.inner = inner


class Annotation(Term):
    def __init__(self, term: Term, ttype: Type) -> None:
        self.term = term
        self.ttype = ttype


class Condition(Term):
    def __init__(self, test: Term, yes: Term, no: Term) -> None:
        self.test = test
        self.yes = yes
        self.no = no


class BLiteral(Term, Enum):
    T = 0
    F = 1
