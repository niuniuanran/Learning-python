import numpy as np
size = 10000


def merge(array1, array2):
    p1 = 0
    p2 = 0
    p = 0
    array = [0] * (len(array1) + len(array2))

    while p1 < len(array1) and p2 < len(array2):
        if array1[p1] < array2[p2]:
            array[p] = array1[p1]
            p1 += 1
        else:
            array[p] = array2[p2]
            p2 += 1
        p += 1

    while p1 < len(array1):
        array[p] = array1[p1]
        p += 1
        p1 += 1

    while p2 < len(array2):
        array[p] = array2[p2]
        p += 1
        p2 += 1

    return array


def merge_sort(array):
    length = len(array)
    if length == 1:
        return array
    else:
        array1 = merge_sort(array[:int(length/2)])
        array2 = merge_sort(array[int(length/2):])
        new_array = merge(array1, array2)
        return new_array


A = np.random.randint(0, 3 * size, size)

print(A)
print(merge_sort(A))



