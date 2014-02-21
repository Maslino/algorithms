# coding: utf8
"""
Design a simple LRU cache.
please refer to:
    http://blog.csdn.net/hexinuaa/article/details/6630384
"""
from cache.linked_list import DoubleLinkedList, Node


class LRUCache(object):
    def __init__(self, capacity):
        assert capacity > 0
        self._capacity = capacity
        self._dict = {}
        self._list = DoubleLinkedList()

    def put(self, k, v):
        node = self._dict.get(k)
        if node is not None:
            node.data = (k, v)
            self._list.move2first(node)
        else:
            if self.size() >= self._capacity:
                data = self._list.remove_last()
                self._dict.pop(data[0])
            node = Node((k, v))
            self._list.add_first(node)
            self._dict[k] = node

    def get(self, k):
        node = self._dict.get(k)
        if node is None:
            return None
        else:
            self._list.move2first(node)
            return node.data[1]

    def remove(self, k):
        if k in self._dict:
            node = self._dict.pop(k)
            self._list.remove(node)

    def size(self):
        return len(self._dict)

    def print_cache(self):
        for k, node in self._dict.items():
            print k, "=>", node.data[1],
        print
        self._list.print_list()


if __name__ == "__main__":
    cache = LRUCache(5)
    cache.put(1, "a")
    cache.put(2, "b")
    cache.put(3, "c")
    cache.put(4, "d")
    cache.put(5, "e")
    cache.print_cache()

    cache.put(6, "f")
    cache.print_cache()
    cache.put(5, "g")
    cache.print_cache()

    for i in xrange(1, 7):
        print cache.get(i)
        cache.remove(i)

    cache.print_cache()
