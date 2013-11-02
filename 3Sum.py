def three_sum(ls_ints):
    ls_ints.sort()
    set_sol = set()
    len_ints = len(ls_ints)
    for ind_s in range(len_ints - 2):
        ind_m = ind_s + 1
        ind_l = len_ints - 1
        while ind_m < ind_l:
            if ls_ints[ind_m] + ls_ints[ind_l] == -ls_ints[ind_s]:
                set_sol.add((ls_ints[ind_s], ls_ints[ind_m], ls_ints[ind_l]))
                ind_m += 1
                ind_l -= 1
            elif ls_ints[ind_m] + ls_ints[ind_l] < -ls_ints[ind_s]:
                ind_m += 1
            else:
                ind_l -= 1

    return set_sol

def three_sum_no_set(ls_ints):
    ls_ints.sort()
    ls_sol = []
    len_ints = len(ls_ints)
    i_pre_s = 1
    i_pre_m = -1
    i_pre_l = -1
    for ind_s in range(len_ints - 2):
        i_cur_s = ls_ints[ind_s]
        if i_cur_s == i_pre_s:
            continue
        ind_m = ind_s + 1
        ind_l = len_ints - 1
        while ind_m < ind_l:
            i_cur_m = ls_ints[ind_m]
            i_cur_l = ls_ints[ind_l]
            if i_cur_m + i_cur_l == -i_cur_s:
                # print '*', ind_s, ind_m, ind_l, i_pre_s, i_pre_m, i_pre_l
                if i_cur_m != i_pre_m or i_cur_l != i_pre_l:
                    ls_sol.append([i_cur_s, i_cur_m, i_cur_l])
                    i_pre_s, i_pre_m, i_pre_l = i_cur_s, i_cur_m, i_cur_l
                ind_m += 1
                ind_l -= 1
            elif i_cur_m + i_cur_l < -ls_ints[ind_s]:
                ind_m += 1
            else:
                ind_l -= 1
                # print i_pre_s, i_pre_m, i_pre_l

    return ls_sol
    
def three_sum_test():
    import csv
    with open('3SumTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ls_ints = eval(row[0])
            set_expected = set(map(tuple, eval(row[1])))
            set_actual = three_sum(ls_ints)
            ls_actual = three_sum_no_set(ls_ints)
            print row, len(ls_actual)
            assert(len(ls_actual) == len(set_expected))
            assert(set_expected == set(map(tuple, ls_actual)))

def three_sum_closest(ls_ints, i_target):
    ls_ints.sort()
    len_ints = len(ls_ints)
    ls_sol = []
    for ind_s in range(len_ints - 2):
        if ind_s > 0 and ls_ints[ind_s] == ls_ints[ind_s - 1]:
            continue
        ind_m = ind_s + 1
        ind_l = len_ints - 1
        while ind_m < ind_l:
            if not ls_sol:
                ls_sol = [ls_ints[ind_s], ls_ints[ind_m], ls_ints[ind_l]]
            else:
                ls_temp_sol = [ls_ints[ind_s], ls_ints[ind_m], ls_ints[ind_l]]
                if abs(i_target - sum(ls_temp_sol)) < abs(i_target - sum(ls_sol)):
                    ls_sol = ls_temp_sol
                if sum(ls_temp_sol) == i_target:
                    break
                elif sum(ls_temp_sol) < i_target:
                    ind_m += 1
                else:
                    ind_l -= 1

    return sum(ls_sol)

def three_sum_closest_test():
    import csv
    with open('3SumClosestTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            i_actual = three_sum_closest(eval(row[0])[0], eval(row[0])[1])
            i_expected = int(row[1])
            print i_actual
            assert(i_actual == i_expected)

if __name__ == '__main__':
    three_sum_closest_test()
