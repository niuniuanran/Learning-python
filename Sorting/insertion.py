import random

size = 10000
A = [random.randint(1, size * 3) for _ in range(size)]
print(A)


for i in range(size):
    for j in range(i, 0, -1):
        if A[j] < A[j-1]:
            temp = A[j-1]
            A[j-1] = A[j]
            A[j] = temp

print(A)



