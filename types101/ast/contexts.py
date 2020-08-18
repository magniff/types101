from copy import deepcopy
from . import types
from . import terms


class ContextCell:
    def __init__(self, variable: terms.Variable, ttype: types.Type) -> None:
        self.variable = variable
        self.ttype = ttype


class Context(list):
    def fork_with(self, item: ContextCell) -> 'Context':
        new_context = deepcopy(self)
        new_context.append(item)
        return new_context


def cnil() -> Context:
    return Context()


def cappend(item: ContextCell, context: Context) -> Context:
    context.append(item)
    return context
