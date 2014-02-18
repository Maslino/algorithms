# coding: utf8


class Stack(object):
    """
    stack implementation based on python list
    """
    def __init__(self):
        self._list = []

    def push(self, element):
        self._list.append(element)

    def pop(self):
        try:
            return self._list.pop()
        except IndexError as e:
            return -1

    def top(self):
        try:
            return self._list[-1]
        except IndexError:
            return -1

    def is_empty(self):
        return len(self._list) == 0

    def __str__(self):
        return str(self._list)


if __name__ == "__main__":
    stack = Stack()
    print stack
    assert stack.is_empty()

    for i in xrange(10):
        stack.push(i)
    print stack
    assert not stack.is_empty()
    print stack.top()

    for i in xrange(15):
        print stack.pop(),
    assert stack.is_empty()

    print stack.top()
