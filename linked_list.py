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
        while current:
            result += str(current.data)
            current = current.next
            result += ' -> ' if current else ']'

        return result

    def length(self):
        """Counts the number of nodes in the list.
        
        Returns:
            int: Number of nodes in the list.
            
        """
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next

        return length

    def insert_start(self, data):
        """Insert node at the start of the list.

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

print(l.length())
