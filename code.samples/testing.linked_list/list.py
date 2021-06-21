from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, key):
        self.key  = key
        self.prev = None
        self.next = None

@dataclass
class List:
    """basic linked list"""
    head = None
    tail = None

    def __init__(self, key: int):
        self.head = Node(key)

    def insert(self, key: int):
        if self.head.next is None:
            self.tail = Node(key)
            self.tail.prev = self.head
            self.head.next = self.tail

        else:
            curr = self.head.next
            # while curr.next is not None:

