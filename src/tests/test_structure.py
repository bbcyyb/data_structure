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

    def test_insert_data(self):
        self.lst.insert(9999)
        result = self.lst.get(0)
        self.assertEqual(result, 9999)
        self.assertEqual(self.lst.count(), 4)

    def test_contains_specified_data(self):
        self.assertTrue(self.lst.contains('abcde'))
        self.assertFalse(self.lst.contains('xyz'))
        self.lst.append('xyz')
        self.assertTrue(self.lst.contains('xyz'))

    def test_remove_at(self):
        self.lst.remove_at(12345)
        self.assertEqual(self.lst.count(), 2)
        self.assertFalse(self.lst.contains(12345))

    def test_remove_first(self):
        self.assertEqual(self.lst.get(0), 'abcde')
        self.lst.remove_first()
        self.assertEqual(self.lst.get(0), 12345)
        self.assertEqual(self.lst.count(), 2)

    def test_remove_last(self):
        self.assertEqual(self.lst.get(2), True)
        self.lst.remove_last()
        self.assertEqual(self.lst.count(), 2)
        self.assertEqual(self.lst.get(self.lst.count() - 1), 12345)

    def test_clear(self):
        self.assertEqual(self.lst.count(), 3)
        self.lst.clear()
        self.assertEqual(self.lst.count(), 0)
