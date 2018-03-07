import time

from numpy import arange

start = time.time()


def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result


a = arange(9).reshape(3, 3)
print("\nPyPy3 version:", sum2d(a))
print("Duration: {} seconds".format(time.time() - start))
