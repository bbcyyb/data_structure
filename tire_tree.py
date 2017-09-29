# coding: utf-8

class TireTree(object):

    """
    1. _xx 以单下划线开头的表示的是protected类型的变量。
    即保护类型只能允许其本身与子类进行访问。
    若内部变量标示，如： 当使用“from M import”时，不会将以一个下划线开头的对象引入。
    2.__xx 双下划线的表示的是私有类型的变量。
    只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），
    调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）
    3.__xx__定义的是特列方法。
    用户控制的命名空间内的变量或是属性，如init , __import__或是file 。
    只有当文档有说明时使用，不要自己定义这类变量。 
    （就是说这些是python内部定义的变量名）
    """
    class TireNode(object):
        def __init__(self):
            self.children = {}

            #有多少单词通过这个节点,即由根至该节点组成的字符串模式出现的次数
            self.num = 1
            #是不是最后一个节点
            self.isEnd = False
            #节点中存的字符
            self.value = value 


    """
    Tire tree data structure 
    """
    def __init__(self):
        self._root = self.TireNode()

    def output(self):
        node = self.TireNode()
        return 'hello world ' + node.test()

    def insert(self, word):
        if not word:
            raise ValueError()
        current_node = self._root
        for index, char in enumerate(word):
            if not self._children.get(char):
                new_node = self.TireNode()
                new_node.value = char
                self._children[char] = new_node
            else:
                self._children[char].num += 1

