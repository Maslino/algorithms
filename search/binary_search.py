# coding=utf8


def binary_search(array, length, value):
    low = 0
    high = length - 1

    while low <= high:
        mid = low + (high - low) / 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def binary_search_lowest(array, length, value):
    """ find the smallest index that array[index] == value
    """
    low = 0
    high = length - 1

    while low < high:
        mid = low + (high - low) / 2
        if array[mid] < value:
            low = mid + 1
        else:
            high = mid

    assert low == high
    if array[high] == value:
        return high

    return -1


if __name__ == "__main__":
    import random
    data = [random.randint(1, 20) for i in xrange(20)]
    s = sorted(data)
    print s
    for i in s:
        print binary_search_lowest(s, len(s), i),
    print binary_search_lowest(s, len(s), -1)