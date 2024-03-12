from typing import Optional, Iterable


class Deque:
    def __init__(self, collection_: Optional[Iterable] = None):
        self._deque = list(collection_) if collection_ is not None else []

    def is_empty(self) -> bool:
        return len(self._deque) == 0

    def append_start(self, item):
        self._deque.insert(0, item)

    def append_end(self, item):
        self._deque.append(item)

    def pop_start(self):
        return self._deque.pop(0)

    def pop_end(self):
        return self._deque.pop()
