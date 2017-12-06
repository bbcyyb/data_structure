# coding: utf-8
# from structure.tire_tree import TireTree
from programming.happy_number import HappyNumber
from logger import Logger

if __name__ == "__main__":

    logger = Logger(True)

    happy_lst = []
    unhappy_lst = []
    entity = HappyNumber()
    for num in range(1, 100):
        if entity.is_happy_number(num):
            happy_lst.append(num)
        else:
            unhappy_lst.append(num)
    logger.loginfo('happy list is %s\n' % happy_lst)
    print '============================='
    print 'unhappy list is ', unhappy_lst
    """
    tire = TireTree()
    tire.insert('hello')
    tire.insert('world')
    tire.insert('helloW')
    tire.insert('wow')
    tire.insert('head')
    lst = tire.get_all_words()
    print lst
    tire.output()
    tire.delete('wow')
    tire.output()
    print tire.count_words_with_prefix('hel')
    print tire.count_words_with_prefix('wo')
    print tire.get_words_with_prefix('hel')
    print tire.get_words_with_prefix('wo')
    print tire.exists('helloW')
    """
