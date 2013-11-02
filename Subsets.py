import csv

def subsets(set_ints):
    ls_ints = list(set_ints)
    ls_ints.sort()
    ls_subsets = [[]]
    for i_num in ls_ints:
        ls_tmp = []
        for ls_sub in ls_subsets:
            ls_tmp.append(ls_sub + [i_num])
        ls_subsets.extend(ls_tmp)

    return ls_subsets

def subsets_test():
    with open('SubsetsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            set_ints = eval(row[0])
            set_expected = set(map(tuple, eval(row[1])))
            set_actual = set(map(tuple, subsets(set_ints)))
            print set_ints
            assert(set_expected == set_actual)

def subsets_dup(set_ints):
    if not set_ints:
        return [[]]
    ls_ints = list(set_ints)
    ls_ints.sort()
    ls_subsets = [[]]
    ind_start = 0
    ind_end = 0
    while ind_end < len(ls_ints):
        ind_start = ind_end
        while ind_end < len(ls_ints) and ls_ints[ind_end] == ls_ints[ind_start]:
            ind_end += 1
        ls_tmp = []
        for ls_sub in ls_subsets:
            ls_tmp.extend(ls_sub + [ls_ints[ind_start]] * i 
                          for i in range(1, ind_end - ind_start + 1))
        ls_subsets.extend(ls_tmp)

    return ls_subsets

def subsets_dup_test():
    with open('Subsets2Test.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            set_ints = eval(row[0])
            set_expected = set(map(tuple, eval(row[1])))
            set_actual = set(map(tuple, subsets_dup(set_ints)))
            print set_ints
            assert(set_expected == set_actual)

            
if __name__ == '__main__':
    subsets_dup_test()
