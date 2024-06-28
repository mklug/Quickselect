import random


def random_partition_slice(A, L, R, func=lambda x: x):
    '''
    Randomly selects a random index k in [L..R]
    and permutes the entries of A[L..R] so that 
    all entries less than A[k] come before. 
    Returns the index where A[k] is moved to.  

    Optional ``func`` parameter to apply a
    function to the entries to determine their
    order.  
    '''
    if L == R:
        return L
    pivot_index = random.randint(L, R)
    pivot_value = func(A[pivot_index])
    A[pivot_index], A[R] = A[R], A[pivot_index]
    store_index = L
    for i in range(L, R):
        if func(A[i]) < pivot_value:
            A[store_index], A[i] = A[i], A[store_index]
            store_index += 1
    A[R], A[store_index] = A[store_index], A[R]
    return store_index


def quick_select_slice(A, L, R, i, func=lambda x: x):
    '''
    Returns the i-th order element in A[L..R].
    Moves this entry to index i and moves all
    entries in A[L..R] that are smaller than
    it have smaller index.  0 <= i <= len(A)-1.

    Optional ``func`` parameter to apply a
    function to the entries to determine their
    order.  
    '''
    while True:
        if L == R:
            return A[L]
        pivot_index = random_partition_slice(A, L, R, func)
        if i == pivot_index:
            return A[i]
        elif i < pivot_index:
            R = pivot_index - 1
        else:
            L = pivot_index + 1


def random_partition(A, func=lambda x: x):
    '''
    Randomly selects a random index k in 
    [0..len(A)-1] and permutes the entries of A
    so that all entries less than A[k] come before. 
    Returns the index where A[k] is moved to.  

    Optional ``func`` parameter to apply a
    function to the entries to determine their
    order.  
    '''
    return random_partition_slice(A, 0, len(A)-1, func)


def median(A, func=lambda x: x):
    '''
    Returns the median of A.  If A has even length,
    returns the order statistic with order 
    (len(A) - 1) // 2 (where we start counting at 0).
    Modifies A to move this entry to the middle 
    position and all entries smaller than it to its
    left.  

    Optional ``func`` parameter to apply a
    function to the entries to determine their
    order.  
    '''
    median_index = (len(A) - 1) // 2
    return quick_select_slice(A, 0, len(A)-1, median_index, func)


def quick_select(A, i, func=lambda x: x):
    '''
    Returns the i-th order element in A.
    Moves this entry to index i and moves all
    entries in A that are smaller than
    it have smaller index.  0 <= i <= len(A)-1.

    Optional ``func`` parameter to apply a
    function to the entries to determine their
    order.  
    '''
    return quick_select_slice(A, 0, len(A)-1, i. func)
