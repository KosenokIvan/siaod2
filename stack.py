from typing import Optional, Iterable


class Stack:
    def __init__(self, collection_: Optional[Iterable] = None):
        self._stack = list(collection_) if collection_ is not None else []

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def append(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()
