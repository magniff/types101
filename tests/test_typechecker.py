import pytest

from types101.ast.terms import Condition, Variable, Annotation, BLiteral
from types101.ast.types import Z, B
from types101.ast.contexts import cnil, cappend, ContextCell
from types101.typechecker import infer


TYPECHECKER_CASES = [
    # Boolean literals: True
    (
        # Context doesnt matter here
        cnil().fork_with(ContextCell(Variable("x"), ttype=Z.Boolean)),
        BLiteral.T,
        Z.Boolean,
    ),
    # Boolean literals: False
    (
        # Context doesnt matter here
        cnil().fork_with(ContextCell(Variable("x"), ttype=Z.Boolean)),
        BLiteral.F,
        Z.Boolean,
    ),
    # Variable directly from the context provided
    (
        cnil().fork_with(ContextCell(Variable("x"), ttype=Z.Boolean)),
        Variable("x"),
        Z.Boolean,
    ),
    # Variable annotation
    (
        cnil().fork_with(ContextCell(Variable("x"), ttype=Z.Boolean)),
        Annotation(Variable("x"), Z.Boolean),
        Z.Boolean,
    ),
    # Condition
    (
        cnil().fork_with(ContextCell(Variable("x"), ttype=Z.Boolean)),
        Annotation(
            Condition(
                test=BLiteral.T,
                yes=BLiteral.T,
                no=BLiteral.T,
            ),
            Z.Boolean
        ),
        Z.Boolean,
    ),
]


@pytest.mark.parametrize("context, term, expected", TYPECHECKER_CASES)
def test_typeinference(context, term, expected):
    assert infer(context, term) == expected
