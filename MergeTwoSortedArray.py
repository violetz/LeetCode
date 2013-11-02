def MergeTwoArray(ls_a, len_a, ls_b, len_b):
    pt_a = len_a - 1
    pt_b = len_b - 1
    # while pt_a >= 0:
    #     pt_bpre = pt_b
    #     while pt_b >= 0: 
    #         if ls_b[pt_b] >= ls_a[pt_a]:
    #             pt_b -= 1
    #         else:
    #             ls_a[pt_a + pt_b + 1] = ls_a[pt_a]
    #             ls_a[pt_a + pt_b + 2 : pt_a + pt_bpre + 2] = ls_b[pt_b + 1 : pt_bpre + 1]
    #             break
    #     pt_a -= 1
    # if pt_b >= 0:
    #     ls_a[:pt_b + 1] = ls_b[:pt_b + 1]
    while pt_a >= 0 and pt_b >= 0:
        if ls_a[pt_a] < ls_b[pt_b]:
            ls_a[pt_a + pt_b + 1] = ls_b[pt_b]
            pt_b -= 1
        else:
            ls_a[pt_a + pt_b + 1] = ls_a[pt_a]
            pt_a -= 1
    if pt_b >= 0:
        ls_a[:pt_b + 1] = ls_b[:pt_b + 1]
    return

def MergeTwoArrayTest():
    import numpy.random as nprnd
    for i_test in range(100):
        [len_a, len_b] = nprnd.randint(10, size = 2)
        ls_a = list(nprnd.randint(10, size = len_a))
        ls_b = list(nprnd.randint(20, size = len_b))
        ls_a.sort()
        ls_b.sort()
        ls_sum = ls_a + ls_b
        ls_sum.sort()
        print ls_a, ls_b, ls_sum
        ls_a += [None] * len_b
        MergeTwoArray(ls_a, len_a, ls_b, len_b)
        print ls_a
        assert(ls_sum == ls_a)
    return
        
if __name__ == '__main__':
    MergeTwoArrayTest()
