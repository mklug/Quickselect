import statistics
import random
from median import median
from median import random_partition_slice

# Test ``median`` on arrays of integers.

funcs = [lambda x: x, lambda x: -x, lambda x: x**2 - x + 12]

for func in funcs:
    for _ in range(10000):
        N = random.randint(1, 100)
        A = [random.randint(-N, N) for _ in range(N)]
        median_index = (len(A) - 1) // 2
        med = median(A, func)
        for i, x in enumerate(A):
            if i < median_index:
                assert func(A[i]) <= func(med)
            else:
                assert func(A[i]) >= func(med)


# Test ``median`` on arrays of arrays.

funcs = [lambda x: x[0], lambda x: x[1],
         lambda x: -x[0]**2 - x[1] + 12]

for func in funcs:
    for _ in range(10000):
        N = random.randint(1, 100)
        A = [(random.randint(-N, N), random.randint(-N, N))
             for _ in range(N)]
        median_index = (len(A) - 1) // 2
        med = median(A, func)
        for i, x in enumerate(A):
            if i < median_index:
                assert func(A[i]) <= func(med)
            else:
                assert func(A[i]) >= func(med)


# Test ``random_partition``.

funcs = [lambda x: x, lambda x: -x, lambda x: x**2 - x + 12]

for func in funcs:
    for _ in range(10000):
        N = random.randint(1, 100)
        A = [random.randint(-N, N) for _ in range(N)]
        L = random.randint(0, len(A)-1)
        R = random.randint(L, len(A)-1)
        index = random_partition_slice(A, L, R, func)
        for i in range(L, R+1):
            if i < index:
                assert func(A[i]) < func(A[index])
            else:
                assert func(A[i]) >= func(A[index])

# More tests of the ``median`` function.


def func(x): return x


for _ in range(10000):
    N = random.randint(1, 100)
    A = [random.randint(-N, N) for _ in range(N)]

    # Test ``median`` for odd length arrays.
    N = 2*N + 1
    A = [random.randint(-N, N) for _ in range(N)]
    assert median(A, func) == statistics.median(A)

    # Test ``median`` for even length arrays
    N = 2*random.randint(1, 100)
    A = [random.randint(-N, N) for _ in range(N)]
    assert median(A, func) == sorted(A)[(len(A) - 1) // 2]
