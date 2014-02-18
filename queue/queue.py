# coding: utf8


class Queue(object):
    """
    queue implementation based on python list
    """
    def __init__(self):
        self._list = []

    def enqueue(self, element):
        self._list.append(element)

    def dequeue(self):
        try:
            return self._list.pop(0)
        except IndexError as e:
            return -1

    def is_empty(self):
        return len(self._list) == 0

    def __str__(self):
        return str(self._list)


if __name__ == "__main__":
    q = Queue()
    assert q.is_empty()
    print q

    for i in xrange(10):
        q.enqueue(i)
    assert not q.is_empty()
    print q

    for i in xrange(15):
        print q.dequeue(),
    assert q.is_empty()
    print q
