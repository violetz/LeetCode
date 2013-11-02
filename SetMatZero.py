def SetMatZero(mat):
    m = len(mat)
    n = len(mat[0])
    col_flag = 0
    row_flag = 0
    for i in range(m):
        if mat[i][0] == 0:
            col_flag = 1
            break
    for j in range(n):
        if mat[0][j] == 0:
            row_flag = 1
            break
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                mat[0][j] = 0
                mat[i][0] = 0
                # print i, j, mat
    for i in range(1, m):
        if mat[i][0] == 0:
            mat[i] = [0 for j in range(n)]
            # print mat
    for j in range(1, n):
        if mat[0][j] == 0:
            for i in range(m):
                mat[i][j] = 0
                # print mat
    if row_flag:
        mat[0] = [0 for j in range(n)]
    if col_flag:
        for i in range(m):
            mat[i][0] = 0
    return

def DirectSetZero(mat):
    m = len(mat)
    n = len(mat[0])
    set_row = set()
    set_col = set()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                set_row.add(i)
                set_col.add(j)
    for i in set_row:
        mat[i] = [0 for j in range(n)]
    for j in set_col:
        for i in range(m):
            mat[i][j] = 0
    return

def SetMatZeroTest():
    import numpy.random as nprnd
    import copy
    for i_test in range(1000):
        m = nprnd.randint(10)
        n = nprnd.randint(10)
        if m == 0 or n == 0:
            continue
        mat = [[0] * n for i in range(m)]
        i_zeros = nprnd.randint(m * n / 2 + 1)
        ls_mat = list(nprnd.randint(10, size = m * n - i_zeros)) + [0] * i_zeros
        nprnd.shuffle(ls_mat)
        for i in range(m):
            for j in range(n):
                mat[i][j] = ls_mat[i * n + j]
        mat_cp = copy.deepcopy(mat)
        print mat
        SetMatZero(mat)
        DirectSetZero(mat_cp)
        print mat, 1, mat_cp
        assert(mat == mat_cp)
    return

if __name__ == '__main__':
    SetMatZeroTest()
    #assert(False)
