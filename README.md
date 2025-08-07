# Data Structures

A repository dedicated to the study and implementation of fundamental data structures and algorithms in pure Python. This project focuses on creating clean, well-documented, and efficient code to solidify theoretical concepts learned during my academic and personal studies.

Each data structure is implemented with a focus on best practices, including clear documentation, type hinting, and performance analysis.

## Doubly Linked List Implementation in Python

A pure Python implementation of a Doubly Linked List data structure. This project is part of a personal study on fundamental data structures and algorithms, focusing on clean code, performance, and clear documentation.

### 📂 Overview

A Doubly Linked List is a linear data structure where each element (node) contains a value and pointers to both the next and the previous nodes in the sequence. This bidirectional linkage allows for efficient traversal in both directions.

This implementation provides a `DoublyLinkedList` class that supports common operations like appending and popping elements from both ends of the list.

### ✨ Features & Operations

The `DoublyLinkedList` class supports the following methods and features:

- `append_left(value)`: Adds a new element to the beginning of the list.
- `append_right(value)`: Adds a new element to the end of the list.
- `pop_left()`: Removes and returns the element from the beginning of the list.
- `pop_right()`: Removes and returns the element from the end of the list.
- `get(index)`: Returns the value at a specific index in the list.
- `len()`: Supports the built-in `len()` function to get the list's size in O(1) time.
- **Iterable**: The list can be traversed from head to tail using a standard `for` loop.

### ⏱️ Time Complexity

The performance of the key operations is a major advantage of a doubly linked list.

| Operation       | Time Complexity |
| --------------- | :-------------: |
| Append Left     |      O(1)       |
| Append Right    |      O(1)       |
| Pop Left        |      O(1)       |
| Pop Right       |      O(1)       |
| Search          |      O(n)       |
| Access by Index |      O(n)       |

### 💾 Space Complexity

The space complexity of the Doubly Linked List is **O(n)**, as it needs to store a node for each of the `n` elements in the list.

### 🚀 How to Use

The implementation is contained within a single file and can be used by importing the `DoublyLinkedList` class.

Here is a basic usage example:

```python
from doubly_linked_list import DoublyLinkedList

# Create a new list
dll = DoublyLinkedList()

# Append elements
dll.append_right(10)
dll.append_right(20)
dll.append_left(5)  # List: 5 <-> 10 <-> 20

# Check the length
print(f"Current length: {len(dll)}")  # Output: 3

# Get a value by index
print(f"Value at index 1: {dll.get(1)}")  # Output: 10

# Iterate and print values
for value in dll:
    print(value)  # Output: 5, 10, 20

# Pop elements
print(f"Popped from right: {dll.pop_right()}")  # Output: 20
print(f"Popped from left: {dll.pop_left()}")   # Output: 5
```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
