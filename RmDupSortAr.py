import csv

def RmDup(ls_a):
    pt_cur = 0
    pt_ls = 0
    while True:
        while pt_ls < len(ls_a) and ls_a[pt_ls] == ls_a[pt_cur]:
            pt_ls += 1
        if pt_ls == len(ls_a):
            break
        else:
            pt_cur += 1
            ls_a[pt_cur] = ls_a[pt_ls]

    return ls_a[:pt_cur+1], pt_cur + 1

def DirectRmDup(ls_a):
    ls_unique = list(set(ls_a))
    ls_unique.sort()
    return ls_unique, len(ls_unique)

def RmDupTest():
    import numpy.random as nprnd
    for i in range(200):
        len_a = nprnd.randint(20)
        if len_a == 0:
            continue
        ls_a = list(nprnd.randint(5, size = len_a))
        ls_a.sort()
        print ls_a
        print DirectRmDup(ls_a)
        t_tmp = RmDup(ls_a)
        print t_tmp
        assert(t_tmp == DirectRmDup(ls_a))

def rm_dup(ls_a):
    if not ls_a:
        return ls_a
    ind_new_str = 0

    for ind_cur in range(1, len(ls_a)):
        if ls_a[ind_cur] != ls_a[ind_cur - 1]:
            ind_new_str += 1
            ls_a[ind_new_str] = ls_a[ind_cur]

    return ls_a[:ind_new_str + 1]

def rm_dup_test():
    with open('RmDupSortArTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_a = eval(row[0])
            assert(rm_dup(ls_a) == eval(row[1]))
    
if __name__ == '__main__':
    rm_dup_test()
