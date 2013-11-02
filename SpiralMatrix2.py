import csv

def generate_spiral(i_n):
    ls_mat = [[0] * i_n for i in range(i_n)]
    ind_toprow = 0
    ind_botrow = i_n -1
    i_start = 1

    while ind_toprow < ind_botrow:
        for j in range(ind_toprow, ind_botrow):
            ls_mat[ind_toprow][j] = i_start
            i_start += 1
        for i in range(ind_toprow, ind_botrow):
            ls_mat[i][ind_botrow] = i_start
            i_start += 1
        for j in range(ind_botrow, ind_toprow, -1):
            ls_mat[ind_botrow][j] = i_start
            i_start += 1
        for i in range(ind_botrow, ind_toprow, -1):
            ls_mat[i][ind_toprow] = i_start
            i_start += 1
        ind_toprow += 1
        ind_botrow -= 1

    if ind_toprow == ind_botrow:
        ls_mat[ind_toprow][ind_toprow] = i_start

    return ls_mat

def generate_spiral_test():
    with open('SpiralMatrix2Test.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            assert(generate_spiral(int(row[0])) == eval(row[1]))

if __name__ == '__main__':
    generate_spiral_test()
