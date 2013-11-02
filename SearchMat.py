def IndexToValue(mat, ind):
    m = len(mat)
    n = len(mat[0])
    i = ind / n
    j = ind % n
    return mat[i][j]

def SearchMat(mat, i_key, ind_s, ind_e):
    if ind_s >= ind_e:
        return False
    ind_c = (ind_s + ind_e) / 2
    i_c = IndexToValue(mat, ind_c)
    if i_c == i_key:
        return True
    if i_c < i_key:
        return SearchMat(mat, i_key, ind_c + 1, ind_e)
    if i_c > i_key:
        return SearchMat(mat, i_key, ind_s, ind_c)

def DirectSearch(ls_mat, i_key):
    try:
        i_pos = ls_mat.index(i_key)
        return True
    except ValueError:
        return False
    
def SearchMatTest():
    import numpy.random as nprnd
    for i_test in range(1000):
        m = nprnd.randint(10)
        n = nprnd.randint(10)
        if m == 0 or n == 0:
            continue
        mat = [[0] * n for i in range(m)]
        ls_mat = list(nprnd.randint(40, size = m * n))
        ls_mat.sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = ls_mat[i * n + j]
        i_key1 = ls_mat[nprnd.randint(m*n)]
        i_key2 = nprnd.randint(50)
        print mat, i_key1, i_key2, SearchMat(mat, i_key1, 0, m*n), SearchMat(mat, i_key2, 0, m*n)
        assert(SearchMat(mat, i_key1, 0, m*n) == DirectSearch(ls_mat, i_key1))
        assert(SearchMat(mat, i_key2, 0, m*n) == DirectSearch(ls_mat, i_key2))

if __name__ == '__main__':
    SearchMatTest()
