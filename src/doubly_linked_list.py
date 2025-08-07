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
        length: The number of nodes in the list.

    """

    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def __iter__(self) -> Iterator[int]:
        """Yield each node's value, from head to tail."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self.length

    def append_left(self, value: int) -> None:
        """Add a new node with the given value to the beginning of the list."""
        new_node = Node(value)
        self.length += 1
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
        self.length += 1
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
            self.length = 0
            return removed_value
        self.head = self.head.next
        assert self.head
        self.head.prev = None
        self.length -= 1
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
            self.length = 0
            return removed_value
        self.tail = self.tail.prev
        assert self.tail
        self.tail.next = None
        self.length -= 1
        return removed_value

    def get(self, index: int) -> int:
        """Get the value at a specific index.

        This method retrieves the value of the node at the given index.
        It optimizes the search by traversing from the head for the first half
        of the list and from the tail for the second half.

        Args:
        index: The index of the node to retrieve.

        Returns:
        int: The value of the node at the specified index.

        Raises:
        IndexError: If the index is out of the list's bounds.

        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                assert current
                current = current.next
            assert current
            return current.value
        current = self.tail
        for _ in range(self.length - index - 1):
            assert current
            current = current.prev
        assert current
        return current.value


if __name__ == "__main__":
    print("--- Initializing Doubly Linked List ---")
    dll = DoublyLinkedList()
    print(f"Initial list: {list(dll)}")
    print(f"Initial length: {len(dll)}\n")

    print("--- Testing append_right ---")
    dll.append_right(1)
    dll.append_right(2)
    dll.append_right(3)
    print(f"List after append_right: {list(dll)}")
    print(f"Length: {len(dll)}\n")

    print("--- Testing append_left ---")
    dll.append_left(0)
    dll.append_left(-1)
    print(f"List after append_left: {list(dll)}")
    print(f"Length: {len(dll)}\n")

    print("--- Testing get() ---")
    print(f"Value at index 0: {dll.get(0)}")  # Expected: -1
    print(f"Value at index 2: {dll.get(2)}")  # Expected: 1
    print(f"Value at index 4: {dll.get(4)}")  # Expected: 3

    try:
        dll.get(99)
    except IndexError as e:
        print(f"Successfully caught expected error: {e}\n")

    print("--- Testing pop_left ---")
    print(f"Popped from left: {dll.pop_left()}")  # Expected: -1
    print(f"List after pop_left: {list(dll)}")
    print(f"Length: {len(dll)}")
    print(f"Popped from left: {dll.pop_left()}")  # Expected: 0
    print(f"List after pop_left: {list(dll)}")
    print(f"Length: {len(dll)}\n")

    print("--- Testing pop_right ---")
    print(f"Popped from right: {dll.pop_right()}")  # Expected: 3
    print(f"List after pop_right: {list(dll)}")
    print(f"Length: {len(dll)}")
    print(f"Popped from right: {dll.pop_right()}")  # Expected: 2
    print(f"List after pop_right: {list(dll)}")
    print(f"Length: {len(dll)}\n")

    print("--- Final State ---")
    print(f"Final list: {list(dll)}")  # Expected: [1]
    print(f"Final length: {len(dll)}\n")  # Expected: 1

    print("--- Testing empty list ---")
    dll.pop_left()
    print(f"Popped from empty list (left): {dll.pop_left()}")  # Expected: None
    print(f"Popped from empty list (right): {dll.pop_right()}")  # Expected: None
    print(f"Length of empty list: {len(dll)}")  # Expected: 0
