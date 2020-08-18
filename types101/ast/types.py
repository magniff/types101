from enum import Enum


class Type:
    pass


class Z(Type, Enum):
    """Zero-ary kind of types
    """
    Boolean = 0


class B(Type):
    """Bin-ary kind of types, arrow type basically
    """
    def __init__(self, left: Type, right: Type) -> None:
        self.left = left
        self.right = right
