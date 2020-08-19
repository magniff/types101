from __future__ import annotations
from copy import deepcopy


from . import types
from . import terms
from ..exceptions import ContextCorruption


class ContextCell:
    def __init__(self, variable: terms.Variable, ttype: types.Type) -> None:
        self.variable = variable
        self.ttype = ttype


class Context(dict):
    def forkwith(self, item: ContextCell) -> Context:
        context_response = self.get(item.variable)
        if context_response is not None and context_response != item.ttype:
            raise ContextCorruption()
        new_context = deepcopy(self)
        new_context[item.variable] = item.ttype
        return new_context


def cnil() -> Context:
    return Context()
