# coding: utf-8


class LinkedList(object):
    def __init__(self):
        self._head = LinkedNode()
        self._tail = LinkedNode()
        self._head.prev = self._tail
        self._tail.next = self._head

    def add_first(self, data):
        """
        Adds a new node containing the specified value
        at the start of the LinkedList
        """
        node = LinkedNode(data)
        self._tail.next.prev = node
        node.next = self._tail.next
        node.prev = self._tail
        self._tail.next = node

    def add_last(self, data):
        """
        Adds a new node containing the specified value
        at the end of the LinkedList
        """
        node = LinkedNode(data)
        self._head.prev.next = node
        node.prev = self._head.prev
        node.next = self._head
        self._head.prev = node

    def contains(self, data):
        """
        Determines whether a value is in the LinkedList
        """
        pass

    def find(self):
        """
        Finds the first node that contains the specified value
        """
        pass

    def find_last(self):
        """
        Finds the last node that contains the specified value
        """
        pass

    def remove(self, data):
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


    def remove_all(self):
        """
        Removes all nodes from the LinkedList
        """
        pass

    def count(self):
        """
        Gets the number of nodes actually contained in the LinkedList
        """
        pass

    class LinkedNode(object):
        def __init__(self, data=None):

            self.data = data
            self.next = None
            self.prev = None
