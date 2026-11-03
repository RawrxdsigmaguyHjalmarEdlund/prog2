from typing import TypeVar, Generic
T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, value):
        self.value = value
    def get_value(self) -> T:
        return self.value
