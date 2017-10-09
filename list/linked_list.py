# coding: utf-8


class LinkedList(object):

    def __init__(self):

        self._head = None

    def append(self, value):

        node = self.LinkedNode(value);
        self._head = node

    class LinkedNode(object):

        def __init__(self, value):

            self.data = value
            self.next = None
