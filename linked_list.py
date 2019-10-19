class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
        if not self.tail:
            self.tail = self.head

    def insert_end(self, data):
        """Insert node at the end of the list.

        Args:
            data: Data to be stored in the node.

        """
        node = Node(data)
        self.tail.next = node
        self.tail = node

    def delete_start(self):
        """Delete first node in the list."""
        if self.head:
            self.head = self.head.next

    def delete_end(self):
        """Delete last node in the list."""
        current = self.head
        while current:
            if current.next == self.tail:
                current.next = None
                self.tail = current
            else:
                current = current.next


l = SinglyLinkedList()
l.insert_start("1")
l.insert_start("2")
l.insert_start("3")
l.insert_end("a")
l.insert_end("b")
l.insert_end("c")

print(l)
# print(l.head.data)
# print(l.tail.data)

# l.delete_start()
l.delete_end()
print(l)
