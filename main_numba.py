import time

from numba import jit
from numpy import arange

start = time.time()


# jit decorator tells Numba to compile this function.
# The argument types will be inferred by Numba when function is called.
@jit
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result


a = arange(9).reshape(3, 3)
print("\nNumba version:", sum2d(a))
print("Duration: {} seconds".format(time.time() - start))

start_python = time.time()


def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result


a = arange(9).reshape(3, 3)
print("\nPlain Python 3.6.4 version:", sum2d(a))
print("Duration: {} seconds".format(time.time() - start_python))
