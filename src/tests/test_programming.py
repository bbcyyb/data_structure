# -*- coding: utf-8 -*-

import unittest
from logger import Logger
from programming.happy_number import HappyNumber


class TestHappyNumber(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.logger = Logger(True)
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.logger.loginfo('This is setUp function')

    def tearDown(self):
        self.logger.loginfo('This a tearDown function')

    def test_is_happy_number(self):
        happy_number = HappyNumber()
        result = happy_number.is_happy_number(91)
        self.assertEqual(result, True)

    def test_is_not_happy_number(self):
        happy_number = HappyNumber()
        result = happy_number.is_happy_number(84)
        self.assertEqual(result, False)

    def test_number_of_happy_number(self):
        happy_number = HappyNumber()
        happy_lst = []
        for item in range(1, 100):
            if happy_number.is_happy_number(item):
                happy_lst.append(item)
        self.assertEqual(len(happy_lst), 19)
