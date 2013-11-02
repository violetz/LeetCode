import csv

def jump_dp(ls_ints):
    i_len = len(ls_ints)
    ls_min_jumps = [0] + [i_len] * (i_len - 1)

    for ind_cur in range(i_len):
        for ind_extend in range (ls_ints[ind_cur]):
            if 1 + ind_cur + ind_extend < i_len:
                ls_min_jumps[1 + ind_cur + ind_extend] = min(
                    ls_min_jumps[ind_cur] + 1, 
                    ls_min_jumps[1 + ind_cur + ind_extend])
            else:
                break
                

    if ls_min_jumps[-1] == i_len:
        return -1
    else:
        return ls_min_jumps[-1]

def jump1(ls_ints):
    if len(ls_ints) <= 1:
        return 0
    i_len = len(ls_ints)
    i_max_extend = ls_ints[0]
    i_new_max_extend = i_max_extend
    ind_cur = 1
    i_jump_num = 1

    while ind_cur <= i_max_extend:
        if i_max_extend >= i_len - 1:
            return i_jump_num
        i_new_max_extend = max(i_new_max_extend, ind_cur + ls_ints[ind_cur])
        ind_cur += 1
        if ind_cur > i_max_extend:
            i_max_extend = i_new_max_extend
            i_jump_num += 1

    return -1

def jump(ls_ints):
    i_len = len(ls_ints)
    i_max_extend = 0
    i_new_max_extend = 0
    i_jump_num = 0

    for ind_cur in range(i_len):
        if ind_cur > i_max_extend:
            i_max_extend = i_new_max_extend
            i_jump_num += 1
        i_new_max_extend = max(i_new_max_extend, ind_cur + ls_ints[ind_cur])

    return i_jump_num

def jump_test():
    with open('JumpGame2Test.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_ints = eval(row[0])
            assert(jump(ls_ints) == int(row[1]))

if __name__ == '__main__':
    jump_test()
