def comb(i_n, i_k):
    if i_n == 0 or i_k == 0 or i_n < i_k:
        return []
    if i_k == 1:
        return [[i + 1] for i in xrange(i_n)]
    if i_n == i_k:
        return [[i + 1 for i in xrange(i_n)]]
    ls_pre_combs = comb(i_n - 1, i_k - 1)
    for sublist in ls_pre_combs:
        sublist.append(i_n)
    ls_combs = comb(i_n - 1, i_k) + ls_pre_combs
    return ls_combs

def comb_test():
    import csv
    with open('CombinationsTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            i_n, i_k = map(int, row[0].split(', '))
            ls_expected = map(lambda x: map(int, x.split(',')), row[1].strip('[]').split('],['))
            ls_actual = comb(i_n, i_k)
            set_expected = set(map(tuple, ls_expected))
            set_actual = set(map(tuple, ls_actual))
            print set_expected
            assert(set_expected == set_actual)

if __name__ == '__main__':
    comb_test()
        
