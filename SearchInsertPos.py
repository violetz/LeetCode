def binary_search(ls_a, key, ledge, redge):
    #print ledge, redge, ls_a[ledge:(redge + 1)]
    if ledge == redge or ledge == redge - 1:
        if key == ls_a[ledge]:
            return ledge
        if key == ls_a[redge]:
            return redge
        if key < ls_a[ledge]:
            if ledge == 0:
                return 0
            else:
                return ledge
        if ls_a[ledge] < key < ls_a[redge]:
            return redge
        if key > ls_a[redge]:
            return redge + 1
    mid_pt = (ledge + redge) / 2
    if key == ls_a[mid_pt]:
        return mid_pt
    elif key < ls_a[mid_pt]:
        return binary_search(ls_a, key, ledge, mid_pt)
    else:
        return binary_search(ls_a, key, mid_pt+1, redge)

def binary_search_ford(ls_a, key):
    left = -1
    right = len(ls_a)
    while left < right:
        mid = (left + right) / 2
        if ls_a[mid] == key:
            return mid
        elif ls_a[mid] < key:
            if left == mid:
                return right
            left = mid
        else:
            right = mid
    return left + 1

def binary_search_mary(ls_a, key):
    ledge = -1
    redge = len(ls_a)
    while ledge < redge:
        mid_pt = (ledge + redge) / 2
        if key == ls_a[mid_pt]:
            return mid_pt
        elif key < ls_a[mid_pt]:
            redge = mid_pt
            if ledge == redge - 1:
                break
        else:
            ledge = mid_pt
            if ledge == redge -1:
                break
    return ledge + 1
    
def binary_search_test():
    import numpy.random as nprnd
    for i_test in range(1000):
        len_a = nprnd.randint(1, 15)
        ls_a = list(nprnd.choice(range(30), size = len_a, replace = False))
        ls_a.sort()
        key = nprnd.randint(-5, 35)
        print ls_a, key
        if key in ls_a:
            ind_key = ls_a.index(key)
        else:
            ls_b = ls_a + [key]
            ls_b.sort()
            ind_key = ls_b.index(key)
        print "ind_key: ", ind_key
        print "b_search: ", binary_search_mary(ls_a, key)
        # assert(ind_key == binary_search(ls_a, key, 0, len_a-1))
        # assert(ind_key == binary_search_ford(ls_a, key))
        assert(ind_key == binary_search_mary(ls_a, key))

if __name__ == '__main__':
    binary_search_test()
