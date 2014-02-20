# coding: utf8
"""
Simulation of buddy memory management.
please refer to:
    http://www.cs.fsu.edu/~engelen/courses/COP402003/p827.pdf
    https://github.com/cloudwu/buddy/blob/master/buddy.c
"""


class Buddy(object):

    UNUSED, USED, SPLIT = xrange(3)

    def __init__(self, l, u):
        assert 0 < l < u

        self.lower = l
        self.upper = u
        # 使用满二叉树表示分配状态
        self.states = [Buddy.UNUSED] * (2 ** (u - l + 1) - 1)
        self.map = {}
        for i in xrange(u - l + 1):
            for j in xrange(2 ** i - 1, 2 ** (i + 1) - 1):
                self.map[j] = 2 ** (u - i)

        assert len(self.states) == len(self.map)

    @staticmethod
    def is_pow_of_2(n):
        return n >= 1 and (not (n & (n - 1)))

    @staticmethod
    def next_pow_of_2(n):
        if Buddy.is_pow_of_2(n):
            return n
        if n <= 2:
            return n

        # todo: use bit operation
        p = 2
        while p < n:
            p *= 2
        return p

    def __parent(self, index):
        return (index - 1) / 2

    def __lchild(self, index):
        return 2 * index + 1

    def __rchild(self, index):
        return 2 * index + 2

    def __buddy(self, index):
        # there is no buddy for zero index
        assert index > 0
        return ((index + 1) ^ 1) - 1

    def __length(self, index):
        assert 0 <= index < 2 ** (self.upper - self.lower + 1)
        return self.map[index]

    def __index2level(self, index):
        if index == 0:
            return 0
        if index == 1 or index == 2:
            return 1

        return self.__index2level(self.__parent(index)) + 1

    def __index2offset(self, index):
        level = self.__index2level(index)
        # 对某一level来说，所有偏移从小到大分别为：
        # 0, 2^(upper-level) * 1, 2^(upper-level) * 2, ..., 2^(upper-level) * (2^level-1)
        return 2 ** (self.upper - level) * (index - (2 ** level - 1))

    def __offset2index(self, offset):
        index = 0
        left = 0
        length = 2 ** self.upper
        while True:
            if self.states[index] == Buddy.USED:
                return index
            else:
                length /= 2
                if offset < left + length:
                    index = self.__lchild(index)
                else:
                    left += length
                    index = self.__rchild(index)

    def alloc(self, size):
        assert size > 0
        norm_size = self.next_pow_of_2(size)
        index = self.__allocate(norm_size, 0)
        return self.__index2offset(index) if index >= 0 else index

    def __allocate(self, norm_size, index):
        if norm_size < 2 ** self.lower or norm_size > 2 ** self.upper:
            return -1

        if self.__length(index) == norm_size:
            if self.states[index] == Buddy.UNUSED:
                self.states[index] = Buddy.USED
                return index
            else:
                return -1
        else:
            if self.states[index] == Buddy.USED:
                return -1
            else:
                lchild_index = self.__lchild(index)
                rchild_index = self.__rchild(index)
                if self.states[index] == Buddy.UNUSED:
                    self.states[index] = Buddy.SPLIT
                    self.states[lchild_index] = Buddy.UNUSED
                    self.states[rchild_index] = Buddy.UNUSED
                    return self.__allocate(norm_size, lchild_index)
                elif self.states[index] == Buddy.SPLIT:
                    result = self.__allocate(norm_size, lchild_index)
                    return result if result >= 0 else self.__allocate(norm_size, rchild_index)

    def free(self, offset):
        index = self.__offset2index(offset)
        while index > 0:
            self.states[index] = Buddy.UNUSED
            buddy_index = self.__buddy(index)
            parent_index = self.__parent(index)
            if self.states[buddy_index] == Buddy.UNUSED:
                self.states[parent_index] = Buddy.UNUSED
                index = parent_index
            else:
                break

    def size(self, offset):
        index = self.__offset2index(offset)
        return self.map[index]

    def print_state(self):
        # todo: better representation
        print self.states


if __name__ == "__main__":
    buddy = Buddy(6, 10)
    buddy.print_state()

    offset_a = buddy.alloc(70)
    print offset_a, buddy.size(offset_a)
    buddy.print_state()

    offset_b = buddy.alloc(35)
    print offset_b, buddy.size(offset_b)
    buddy.print_state()

    offset_c = buddy.alloc(80)
    print offset_c, buddy.size(offset_c)
    buddy.print_state()

    buddy.free(offset_a)
    buddy.print_state()

    offset_d = buddy.alloc(60)
    print offset_d, buddy.size(offset_d)
    buddy.print_state()

    buddy.free(offset_b)
    buddy.print_state()

    buddy.free(offset_d)
    buddy.print_state()

    buddy.free(offset_c)
    buddy.print_state()
