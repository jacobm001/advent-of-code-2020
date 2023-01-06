from typing import List


class Node:
    value: int
    children: List

    def __init__(self, value: int):
        self.value    = value
        self.children = []

    def __repr__(self):
        return str(self.value)

    def add_node(self, parent: int, value: int):
        if self.value == parent:
            self.children.append(Node(value))
            return

        # there are no children to check for the parent
        # stop here
        if not self.children:
            return

        for child in self.children:
            child.add_node(parent, value)

        return

    def count_ends(self) -> int:
        # is end
        if not self.children:
            return 1

        count: int = 0
        for child in self.children:
            count += child.count_ends()

        return count


class Tree:
    def __init__(self):
        self.value    = 0
        self.children = []

    def add_node(self, parent: int, value: int):
        if parent == 0:
            self.children.append(Node(value))

        for child in self.children:
            child.add_node(parent, value)

    def count_ends(self) -> int:
        count: int = 0
        for child in self.children:
            count += child.count_ends()

        return count
