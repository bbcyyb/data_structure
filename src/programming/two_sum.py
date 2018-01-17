# -*- coding:utf8 -*-


class TwoSum(object):
    """
    Given an array of integers, return **indices** of the two numbers
    such that they add up to a specific target.
    You may assume that each input would have **exactly** one solution,
    and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """

    def run(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_a in range(len(nums)):
            for index_b in range(index_a + 1, len(nums)):
                if target == nums[index_a] + nums[index_b]:
                    return [index_a, index_b]
        return []

    def run_obsolete(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pool = {}
        for index_num, num in enumerate(nums):
            for cached, index_p in pool.items():
                if target == cached + num:
                    return [index_p, index_num]
            if num not in pool:
                pool[num] = index_num
        return []
