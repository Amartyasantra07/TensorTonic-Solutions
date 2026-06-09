import numpy as np

def matrix_transpose(A):
    n = len(A)      # rows
    m = len(A[0])   # columns

    result = np.empty((m, n))

    for i in range(n):
        for j in range(m):
            result[j, i] = A[i][j]

    return result
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    pass
