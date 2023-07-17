"""
File containing the classes needed for a linked list implementation.
"""


class Node:
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.next = nextNode

    def __str__(self):
        return str(self.value)


class LinkedList:
    nextId = 0

    def __init__(self, head=None):
        self.head = head
        self.id = LinkedList.nextId
        LinkedList.nextId += 1

    def __str__(self):
        response = str(self.head)
        aux = self.head.next
        while aux is not None:
            response += f" {aux}"
            aux = aux.next
        return response
