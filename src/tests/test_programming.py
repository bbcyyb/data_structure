# -*- coding: utf-8 -*-

import unittest
from logger import Logger
from programming.happy_number import HappyNumber
from programming.two_sum import TwoSum
from programming.reserve_integer import ReserveInteger


class TestHappyNumber(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.logger = Logger(True)
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

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

    def test_exists_two_sum(self):
        instance = TwoSum()
        nums = [3, 2, 4]
        target = 6
        result = instance.run(nums, target)
        self.assertListEqual(result, [1, 2])

    def test_not_exists_two_sum(self):
        instance = TwoSum()
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 30, 1, 44, 5325]
        target = 20
        result = instance.run(nums, target)
        self.assertListEqual(result, [])

    def test_reserve_positive(self):
        instance = ReserveInteger()
        result = instance.run(54321)
        self.assertEqual(result, 12345)

    def test_reserve_negative(self):
        instance = ReserveInteger()
        result = instance.run(-12345)
        self.assertEqual(result, -54321)

    def test_reserve_postfix_zero(self):
        instance = ReserveInteger()
        result = instance.run(13010)
        self.assertEqual(result, 1031)
