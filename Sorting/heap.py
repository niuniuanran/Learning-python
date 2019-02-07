import random
size = 10000


def build_max_heap(array):
    heap = [0] + array
    for j in range(int(len(array)/2)+1, 0, -1):
        max_heapify(heap, j)
    return heap


def max_heapify(heap, j):
    left = j * 2
    right = j * 2 + 1
    largest = j
    if left <= len(heap) - 1 and heap[left] > heap[j]:
        largest = left
    if right <= len(heap) - 1 and heap[right] > heap[largest]:
        largest = right
    if largest != j:
        heap[j], heap[largest] = heap[largest], heap[j]
        # swap(heap, j, largest)
        max_heapify(heap, largest)


# def swap(array, a, b):
    # temp = array[a]
    # array[a] = array[b]
    # array[b] = temp


def heap_sort(heap):
    sorted_array = [0] * (len(heap)-1)
    for i in range(len(heap)-1, 0, -1):
        heap[1], heap[i] = heap[i], heap[1]
        # swap(heap, 1, i)
        sorted_array[i-1] = heap.pop(i)
        max_heapify(heap, 1)
    return sorted_array


A = [random.randint(1, size * 3) for _ in range(size)]
print(A)

T = build_max_heap(A)
B = heap_sort(T)
print(B)




