# coding: utf-8
from tree.tire_tree import TireTree
from happy_number import HappyNumber

if __name__ == "__main__":

    happy_lst = []
    unhappy_lst = []
    entity = HappyNumber()
    for num in range(1,1000):
        if entity.happy(num):
            happy_lst.append(num)
        else:
            unhappy_lst.append(num)
    print 'happy list is ', happy_lst
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
