def in_place_swap(i_a, i_b):
    i_a = i_a ^ i_b
    i_b = i_a ^ i_b
    i_a = i_a ^ i_b

    return i_a, i_b

def rot_image(ls_mat):
    i_dim = len(ls_mat)
    for i in range(i_dim/2):
        for j in range(i, i_dim - 1 - i):
            # print ls_mat[i][j], ls_mat[j][i_dim - 1 - i]
            # (ls_mat[i][j], ls_mat[j][i_dim - 1 - i]) = in_place_swap(ls_mat[i][j], ls_mat[j][i_dim - 1 - i])
            # print ls_mat[i][j], ls_mat[j][i_dim - 1 - i]
            # in_place_swap(ls_mat[i][j], ls_mat[i_dim - 1 - i][i_dim - 1 - j])
            # in_place_swap(ls_mat[i][j], ls_mat[i_dim - 1 - j][i])
            ls_mat[i][j], ls_mat[j][i_dim - 1 - i] = ls_mat[j][i_dim - 1 - i], ls_mat[i][j]
            ls_mat[i][j], ls_mat[i_dim - 1 - i][i_dim - 1 - j] = ls_mat[i_dim - 1 - i][i_dim - 1 - j], ls_mat[i][j]
            ls_mat[i][j], ls_mat[i_dim - 1 - j][i] = ls_mat[i_dim - 1 - j][i], ls_mat[i][j]
    return ls_mat

def rot_image_test():
    import numpy.random as nprnd
    i_dim = nprnd.randint(1, 10)
    ls_mat = [[nprnd.randint(20) for i in range(i_dim)] for j in range(i_dim)]




