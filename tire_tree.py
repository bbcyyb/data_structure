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

    def __init__(self):
        """
        Tire tree data structure
        """
        self._root = self.TireNode()

    def insert(self, word):
        """
        Insert a word into tire tree.
        """
        if not word:
            raise ValueError()
        current_node = self._root
        for index, char in enumerate(word):
            if not current_node.children.get(char):
                new_node = self.TireNode()
                new_node.parent = current_node
                new_node.level = current_node.level + 1
                new_node.value = char
                current_node.children[char] = new_node
            else:
                current_node.children[char].num += 1
            current_node = current_node.children[char]
        current_node.is_end = True

    def delete(self, word):

        leaf = self._get_last_node(word)
        if leaf and leaf.is_end:
            self._delete_node_recursive(leaf)

    def count_words_with_prefix(self, prefix):
        """
        Count words with prefix
        """

        if not prefix:
            return 0

        current_node = self._root
        for index, char in enumerate(prefix):
            if not current_node.children.get(char):
                return 0
            else:
                current_node = current_node.children[char]
        return current_node.num

    def get_words_with_prefix(self, prefix):
        """
        Get works with prefix
        """

        result = []
        if not prefix:
            return result

        current_node = self._root
        for index, char in enumerate(prefix):
            if not current_node.children.get(char):
                return result
            else:
                current_node = current_node.children[char]
        lst = self._preorder_traversal(current_node)
        result = [prefix[:-1] + item for item in lst]
        return result

    def exists(self, word):
        """
        Check if current word exists in tree.
        """

        leaf = self._get_last_node(word)
        return True if leaf and leaf.is_end else False

    def output(self, node=None):
        """
        Traverse whole tree to print each node infomation.
        """

        if not node:
            node = self._root
        print "level: %s value: %s num: %d is_end: %s" % (node.level,
                                                          node.value, node.num,
                                                          node.is_end)
        if len(node.children) > 0:
            for key, value in node.children.items():
                self.output(value)

    def _preorder_traversal(self, node):

        result = []
        if not node:
            return result

        if node.is_end:
            result.extend(node.value)
        for key, value in node.children.items():
            lst = self._preorder_traversal(value)
            result.extend([node.value + item for item in lst])
        return result

    def _delete_node_recursive(self, node):

        if node.level == 0:
            return
        parent = node.parent
        if node.num > 1:
            node.num -= 1
        else:
            parent.children.pop(node.value)
        self._delete_node_recursive(parent)

    def _get_last_node(self, word):
        if not word:
            return None

        current_node = self._root
        for index, char in enumerate(word):
            if not current_node.children.get(char):
                return None
            else:
                current_node = current_node.children[char]
        return current_node

    class TireNode(object):
        """
        Basic tree node.
        """

        def __init__(self):
            self.children = {}
            self.parent = None
            self.level = 0

            # 有多少单词通过这个节点,即由根至该节点组成的字符串模式出现的次数
            self.num = 1
            # 是不是最后一个节点
            self.is_end = False
            # 节点中存的字符
            self.value = None
