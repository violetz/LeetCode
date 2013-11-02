def min_path_sum(array_grid):
    if not array_grid or not array_grid[0]:
        return 0
    
    i_tot_row = len(array_grid)
    i_tot_col = len(array_grid[0])
    ls_temp_row = [0] * i_tot_col
    for ind_row in range(i_tot_row):
        if ind_row == 0:
            ls_temp_row[0] = array_grid[0][0]
            for ind_col in range(1, i_tot_col):
                ls_temp_row[ind_col] = (ls_temp_row[ind_col - 1]
                                        + 
                                        array_grid[0][ind_col])
        else:
            ls_temp_row[0] += array_grid[ind_row][0]
            for ind_col in range(1, i_tot_col):
                ls_temp_row[ind_col] = (min(ls_temp_row[ind_col],
                                           ls_temp_row[ind_col - 1]) + 
                                           array_grid[ind_row][ind_col])
    return ls_temp_row[-1]
            
def min_path_sum_test():
    import csv
    with open('MinPathSumTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            array_grid = map(lambda x: map(int, x.split(',')), 
                             row[0].strip('[]').split('],['))
            i_expected = int(row[1])
            i_actual = min_path_sum(array_grid)
            print i_actual
            assert(i_actual == i_expected)

if __name__ == '__main__':
    min_path_sum_test()
