import csv

################################### dp ######################################
def get_sol(set_c, ls_sol, i):
    if i < -1:
        return []
    elif i == -1:
        return [[0] * len(set_c)]
    elif 0 <= i < len(ls_sol):
        return map(list, ls_sol[i])
    else:
        raise ValueError('index out of range')

def comb_sum(set_c, i_t):
    ls_c = list(set_c)
    ls_c.sort()
    ls_sol = [set() for i in range(i_t)]
    for item_t in range(i_t):
        ls_item_sol = []
        for ind_c in range(len(ls_c)):
            ls_sub_sol = get_sol(set_c, ls_sol, item_t - ls_c[ind_c]) 
            if len(ls_sub_sol) > 0:
                for item in ls_sub_sol:
                    item[ind_c] += 1
                ls_item_sol += ls_sub_sol
        ls_sol[item_t] = set(map(tuple, ls_item_sol))
        
    ls_comb = []
    for set_sol in ls_sol[i_t - 1]:
        ls_temp = []
        for ind_c in range(len(ls_c)):
            ls_temp.extend([ls_c[ind_c]] * set_sol[ind_c])
        ls_comb.append(ls_temp)
    return ls_comb  

############################# back tracking ################################## 
def comb_sum2(set_c, i_t):
    ls_c = list(set_c)
    ls_c.sort()
    ls_sol = []
    find_comb_sum(ls_c, i_t, len(ls_c) - 1, ls_sol)
    return ls_sol

def find_comb_sum(ls_c, i_t, ind_end, ls_sol):
    if i_t == 0:
        return True
    if ind_end >= 0 and i_t < ls_c[0]:
        return False
        
    for ind_c in reversed(range(ind_end + 1)):
        if ls_c[ind_c] > i_t:
            continue
        i_largest = ls_c[ind_c]
        for i_times in range(1, i_t / i_largest + 1):
            ls_sub_sol = []
            if find_comb_sum(ls_c, i_t - i_largest * i_times, ind_c - 1, ls_sub_sol):
                if not ls_sub_sol:
                    ls_sol.append([i_largest] * i_times)
                else:
                    ls_sol.extend(sub_sol + [i_largest] * i_times for sub_sol in ls_sub_sol)

    if len(ls_sol) > 0:
        return True
    else:
        return False
        
################################# test #######################################
def comb_sum_test():
    with open('CombSumTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            set_actual = set(map(tuple, comb_sum2(eval(row[0])[0], eval(row[0])[1])))
            set_expected = set(map(tuple, eval(row[1])))
            print row[0]
            assert(set_actual == set_expected)


if __name__ == '__main__':
    comb_sum_test()
