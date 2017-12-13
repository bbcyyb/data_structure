# -*- coding: utf-8 -*-

import unittest
from logger import Logger
from structure.linked_list import LinkedList


class TestStructure(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.logger = Logger(True)
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        sample1 = 'abcde'
        sample2 = 12345
        sample3 = True
        self.lst = LinkedList()
        self.lst.append(sample1)
        self.lst.append(sample2)
        self.lst.append(sample3)

    def tearDown(self):
        pass

    def test_append_3_item(self):
        self.assertEqual(self.lst.count(), 3)

    def test_get_data_by_index1(self):
        result = self.lst.get(1)
        result2 = self.lst.get(2)
        self.assertEqual(result, 12345)
        self.assertEqual(result2, True)

    def test_remove_first_data(self):
        self.lst.remove_first()
        result = self.lst.get(0)
        self.assertEqual(result, 12345)
