import numpy as np
com_count = 0
size = 10000


def bin_locate(array, num):
    # to operate on a variable in a function without making it a local variable, declare "global" at the beginning.
    global com_count
    #   find a j so that array[i] > array[j-1] and array[i] < array[j], or array
    #   array[0:i-1] is a sorted increasing array.
    #   when you iterate into a new array, the size changes and the position of num in the array changes.
    array_end = len(array) - 1
    mid = int(array_end/2)

    if array_end == 0:
        return 0
    if array[mid] < num:
        if array[mid+1] >= num:
            return mid + 1
        else:
            return bin_locate(array[mid+1:array_end+1], num) + mid + 1
        # 递归中注意离开每一层函数之后返回的值在其外层的函数中如何使用。
        # A[1:3]表示的数列是 [A[1], A[2]]
        # range(1,3)表示的数列是 [1,2]
    elif array[mid] > num:
        if array[mid-1] <= num:
            return mid
        else:
            return bin_locate(array[0:mid+1], num)
    else:
        return mid


A = np.random.randint(1, size * 3, size)
print(A)

for i in range(1, size):
    n = bin_locate(A[0:i+1], A[i])
    if n == i:
        continue
    else:
        temp1 = A[n]
        A[n] = A[i]
        for j in range(n+1, i+1, 2):
            temp2 = A[j]
            A[j] = temp1
            if j+1 > i:
                break
            else:
                temp1 = A[j+1]
                A[j+1] = temp2


print(A)
print(com_count)


