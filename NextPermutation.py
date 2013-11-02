def next_perm(ls_num):
    i_len = len(ls_num)
    for ind_num in reversed(xrange(i_len)):
        if ls_num[ind_num] > ls_num[ind_num - 1]:
            break
    if ind_num == 0:
        ls_num.reverse()
        
    else:
        for ind_slot in range(ind_num, i_len):
            if ls_num[ind_slot] <= ls_num[ind_num - 1]:
                break
        if ind_slot == i_len - 1 and ls_num[ind_slot] > ls_num[ind_num - 1]:
            ind_slot += 1
        ls_num[ind_num - 1], ls_num[ind_slot - 1] = ls_num[ind_slot - 1], ls_num[ind_num - 1]
        for i in range((i_len - ind_num) / 2):
            ls_num[ind_num + i], ls_num[-1 - i] = ls_num[-1 - i], ls_num[ind_num + i]
            
    return ls_num
        
def next_perm_test():
    import csv
    with open('NextPermutationTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            ls_num = map(int, row[0].strip('"[]').split(','))
            print ls_num
            ls_expected = map(int, row[1].strip('"[]').split(','))
            ls_actual = next_perm(ls_num)
            print ls_expected, ls_actual
            assert(ls_expected == ls_actual)

if __name__ == '__main__':
    next_perm_test()
