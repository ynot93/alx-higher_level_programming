#!/usr/bin/python3
"""This module is an implementation of singly linked lists"""


class Node:
    """defines the node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): The integer data for this node
            next_node (node): Next node in the linked list(defaults to none)

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data of current node"""
        return self._data

    @data.setter
    def data(self, value):
        """Set value of data.

        Args:
            value: Value of data to set.
        
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Get data of next node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a node object")
        self._next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize empty list"""
        self.head = None

    def sorted_insert(self, value):
        """Insert node in sorted increasing order.

        Args:
            value (int): Integer to add to list.

        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return string representation of list."""
        linked_list = []
        current = self.head
        while current:
            linked_list.append(str(current.data))
            current = current.next_node
        return '\n'.join(linked_list)
