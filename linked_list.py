from yaml import dump


class Node:
    def __init__(self, value, index: int, left, right):
        self.left = left
        self.right = right
        self.value = value
        self.index = index


class LinkedList:
    def __init__(self, *args):

        if not args:
            self._first = self._last = None

        else:
            self._first = Node(value=args[0], index=0, left=None, right=None)
            node = self._first

            for index, value in enumerate(args[1:]):
                node.right = Node(value, index + 1, left=node, right=None)
                node = node.right

            self._last = node

    def __iter__(self):
        node = self._first

        while node:
            yield node
            node = node.right

    def first(self):
        return self._first.value

    def last(self):
        return self._last.value

    def is_empty(self) -> bool:
        return self._first is None

    def _insert_single(self, value):
        node = Node(value, index=0, left=None, right=None)
        self._first = self._last = node

    def _get(self, index: int):
        if index < 0:
            for node in self:
                if node.index == self.size + index:
                    return node

        for node in self:
            if node.index == index:
                return node

        raise IndexError

    def at(self, index: int):
        return self._get(index).value

    def find(self, criteria: callable):
        for node in self:
            if criteria(node.value):
                return node.value

        return None

    def insert(self, at: int, *args):
        """inserts BEFORE index"""

        if not args:
            raise ValueError

        if at == 0:
            prev_right = self._first
            new_first = Node(value=args[0], index=0, left=None, right=None)
            args = args[1:]
            self._first = current = new_first
        elif at == self.size:
            prev_right = None
            current = self._last
        else:
            current = self._get(at - 1)
            print(current.value)
            prev_right = current.right

        for value in args:
            new = Node(value, index=current.index + 1, left=current, right=None)
            current.right = new
            current = new

        if prev_right:
            current.right = prev_right
            prev_right.left = current

        diff = len(args) + 1
        current = current.right
        while current:
            current.index += diff
            current = current.right

    def add_first(self, value):
        self.insert(0, value)

    def add_last(self, value):
        if self.is_empty():
            self._insert_single(value)
            return

        self.insert(self.size, value)

    def _remove(self, node: Node):
        if node.index == 0:
            node.right.left = None
            self._first = node.right
        elif node.index == self.size - 1:
            node.left.right = None
            self._last = node.left
        else:
            node.right.left = node.left
            node.left.right = node.right

        node.left = node.right = None

    def remove_at(self, index: int):
        node = self._get(index)
        self._remove(node)

    def remove(self, value):
        for node in self:
            if node.value == value:
                self._remove(node)
                return

        raise ValueError(f"{value} not found")

    def remove_first(self):
        self.remove_at(0)

    def remove_last(self):
        self.remove_at(self.size - 1)

    def change(self, index: int, new_value):
        node = self._get(index)
        node.value = new_value

    @property
    def size(self) -> int:
        return self._last.index + 1

    def clear(self):
        self._first = self._last = None

    def clone(self):
        return LinkedList(*self.to_list())

    def to_list(self) -> list:
        return [node.value for node in self]

    def __repr__(self) -> str:
        return str(self.to_list())


if __name__ == "__main__":
    l = LinkedList("a", "bx", "c", "d")
    print(l.find(lambda x: len(x) == 2))
