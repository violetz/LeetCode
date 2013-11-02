import sys
sys.path.append('/media/xiaowei/Study/Software Learning/Python/LeetCode')
from DataStructures.LinkedQueue import *

def AddTwoLists(ls_a, ls_b):
    ls_sum = LinkedQueue()
    pt_a = ls_a._head
    pt_b = ls_b._head
    i_tens = 0
    while pt_a is not None or pt_b is not None:
        if pt_a is not None and pt_b is not None:
            i_sum = pt_a._element + pt_b._element + i_tens
        if pt_a is None and pt_b is not None:
            i_sum = pt_b._element + i_tens
        if pt_a is not None and pt_b is None:
            i_sum = pt_a._element + i_tens
        i_ones = i_sum % 10
        i_tens = (i_sum - i_ones) / 10
        ls_sum.enqueue(i_ones)
        if pt_a is not None:
            pt_a = pt_a._next
        if pt_b is not None:
            pt_b = pt_b._next
    if i_tens != 0:
        ls_sum.enqueue(i_tens)
    return ls_sum

def ListToNum(ls_a):
    if ls_a.is_empty():
        return 0
    r_a = repr(ls_a)
    list_a = r_a.split()
    list_a.reverse()
    s_a = ''.join(list_a)
    i_a = int(s_a)
    return i_a
    
def DirectAdd(ls_a, ls_b):
    i_a = ListToNum(ls_a)
    i_b = ListToNum(ls_b)
    i_sum = i_a + i_b
    return i_sum
    
def AddTwoListsTest():
    import numpy.random as nprnd
    for i in range(10000):
        len_a = nprnd.randint(10)
        len_b = nprnd.randint(10)
        temp_a = nprnd.randint(10, size = len_a)
        temp_b = nprnd.randint(10, size = len_b)
        ls_a = LinkedQueue()
        ls_b = LinkedQueue()
        for item in temp_a:
            ls_a.enqueue(item)
        for item in temp_b:
            ls_b.enqueue(item)
        ls_sum = AddTwoLists(ls_a, ls_b)
        print ls_a, ':', ls_b, ':', ls_sum
        assert(ListToNum(ls_sum) == DirectAdd(ls_a, ls_b))

if __name__ == '__main__':
    AddTwoListsTest()
