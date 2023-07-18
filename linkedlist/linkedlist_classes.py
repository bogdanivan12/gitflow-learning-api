"""
File containing the classes needed for a linked list implementation.
"""


class Node:
    """
    Class that represents a node in a linked list.

    Object attributes:
        value: the actual value of the node.
        next_node = reference to the next node in the linked list.
    """
    def __init__(self, value=None, next_node=None):
        """
        Function that initializes the object with the provided parameters.
        """
        self.value = value
        self.next = next_node

    def __str__(self):
        """
        Function that defines the string cast for the Node objects.
        """
        return str(self.value)


class LinkedList:
    """
    Class that represents a linked list.

    Object attributes:
        head: the first element (node) in the list.
        name: the name of the list.
    """
    def __init__(self, name, head=None):
        """
        Function that initializes the object with the provided parameters.
        """
        self.head = head
        self.name = name

    def __str__(self):
        """
        Function that defines the string cast for the Node objects.
        """
        response = str(self.head)
        aux = self.head.next_node
        while aux is not None:
            response += f" {aux}"
            aux = aux.next_node
        return response
