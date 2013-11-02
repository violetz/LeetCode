import csv

def leave_twice_v1(ls_a):
    if not ls_a:
        return ls_a

    ind_new_str = 0
    i_counter = 1

    for ind_cur in range(1, len(ls_a)):
        if ls_a[ind_cur] != ls_a[ind_new_str]:
            ind_new_str += 1
            ls_a[ind_new_str] = ls_a[ind_cur]
            i_counter = 1
        elif ls_a[ind_cur] == ls_a[ind_new_str]:
            if i_counter < 2:
                ind_new_str += 1
                ls_a[ind_new_str] = ls_a[ind_cur]
            i_counter += 1

    return ls_a[:ind_new_str + 1]

def leave_twice(ls_a):
    if len(ls_a) < 3:
        return ls_a

    ind_new_str = 1

    for ind_cur in range(2, len(ls_a)):
        if ls_a[ind_cur] != ls_a[ind_new_str] or ls_a[ind_cur] != ls_a[ind_new_str - 1]:
            ind_new_str += 1
            ls_a[ind_new_str] = ls_a[ind_cur]

    return ls_a[:ind_new_str + 1]

def leave_twice_test():
    with open('RmDupSortAr2Test.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_a = eval(row[0])
            assert(leave_twice(ls_a) == eval(row[1]))
    
if __name__ == '__main__':
    leave_twice_test()
