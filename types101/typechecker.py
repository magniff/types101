from types101.ast.contexts import ContextCell
from types101.ast.terms import Abstraction, Application, Condition, BLiteral, Variable
from .ast import terms, types, contexts
from .exceptions import TypingError101


def lookup_var(context: contexts.Context, variable: terms.Variable) -> types.Type:
    lookup_result = context.get(variable)
    if lookup_result is not None:
        return lookup_result
    else:
        raise TypingError101()


def check(context: contexts.Context, term: terms.Term, ttype: types.Type) -> bool:
    if isinstance(term, Condition):
        return (
            check(context, term.test, types.Z.Boolean) and
            check(context, term.yes, ttype) and
            check(context, term.no, ttype)
        )
    elif isinstance(term, Abstraction):
        if not isinstance(ttype, types.B):
            return False
        return check(
            context=context.forkwith(
                ContextCell(variable=term.var, ttype=ttype.left)
            ),
            term=term.inner,
            ttype=ttype.right
        )
    else:
        return infer(context, term) == ttype


def infer(context: contexts.Context, term: terms.Term) -> types.Type:
    if term in (terms.BLiteral.T, terms.BLiteral.F):
        return types.Z.Boolean
    elif isinstance(term, terms.Variable):
        return lookup_var(context, term)
    elif isinstance(term, terms.Annotation):
        if check(context, term.term, ttype=term.ttype):
            return term.ttype
        else:
            raise TypingError101()
    elif isinstance(term, Application):
        # e0 e1 or how we call it term.left term.right
        function_type = infer(context, term.left)
        # if function_type is not really a function type, then fail
        if not isinstance(function_type, types.B):
            raise TypingError101()
        if check(context, term.right, function_type.left):
            return function_type.right
        else:
            raise TypingError101()
    else:
        raise TypingError101()
