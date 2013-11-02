def min_path_rec(ls_triangle):
    if len(ls_triangle) == 1 and len(ls_triangle[0]) == 1:
        return ls_triangle[0][0]
    ls_left_triangle = [row[:-1] for row in ls_triangle[1:]]
    ls_right_triangle = [row[1:] for row in ls_triangle[1:]]
    
    return min(min_path_rec(ls_left_triangle), 
               min_path_rec(ls_right_triangle)) + ls_triangle[0][0]

def min_path_iter(ls_triangle):
    import copy
    i_nrow = len(ls_triangle)
    ls_min_path = copy.copy(ls_triangle[-1])
    for ind_row in reversed(range(i_nrow - 1)):
        print ind_row, ls_min_path
        ls_min_path = [ls_triangle[ind_row][i] + 
                       min(ls_min_path[i], ls_min_path[i+1])
                       for i in range(ind_row + 1)]

    return ls_min_path[0]

def min_path_iter_test():
    import csv
    with open('TriangleTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ls_triangle = map(lambda x: map(int, x.split(',')), 
                              row[0].strip('[]').split('],['))
            i_expected = int(row[1])
            i_actual = min_path_iter(ls_triangle)
            print i_actual
            assert(i_actual == i_expected)

if __name__ == '__main__':
    min_path_iter_test()
