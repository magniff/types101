import pytest


from types101.ast.terms import Application, Condition, Variable, Annotation, BLiteral
from types101.ast.types import Simple, Arrow
from types101.ast.contexts import cnil, ContextCell
from types101.typechecker import infer


TYPECHECKER_CASES = [
    # Boolean literals: True
    (
        # Context doesnt matter here
        cnil().forkwith(ContextCell(Variable("x"), ttype=Simple.Boolean)),
        BLiteral.T,
        Simple.Boolean,
    ),
    # Boolean literals: False
    (
        # Context doesnt matter here
        cnil().forkwith(ContextCell(Variable("x"), ttype=Simple.Boolean)),
        BLiteral.F,
        Simple.Boolean,
    ),
    # Variable directly from the context provided
    (
        cnil().forkwith(ContextCell(Variable("x"), ttype=Simple.Boolean)),
        Variable("x"),
        Simple.Boolean,
    ),
    # Variable annotation
    (
        cnil().forkwith(ContextCell(Variable("x"), ttype=Simple.Boolean)),
        Annotation(Variable("x"), Simple.Boolean),
        Simple.Boolean,
    ),
    # Condition
    (
        cnil().forkwith(ContextCell(Variable("x"), ttype=Simple.Boolean)),
        Annotation(
            Condition(
                test=BLiteral.T,
                yes=BLiteral.T,
                no=BLiteral.T,
            ),
            Simple.Boolean
        ),
        Simple.Boolean,
    ),
    # Application 0: return nonarrow type
    (
        cnil()
        .forkwith(
            ContextCell(Variable("func"), ttype=Arrow(left=Simple.Boolean, right=Simple.Boolean))
        )
        .forkwith(
            ContextCell(Variable("x"), ttype=Simple.Boolean)
        ),
        Annotation(
            Condition(
                test=Application(Variable("func"), Variable("x")),
                yes=BLiteral.T,
                no=Application(Variable("func"), BLiteral.T),
            ),
            Simple.Boolean
        ),
        Simple.Boolean,
    ),
    # Application 1: return arrow type
    (
        cnil()
        .forkwith(
            # func : Boolean -> (Boolean -> Boolean)
            ContextCell(Variable("func"),
                ttype=Arrow(
                    left=Simple.Boolean,
                    right=Arrow(left=Simple.Boolean, right=Simple.Boolean)
                )
            )
        )
        .forkwith(
            ContextCell(Variable("x"), ttype=Simple.Boolean)
        ),
        Application(Variable("func"), Variable("x")),
        Arrow(left=Simple.Boolean, right=Simple.Boolean)
    ),
]


@pytest.mark.parametrize("context, term, expected", TYPECHECKER_CASES)
def test_typeinference(context, term, expected):
    assert infer(context, term) == expected
