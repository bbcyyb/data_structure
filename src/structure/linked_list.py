# coding: utf-8


class LinkedList(object):
    """
    tail -> data1 -> data2 -> head
    """
    def __init__(self):
        self._head = self.LinkedNode()
        self._tail = self.LinkedNode()
        self._head.prev = self._tail
        self._tail.next = self._head
        self._count = 0
        self._iterhead = self._tail

    def insert(self, data):
        """
        Adds a new node containing the specified value
        at the start of the LinkedList
        """
        node = self.LinkedNode(data)
        self._tail.next.prev = node
        node.next = self._tail.next
        node.prev = self._tail
        self._tail.next = node
        self._count += 1

    def append(self, data):
        """
        Adds a new node containing the specified value
        at the end of the LinkedList
        """
        node = self.LinkedNode(data)
        self._head.prev.next = node
        node.prev = self._head.prev
        node.next = self._head
        self._head.prev = node
        self._count += 1

    def contains(self, data):
        """
        Determines whether a value is in the LinkedList
        """
        pointer = self._tail
        while pointer.next != self.head:
            pointer = pointer.next
            if pointer.data == data:
                return True
        return False

    def get(self,index):
        """
        Finds the first node that contains the specified value
        """
        if index >= self._count:
            raise IndexError
        pointer = self._tail
        for num in range(index + 1):
            pointer = pointer.next
        return pointer.data

    def remove_at(self, data):
        """
        Removes the first occurrence of the specified value
        from the LinkedList
        """
        pass

    def remove_first(self):
        """
        Removes the node at the start of the LinkedList
        """
        if self._tail.next == self._head or self._head.prev == self._tail:
            raise Exception("list is empty.")
        removed_node = self._tail.next
        self._tail.next = self._tail.next.next
        self._tail.next.prev = self._tail
        removed_node.prev = None
        removed_node.next = None
        self._count -= 1

    def remove_last(self):
        """
        Removes the node at the end of the LinkedList
        """
        if self._tail.next == self._head or self._head.prev == self._tail:
            raise Exception("list is empty.")
        removed_node = self._head.prev
        self._head.prev = self._head.prev.prev
        self._head.prev.next = self._head
        removed_node.prev = None
        removed_node.next = None
        self._count -= 1

    def clear(self):
        """
        Removes all nodes from the LinkedList
        """
        while self._head.prev != self._tail:
            remove_last(self)


    def count(self):
        """
        Gets the number of nodes actually contained in the LinkedList
        """
        return self._count

    def __iter__(self):
        self._iterhead = self._tail
        return self

    def next(self):
        if self._iterhead.next != self._head:
            self._iterhead = self._iterhead.next
            return self._iterhead.data
        else:
            raise StopIteration

    class LinkedNode(object):
        def __init__(self, data=None):

            self.data = data
            self.next = None
            self.prev = None
