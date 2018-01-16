class TwoSum(object):
    def run(self, nums, target):
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
