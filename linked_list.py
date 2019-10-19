class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        result = '['
        while current is not None:
            result += str(current.data)
            current = current.next
            result += ' -> ' if current else ']'

        return result
