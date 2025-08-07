"""Provide a Doubly Linked List data structure implementation.

This module contains the necessary classes to create and manage a doubly
linked list, including the Node class for individual elements and the
DoublyLinkedList class for the main structure and operations.

Classes:
    Node: Represents a single element in the doubly linked list.
    DoublyLinkedList: Represents the complete doubly linked list structure.
"""

from collections.abc import Iterator


class Node:
    """Represent a single node in a doubly linked list.

    Attributes:
        value: The data stored in the node.
        next: A pointer to the next node in the list.
        prev: A pointer to the previous node in the list.

    """

    def __init__(self, value: int) -> None:
        """Initialize a new Node.

        Args:
            value: The data to be stored in the node.

        """
        self.value: int = value
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    """Represent a doubly linked list data structure.

    This class provides methods to append and pop elements from both ends
    of the list in O(1) time complexity.

    Attributes:
        head: The first node in the list.
        tail: The last node in the list.

    """

    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        self.head: Node | None = None
        self.tail: Node | None = None

    def __iter__(self) -> Iterator[int]:
        """Yield each node's value, from head to tail."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def append_left(self, value: int) -> None:
        """Add a new node with the given value to the beginning of the list."""
        new_node = Node(value)
        if not self.head:
            self.tail = new_node
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append_right(self, value: int) -> None:
        """Add a new node with the given value to the end of the list."""
        new_node = Node(value)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def pop_left(self) -> int | None:
        """Remove and return the value from the beginning of the list.

        Returns:
        int | None: The value of the removed node, or None if the list is empty.

        """
        if not self.head:
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return removed_value
        self.head = self.head.next
        assert self.head
        self.head.prev = None
        return removed_value

    def pop_right(self) -> int | None:
        """Remove and return the value from the end of the list.

        Returns:
        int | None: The value of the removed node, or None if the list is empty.

        """
        if not self.tail:
            return None
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return removed_value
        self.tail = self.tail.prev
        assert self.tail
        self.tail.next = None
        return removed_value


if __name__ == "__main__":
    # Create an empty doubly linked list
    dll = DoublyLinkedList()

    # Append elements to the right (end of the list)
    dll.append_right(1)  # List: 1
    dll.append_right(2)  # List: 1 <-> 2
    dll.append_right(3)  # List: 1 <-> 2 <-> 3

    # Append elements to the left (start of the list)
    dll.append_left(0)  # List: 0 <-> 1 <-> 2 <-> 3
    dll.append_left(-1)  # List: -1 <-> 0 <-> 1 <-> 2 <-> 3

    # Iterate over the list and print each value
    # Expected output: -1 0 1 2 3
    for value in dll:
        print(value)

    # Pop elements from the left (start)
    # Removes -1, then 0
    print(dll.pop_left())  # Expected: -1
    print(dll.pop_left())  # Expected: 0

    # Pop elements from the right (end)
    # Removes 3, then 2
    print(dll.pop_right())  # Expected: 3
    print(dll.pop_right())  # Expected: 2

    # Check the remaining element(s)
    # Only 1 should remain
    for value in dll:
        print(value)  # Expected: 1

    # Pop the last remaining element
    print(dll.pop_left())  # Expected: 1

    # Try to pop from an empty list (should return None)
    print(dll.pop_left())  # Expected: None
    print(dll.pop_right())  # Expected: None
