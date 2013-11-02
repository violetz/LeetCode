def perm(ls_nums):
    import copy
    if ls_nums == []:
        return []
    if len(ls_nums) == 1:
        return [ls_nums]
    ls_perms = []
    ls_pre_perms = perm(ls_nums[1:])
    for sublist in ls_pre_perms:
        for i in range(len(sublist) + 1):
            new_perm = copy.copy(sublist)
            new_perm.insert(i, ls_nums[0])
            ls_perms.append(new_perm)

    return ls_perms
        
def perm_test():
    import csv
    with open('Permutations1Test.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            ls_nums = map(int, row[0].strip('"[]').split(','))
            ls_expected = map(lambda x: map(int, x.split(',')), row[1].strip('"[]').split('],['))
            set_expected = set(map(tuple, ls_expected))
            set_actual = set(map(tuple, perm(ls_nums)))
            print ls_expected
            assert(set_expected == set_actual)

if __name__ == '__main__':
    perm_test()
