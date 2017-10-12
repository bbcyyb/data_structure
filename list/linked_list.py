# coding: utf-8


class LinkedList(object):
    def __init__(self):

        self._head = None

    def append(self, value):

        node = self.LinkedNode(value)
        self._head = node

    class LinkedNode(object):
        def __init__(self, data):

            self.data = data
            self.next = None

        def add_first(self, data):
            """
            Adds a new node containing the specified value
            at the start of the LinkedList
            """
            pass

        def add_last(self, data):
            """
            Adds a new node containing the specified value
            at the end of the LinkedList
            """
            pass

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
            pass

        def remove_last(self):
            """
            Removes the node at the end of the LinkedList
            """
            pass

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
