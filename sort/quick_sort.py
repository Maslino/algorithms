# coding:utf8


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def quick_sort(array, low, high):
    if low >= high:
        return

    pivot = array[low]
    i = low
    j = high + 1

    while True:
        while True:
            i += 1
            if i > high or array[i] >= pivot:
                break
        while True:
            j -= 1
            if array[j] <= pivot:
                break
        if i > j:
            break
        swap(array, i, j)

    swap(array, low, j)
    quick_sort(array, low, j - 1)
    quick_sort(array, j + 1, high)


if __name__ == "__main__":
    import sys
    import random

    for limit in xrange(1000):
        array = [random.randint(0, sys.maxint) for i in xrange(limit)]
        array_copy = array[:]
        quick_sort(array, 0, len(array) - 1)
        assert array == sorted(array_copy)
