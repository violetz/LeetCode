import sys
sys.path.append('/media/xiaowei/Study/Software Learning/Python/LeetCode')
from DataStructures.LinkedStack import *

def RmNth(ls_a, n):
    pt0 = ls_a._head
    pt1 = ls_a._head
    pt2 = ls_a._head
    for i in range(n-1):
        pt2 = pt2._next
    while pt2._next is not None:
        pt0 = pt1
        pt1 = pt1._next
        pt2 = pt2._next
    if pt0 == pt1:
        ls_a._head = ls_a._head._next
    else:
        pt0._next = pt1._next
    return
    
    
def RmNthTest():
    import numpy.random as nprnd
    for i_loop in range(100):
        n = nprnd.randint(5)
        if n == 0:
            continue
        len_a = n + nprnd.randint(5)
        temp_a = nprnd.randint(10, size = len_a)
        ls_a = LinkedStack()
        for item in temp_a:
            ls_a.push(item)
        ls_rm = LinkedStack()
        for i in range(len_a):
            if i == n - 1:
                continue
            ls_rm.push(temp_a[i])
        print ls_a, ':', ls_rm, ':', n
        RmNth(ls_a, n)
        assert(repr(ls_a) == repr(ls_rm))
    return

if __name__ == '__main__':
    RmNthTest()
