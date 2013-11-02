import csv

def comb_sum(ls_nums, i_target):
    ls_nums.sort()
    ls_combs = []

    get_comb_sum(ls_nums, i_target, 0, ls_combs)
    # print a

    return ls_combs

def get_comb_sum(ls_nums, i_target, ind_start, ls_combs):
    #    print ls_nums, i_target, ind_start, ls_combs
    if i_target == 0:
        return True
    if ind_start >= len(ls_nums) or i_target < ls_nums[ind_start]:
        return False

    while ind_start < len(ls_nums):
        i_cur = ls_nums[ind_start]
        ind_next_start = ind_start
        while ind_next_start < len(ls_nums) and ls_nums[ind_next_start] == i_cur:
            ind_next_start += 1
            # print '@', ind_start, ind_next_start
        for i_count in xrange(ind_next_start - ind_start):
            # print '%', i_count, i_cur, i_target
            ls_sub_combs = []
            if get_comb_sum(ls_nums, i_target - (i_count + 1) * i_cur,
                            ind_next_start, ls_sub_combs):
                #  print '*', ls_sub_combs
                if ls_sub_combs:
                    #   print '@'
                    ls_combs.extend([i_cur] * (i_count + 1) + sub_comb 
                                    for sub_comb in ls_sub_combs)
                else:
                    #print '?'
                    ls_combs.append([i_cur] * (i_count + 1))
                    #print ls_sub_combs, ls_combs
        ind_start = ind_next_start

    if ls_combs:
        return True
    else:
        return False

def comb_sum_test():
    with open('CombSum2Test.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_nums, i_target = eval(row[0])
            set_actual = set(map(tuple, comb_sum(ls_nums, i_target)))
            set_expect = set(map(tuple, eval(row[1])))
            assert(set_actual == set_expect)

if __name__ == '__main__':
    comb_sum_test()
