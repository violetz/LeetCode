import csv

def can_jump(ls_ints):
    i_n = len(ls_ints) - 1
    ind_cur = 0
    i_max_leap = ls_ints[0]

    while ind_cur <= i_max_leap:
        if i_max_leap >= i_n:
            return True
        i_new_max = max(ind_cur + ls_ints[ind_cur], i_max_leap)
        ind_cur += 1
        if ind_cur > i_max_leap:
            i_max_leap = i_new_max

    return False
        
def can_jump_test():
    with open('JumpGameTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_ints = eval(row[0])
            b_expected = row[1] == 'true'
            assert(can_jump(ls_ints) == b_expected)

if __name__ == '__main__':
    can_jump_test()
