import math
import csv

def perm_seq(i_n, i_k):
    ls_nums = range(1, i_n+1)
    ls_perm = [0 for i in range(i_n)]
    i_k -= 1
    i_k %= math.factorial(i_n)
    for i in xrange(i_n):
        i_fac = math.factorial(i_n - 1 - i)
        ls_perm[i] = ls_nums[i_k / i_fac]
        ls_nums.pop(i_k / i_fac)
        i_k %= i_fac

    return ''.join(str(item) for item in ls_perm)

def perm_seq_test():
    with open('PermutationSequenceTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            (i_n, i_k) = map(int, row[0].split(', '))
            s_expected = row[1].strip('"')
            s_actual = perm_seq(i_n, i_k)
            print s_expected, s_actual
            assert(s_actual == s_expected)

if __name__ == '__main__':
    perm_seq_test()
