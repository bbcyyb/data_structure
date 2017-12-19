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
        while pointer.next != self._head:
            pointer = pointer.next
            if pointer.data == data:
                return True
        return False

    def get(self, index):
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
        point = self._tail
        while point.next != self._head:
            point = point.next
            if point.data == data:
                self._remove_node(point)
                return True
        return False


    def remove_first(self):
        """
        Removes the node at the start of the LinkedList
        """
        if self._tail.next == self._head or self._head.prev == self._tail:
            raise Exception("list is empty.")
        removed_node = self._tail.next
        self._remove_node(removed_node)

    def remove_last(self):
        """
        Removes the node at the end of the LinkedList
        """
        if self._tail.next == self._head or self._head.prev == self._tail:
            raise Exception("list is empty.")
        removed_node = self._head.prev
        self._remove_node(removed_node)

    def clear(self):
        """
        Removes all nodes from the LinkedList
        """
        if self._tail.next == self._head and self.count() == 0:
            return
        # fist element, not tail node
        point = self._tail.next
        while point != self._head:
            point = point.next
            self.remove_first()

    def count(self):
        """
        Gets the number of nodes actually contained in the LinkedList
        """
        return self._count

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self._count -= 1

    def __iter__(self):
        self._iterhead = self._tail
        return self

    def __str__(self):
        return '[%s]' % ', '.join(['\'%s\'' % str(item) for item in self]).rstrip()

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
