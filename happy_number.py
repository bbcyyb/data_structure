# coding: utf-8


class HappyNumber:
    def __init__(self):
        self._happyNum = {}
        self._unhappyNum = {}

    def happy(self, num):
        current = num
        passed_array = {}

        if self._happyNum.has_key(num):
            return True
        elif self._unhappyNum.has_key(num):
            return False

        while (True):
            split_num = current
            new_num = 0
            digit_array = []
            while (split_num):
                digit_array.append(split_num % 10)
                split_num = split_num / 10
            for digit in digit_array:
                new_num = new_num + (digit * digit)
            if new_num == 1:
                passed_array[current] = True
                for key in passed_array.keys():
                    self._happyNum[key] = True
                return True
            elif passed_array.has_key(current):
                for key in passed_array.keys():
                    self._unhappyNum[key] = True
                return False
            else:
                passed_array[current] = True
                current = new_num
