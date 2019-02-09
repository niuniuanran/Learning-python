import bisect
from random import randint


def binary_sort(array):
    sortedarray = []
    for num in array:
        bisect.insort_left(sortedarray, num)
    return sortedarray


def binary_locate_and_insert(array):
    sortedarray = []
    for num in array:
        i = bisect.bisect_left(sortedarray, num)
        sortedarray.insert(i, num)
    return sortedarray


def test():
    A = [randint(1, 50) for _ in range(15)]
    B = [randint(1, 50) for _ in range(15)]

    print(A)
    print(binary_sort(A))
    print(B)
    print(binary_locate_and_insert(B))


if __name__ == '__main__':
    test()