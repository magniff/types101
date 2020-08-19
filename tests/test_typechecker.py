import pytest


from types101.ast.terms import Application, Condition, Variable, Annotation, BLiteral
from types101.ast.types import Z, B
from types101.ast.contexts import cnil, ContextCell
from types101.typechecker import infer


TYPECHECKER_CASES = [
    # Boolean literals: True
    (
        # Context doesnt matter here
        cnil().forkwith(ContextCell(Variable("x"), ttype=Z.Boolean)),
        BLiteral.T,
        Z.Boolean,
    ),
    # Boolean literals: False
    (
        # Context doesnt matter here
        cnil().forkwith(ContextCell(Variable("x"), ttype=Z.Boolean)),
        BLiteral.F,
        Z.Boolean,
    ),
    # Variable directly from the context provided
    (
        cnil().forkwith(ContextCell(Variable("x"), ttype=Z.Boolean)),
        Variable("x"),
        Z.Boolean,
    ),
    # Variable annotation
    (
        cnil().forkwith(ContextCell(Variable("x"), ttype=Z.Boolean)),
        Annotation(Variable("x"), Z.Boolean),
        Z.Boolean,
    ),
    # Condition
    (
        cnil().forkwith(ContextCell(Variable("x"), ttype=Z.Boolean)),
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
    # Application 0: return nonarrow type
    (
        cnil()
        .forkwith(
            ContextCell(Variable("func"), ttype=B(left=Z.Boolean, right=Z.Boolean))
        )
        .forkwith(
            ContextCell(Variable("x"), ttype=Z.Boolean)
        ),
        Annotation(
            Condition(
                test=Application(Variable("func"), Variable("x")),
                yes=BLiteral.T,
                no=Application(Variable("func"), BLiteral.T),
            ),
            Z.Boolean
        ),
        Z.Boolean,
    ),
    # Application 1: return arrow type
    (
        cnil()
        .forkwith(
            # func : Boolean -> (Boolean -> Boolean)
            ContextCell(Variable("func"),
                ttype=B(
                    left=Z.Boolean,
                    right=B(left=Z.Boolean, right=Z.Boolean)
                )
            )
        )
        .forkwith(
            ContextCell(Variable("x"), ttype=Z.Boolean)
        ),
        Application(Variable("func"), Variable("x")),
        B(left=Z.Boolean, right=Z.Boolean)
    ),
]


@pytest.mark.parametrize("context, term, expected", TYPECHECKER_CASES)
def test_typeinference(context, term, expected):
    assert infer(context, term) == expected
