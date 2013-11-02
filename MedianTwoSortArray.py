def FindMed(ls_a, ls_b):
    m = len(ls_a)
    n = len(ls_b)
    ind_a = (m-1) / 2
    ind_b = (n-1) / 2
    print ls_a
    print ls_b
    if m == 0 and n == 0:
        return
    if m == 0:
        return ls_b[ind_b]
    if n == 0:
        return ls_a[ind_a]
    if m == 1 and n == 1:
        return min(ls_a[ind_a], ls_b[ind_b])
    if ls_a[ind_a] == ls_b[ind_b]:
        return ls_a[ind_a]
    if ls_a[(m-1) / 2] < ls_b[(n-1) / 2]:
        if m <= n:
            if m == 1 and n % 2 == 0:
                return ls_b[(n-1) / 2]
            if m == 1 and n % 2 == 1:
                return max(ls_a[(m-1) / 2], ls_b[(n-1) / 2 - 1])
            if m == 2:
                return FindMed(ls_a[1:], ls_b[:n-1])
            else:
                return FindMed(ls_a[(m-1) / 2:], ls_b[:(n - (m-1) / 2)])
        if m > n:
            if n == 1 and m % 2 == 0:
                return min(ls_a[(m-1) / 2 + 1], ls_b[(n-1) / 2])
            if n == 1 and m % 2 == 1:
                return ls_a[(m-1) / 2]
            if n == 2:
                if ls_b[ind_b] <= ls_a[ind_a + 1]:
                    return ls_b[ind_b]
                else:
                    return FindMed(ls_a[1:], ls_b[:-1])
            elif n % 2 == 0:
                return FindMed(ls_a[(n+1) / 2:], ls_b[:(n+1) / 2])
            else:
                return FindMed(ls_a[(n-1) / 2:], ls_b[:(n+1) / 2])
    if ls_a[(m-1) / 2] > ls_b[(n-1) / 2]:
        return FindMed(ls_b, ls_a)

def RightMed(ls_a, ls_b):
    ls_all = ls_a + ls_b
    ls_all.sort()
    return ls_all[(len(ls_all)-1) / 2]

def FindMedTest():
    # ls_a1 = range(10)
    # ls_b1 = range(10)
    # correct_med = RightMed(ls_a1, ls_b1)
    # med = FindMed(ls_a1, ls_a2)
    # print correct_med, med

    # ls_a2 = range(1, 6, 2)
    # ls_b2 = range(2, 10, 2)
    # correct_med = RightMed(ls_a2, ls_b2)
    # med = FindMed(ls_a2, ls_b2)
    # print correct_med, med
    import numpy.random as nprnd
    for i in xrange(100):
        [i_m, i_n] = nprnd.randint(10, size = 2)
        if i_m == 0 and i_n == 0:
            continue
        ls_a = list(nprnd.randint(5, size = i_m))
        ls_a.sort()
        ls_b = list(nprnd.randint(5, size = i_n))
        ls_b.sort()
        print 'i = ', i
        print ls_a
        print ls_b
        med = FindMed(ls_a, ls_b)
        print RightMed(ls_a, ls_b), med
        assert(RightMed(ls_a, ls_b) == FindMed(ls_a, ls_b))
    return

if __name__ == '__main__':
    FindMedTest()
