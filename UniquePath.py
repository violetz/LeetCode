def unique_path(m, n):
    mat = [[0] * (n + 1) for i in range(m + 1)]
    mat[(m - 1)][n] = 1
    for j in range(n-1, -1, -1):
        for i in range(m-1, -1, -1):
            mat[i][j] = mat[i][j+1] + mat[i+1][j]
            # print i, j, mat[i][j]
    map(lambda x: x.pop(), mat)
    return mat[:m]

class matrix(object):
    def __init__(self, m, n):
        self._nrow = m
        self._ncol = n
        self._mat = [[0] * n for i in range(m)]

    def __repr__(self):
        return str(self._mat)

    def get_item(self, i=0, j=0):
        if 0 <= i < self._nrow and 0 <= j < self._ncol:
            return self._mat[i][j]
        elif i == self._nrow or j == self._ncol:
            return 0
        else:
            raise ValueError('index out of range')

    def set_item(self, i, j, val):
        if 0 <= i < self._nrow and 0 <= j < self._ncol:
            self._mat[i][j] = val
        else:
            raise ValueError('index out of range')

def upath(m, n):
    matx = matrix(m, n)
    matx.set_item(m-1, n-1, 1)
    for i in range(m-2, -1, -1):
        matx.set_item(i, n-1, matx.get_item(i+1, n-1))
    for i in range(m-1, -1, -1):
        for j in range(n-2, -1, -1):
            matx.set_item(i, j, matx.get_item(i+1, j) + matx.get_item(i, j+1))
    return matx.get_item()
