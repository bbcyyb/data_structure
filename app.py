# coding: utf-8
from tire_tree import TireTree

if __name__ == "__main__":
    tire = TireTree()
    tire.insert('hello')
    tire.insert('world')
    tire.insert('helloW')
    tire.insert('wow')
    tire.insert('head')
    lst = tire.get_all_words()
    print lst
    """
    tire.output()
    tire.delete('wow')
    tire.output()
    print tire.count_words_with_prefix('hel')
    print tire.count_words_with_prefix('wo')
    print tire.get_words_with_prefix('hel')
    print tire.get_words_with_prefix('wo')
    print tire.exists('helloW')
    """
