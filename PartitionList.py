import csv
import sys
sys.path.append('/media/xiaowei/Study/Software Learning/Python/LeetCode')
from DataStructures.LinkedQueue import *

# def InplacePartition1(ll_a, i_key):
#     pt_sep = ll_a._head
#     while True:
#         while pt_sep is not None and pt_sep._element < i_key:
#             pt_sep = pt_sep._next
#         if pt_sep is None:
#             break
#         pt_le = pt_sep
#         while pt_le._next is not None and pt_le._next._element >= i_key:
#             pt_le = pt_le._next
#         if pt_le._next is None:
#             break
#         Node_l = pt_le._next
#         pt_le._next = Node_l._next
#         Node_l._next = pt_sep
#         pt_sep = ._next
        
def DirectPartition(ll_a, i_key):
    ll_lpart = LinkedQueue()
    ll_gepart = LinkedQueue()
    pt_a = ll_a._head
    while pt_a is not None:
        i_a = pt_a._element
        if i_a < i_key:
            ll_lpart.enqueue(i_a)
        else:
            ll_gepart.enqueue(i_a)
        pt_a = pt_a._next
    if ll_lpart.is_empty():
        return ll_gepart
    else:
        ll_lpart._tail._next = ll_gepart._head
        ll_lpart._tail = ll_gepart._tail
        ll_lpart._size += ll_gepart._size
        return ll_lpart

def PartitionListTest():
    import numpy.random as nprnd
    for i_test in range(100):
        len_a = nprnd.randint(8)
        if len_a == 0:
            continue
        temp_a = list(nprnd.randint(8, size = len_a))
        ll_a = LinkedQueue()
        for item in temp_a:
            ll_a.enqueue(item)

class Node(object):
    def __init__(self, element = 0, next_node = None):
        self._element = element
        self._next = next_node

    def __repr__(self):
        ls_vals = []
        pt_node = self
        while pt_node:
            ls_vals.append(pt_node.get_value())
            pt_node = pt_node._next

        return '->'.join(map(str, ls_vals))

    def get_value(self):
        return self._element

class LinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        return repr(self.head)

    def insert(self, element):
        self.head = Node(element, self.head)

    def remove(self):
        if not self.head:
            raise ValueError
        else:
            self.head = self.head._next

    def build(self, ls_vals):
        for i_val in reversed(ls_vals):
            self.insert(i_val)

def partition_list(node_head, i_key):
    if not node_head:
        return
    node_dummy = Node()
    node_dummy._next = node_head
    pt_sep = node_dummy
    pt_pre = node_dummy

    while pt_pre._next:
        if pt_pre._next.get_value() < i_key:
            if pt_pre == pt_sep:
                pt_pre = pt_pre._next
                pt_sep = pt_sep._next
            else:
                pt_cur = pt_pre._next
                pt_pre._next = pt_cur._next
                pt_cur._next = pt_sep._next
                pt_sep._next = pt_cur
                pt_sep = pt_sep._next
        else:
            pt_pre = pt_pre._next

    return node_dummy._next

def partition_list_test():
    with open('PartitionListTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            node_head = LinkedList()
            try:
                ls_vals = map(int, row[0].split('}, ')[0].strip('{').split(','))
            except ValueError:
                ls_vals = []
            node_head.build(ls_vals)
            i_key = int(row[0].split('}, ')[1])
            head_new = partition_list(node_head.head, i_key)
            if not head_new:
                assert('' == '->'.join(row[1].strip('{}').split(',')))
            else:
                assert(repr(head_new) == '->'.join(row[1].strip('{}').split(',')))

if __name__ == '__main__':
    partition_list_test()
