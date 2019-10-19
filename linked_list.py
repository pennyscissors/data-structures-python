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

    def insert_start(self, data):
        """Insert node at the beginning of the list.

        Args:
            data: Data to be stored in the node.

        """
        node = Node(data, self.head)
        self.head = node

l = SinglyLinkedList()
l.insert_start("1")
l.insert_start("2")
l.insert_start("3")
l.insert_start("a")
l.insert_start("b")
l.insert_start("c")

print(l)
