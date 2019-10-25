class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next_ = next_

class SinglyLinkedList:
    def __init__(self, data_list=None):
        self.head = None
        self.tail = None

        if data_list:
            # Needs some input validation
            for data in reversed(data_list):
                self.insert_start(data)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next_

    def __repr__(self):
        module = type(self).__module__
        class_name = self.__class__.__name__

        return f"{module}.{class_name}({str(self)})"

    def __str__(self):
        str_ = ''
        for current in iter(self):
            str_ = f"{str_}{', ' if str_ else ''}{current.data}"

        return f"[{str_}]"

    def __len__(self):
        """Counts the number of nodes in the list.
        
        Returns:
            int: Number of nodes in the list.
            
        """
        length = 0
        for _ in iter(self):
            length += 1

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
        self.tail.next_ = node
        self.tail = node

    def delete_start(self):
        """Delete first node in the list."""
        if self.head:
            self.head = self.head.next_

    def delete_end(self):
        """Delete last node in the list."""
        for current in iter(self):
            if current.next_ == self.tail:
                current.next_ = None
                self.tail = current
            else:
                current = current.next_
