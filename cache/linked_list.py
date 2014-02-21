# coding: utf8
"""
double linked list implementation
"""


class Node(object):
    def __init__(self, data, p=None, n=None):
        self._data = data
        self._prev = p
        self._next = n

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def p(self):
        return self._prev

    @p.setter
    def p(self, p):
        self._prev = p

    @property
    def n(self):
        return self._next

    @n.setter
    def n(self, n):
        self._next = n

    def __str__(self):
        return str(self._data)


class DoubleLinkedList(object):
    def __init__(self):
        self._head = Node("head")
        self._tail = Node("tail")
        self._head.n = self._tail
        self._tail.p = self._head

    def add_last(self, node):
        t = self._tail.p
        t.n = node
        self._tail.p = node
        node.n = self._tail
        node.p = t

    def add_first(self, node):
        t = self._head.n
        self._head.n = node
        t.p = node
        node.n = t
        node.p = self._head

    def remove_first(self):
        if self.is_empty():
            return Node

        t = self._head.n
        self._head.n = t.n
        t.n.p = self._head

        return t.data

    def remove_last(self):
        if self.is_empty():
            return None

        t = self._tail.p
        t.p.n = self._tail
        self._tail.p = t.p

        return t.data

    def remove(self, node):
        _p = node.p
        _n = node.n
        _p.n = _n
        _n.p = _p

    def move2first(self, node):
        self.remove(node)
        self.add_first(node)

    def is_empty(self):
        return self._head.n == self._tail

    def print_list(self):
        node = self._head
        while node.n is not None:
            print node, "<=>",
            node = node.n
        print node


if __name__ == "__main__":
    l = DoubleLinkedList()
    l.print_list()
    l.add_first(Node(8))
    l.print_list()
    node_5 = Node(5)
    l.add_last(node_5)
    l.print_list()
    l.add_last(Node(3))
    l.print_list()
    print l.remove_last()
    l.print_list()
    print l.remove_first()
    l.print_list()

    node = Node(-1)
    l.add_first(node)
    l.print_list()

    l.move2first(node_5)
    l.print_list()

    l.remove(node)
    l.print_list()
