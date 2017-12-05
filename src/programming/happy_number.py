# coding: utf-8


class HappyNumber:
    def __init__(self):
        self._happy_num = {}
        self._unhappy_num = {}

    def is_happy_number(self, num):
        current = num
        passed_array = {}

        if num in self._happy_num:
            return True
        elif num in self._unhappy_num:
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
                    self._happy_num[key] = True
                return True
            elif current in passed_array:
                for key in passed_array.keys():
                    self._unhappy_num[key] = True
                return False
            else:
                passed_array[current] = True
                current = new_num
