# coding: utf8


class Heap(object):
    def __init__(self, a):
        """
        construct a heap from an array
        """
        self.array = a[:]
        self.size = self.length = len(a)
        self.__construct_heap()

    def parent(self, index):
        """
        return index of parent
        """
        return (index - 1) / 2

    def left(self, index):
        """
        return index of left child
        """
        return index * 2 + 1

    def right(self, index):
        """
        return index of right child
        """
        return index * 2 + 2

    def __construct_heap(self):
        """
        build heap in a bottom up way
        """
        i = self.size / 2 - 1
        while i >= 0:
            self.trickle_down(i)
            i -= 1

    def add(self, element):
        if self.size == self.length:
            self.__extend()

        # add new element to the last position, then bubble up
        self.array[self.size] = element
        self.size += 1
        self.bubble_up(self.size - 1)

    def remove(self):
        if self.size == 0:
            return -1

        temp = self.array[0]
        # move the last element to the root, then trickle down
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.trickle_down(0)

        return temp

    def bubble_up(self, index):
        parent_index = self.parent(index)
        while parent_index >= 0:
            if self.array[parent_index] > self.array[index]:
                self.swap(parent_index, index)

            index = parent_index
            parent_index = self.parent(index)

    def trickle_down(self, index):
        while True:
            left_index = self.left(index)
            right_index = self.right(index)

            if right_index < self.size and self.array[right_index] < self.array[index]:
                if self.array[left_index] < self.array[right_index]:
                    # left index is the smallest
                    next_index = left_index
                else:
                    # right index is the smallest
                    next_index = right_index
            else:
                if left_index < self.size and self.array[left_index] < self.array[index]:
                    next_index = left_index
                else:
                    next_index = -1

            if next_index != -1:
                self.swap(index, next_index)
                index = next_index
            else:
                break

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def __extend(self):
        if self.length == 0:
            self.array = [-1, -1]
            self.length = 2
        else:
            self.array.extend([-1 for _ in xrange(self.length)])
            self.length += self.length

    def __str__(self):
        # todo: better tree representation
        return " ".join([str(self.array[i]) for i in xrange(self.size)])

    def sort(self):
        """
        heap sort: swap the root and the last, then trickle down the root
        """
        while self.size > 1:
            self.swap(0, self.size - 1)
            self.size -= 1
            self.trickle_down(0)

        print " ".join([str(self.array[i]) for i in xrange(self.length)])


def heap_sort(array):
    if len(array) <= 1:
        return

    heap = Heap(array)
    heap.sort()


if __name__ == "__main__":
    import random

    for limit in xrange(20):
        array = [random.randint(0, 100) for i in xrange(limit)]
        heap_sort(array)