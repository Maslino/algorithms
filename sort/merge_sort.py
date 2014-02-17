# coding: utf8


def merge(a, b, c):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1


def merge_sort(array):
    """
    这种实现方式的空间复杂度不是O(n)
    """
    if len(array) <= 1:
        return

    mid = len(array) / 2
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, array)


if __name__ == "__main__":
    import sys
    import random

    for limit in xrange(1000):
        array = [random.randint(0, sys.maxint) for i in xrange(limit)]
        array_copy = array[:]
        merge_sort(array)
        assert array == sorted(array_copy)
