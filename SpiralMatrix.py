import csv

def spiral(ls_mat):
    i_nrow = len(ls_mat)
    i_ncol = len(ls_mat[0])
    ls_spiral = []
    get_spiral(ls_mat, 0, i_nrow - 1, 0, i_ncol - 1, ls_spiral)
    return ls_spiral

def get_spiral(ls_mat, ind_uprow, ind_downrow, ind_leftcol, ind_rightcol, ls_spiral):
    if ind_uprow > ind_downrow or ind_leftcol > ind_rightcol:
        return
    if ind_uprow == ind_downrow:
        for j in range(ind_leftcol, ind_rightcol + 1):
            ls_spiral.append(ls_mat[ind_uprow][j])
        return
    if ind_leftcol == ind_rightcol:
        for i in range(ind_uprow, ind_downrow + 1):
            ls_spiral.append(ls_mat[i][ind_leftcol])
        return
    for j in range(ind_leftcol, ind_rightcol):
        ls_spiral.append(ls_mat[ind_uprow][j])
    for i in range(ind_uprow, ind_downrow):
        ls_spiral.append(ls_mat[i][ind_rightcol])
    for j in range(ind_rightcol, ind_leftcol, -1):
        ls_spiral.append(ls_mat[ind_downrow][j])
    for i in range(ind_downrow, ind_uprow, -1):
        ls_spiral.append(ls_mat[i][ind_leftcol])
    get_spiral(ls_mat, ind_uprow + 1, ind_downrow - 1,
               ind_leftcol + 1, ind_rightcol - 1, ls_spiral)

    return
    
def spiral_test():
    with open('SpiralMatrixTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_mat = eval(row[0])
            assert(spiral(ls_mat) == eval(row[1]))

if __name__ == '__main__':
    spiral_test()
