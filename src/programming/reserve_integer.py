# -*- coding:utf8 -*-


class ReserveInteger(object):
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
    Input: 123
    Output:  321

    Example 2:
    Input: -123
    Output: -321

    Example 3:
    Input: 120
    Output: 21
    """

    def run(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x = x * -1
        arr = []
        arr.append(x % 10)
        x = x / 10
        while x != 0:
            arr = [i * 10 for i in arr]
            arr.append(x % 10)
            x = x / 10

        result = sum(arr) * (-1 if negative else 1)
        if result < -2147483648 or result > 2147483647:
            result = 0
        return result
