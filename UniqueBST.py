def unique_bst(n):
    cache = {0:1}
    unique_bst_with_cache(n, cache)
    return cache[n]

def unique_bst_with_cache(n, cache):
    i_bstno = 0
    for item in xrange(n):
        if item not in cache:
            unique_bst_with_cache(item, cache)
        if n - 1 - item not in cache:
            unique_bst_with_cache(n - 1 - item, cache)
        i_bstno += cache[item] * cache[n - 1 - item]
    cache[n] = i_bstno
    print n, cache

def unique_bst_rec(n):
    if n == 0:
        return 1
    else:
        i_bstno = 0
        for item in xrange(n):
            i_bstno += unique_bst_rec(item) * unique_bst_rec(n - 1 - item)
        return i_bstno

def u_bst_array(n):
    ls_bstno = [0] * (n+1)
    ls_bstno[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            ls_bstno[i] += ls_bstno[j] * ls_bstno[i - 1 - j]
    print ls_bstno            
    return ls_bstno[n]
        
if __name__ == '__main__':
    print unique_bst(3)
