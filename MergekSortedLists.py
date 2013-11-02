import csv
import heapq

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

def merge_k_lists(ls_heads):
    node_dummy = Node()
    pt_merge = node_dummy
    hp_heads = []
    for i in xrange(len(ls_heads)):
        try:
            heapq.heappush(hp_heads, (ls_heads[i].get_value(), i))
        except AttributeError:
            continue

    while hp_heads:
        (node_value, ind_head) = heapq.heappop(hp_heads)
        pt_merge._next = ls_heads[ind_head]
        ls_heads[ind_head] = ls_heads[ind_head]._next
        pt_merge = pt_merge._next
        pt_merge._next = None
        try:
            heapq.heappush(hp_heads, (ls_heads[ind_head].get_value(), ind_head))
        except AttributeError:
            continue

    return node_dummy._next

def merge_k_lists_test():
    with open('MergekSortedListsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_heads = []
            ls_vals = eval(row[0].replace('{', '[').replace('}', ']'))
            for sub_ls in ls_vals:
                ll_new = LinkedList()
                ll_new.build(sub_ls)
                ls_heads.append(ll_new.head)
            node_merge = merge_k_lists(ls_heads)
            if not node_merge:
                assert('' == '->'.join(row[1].strip('{}').split(',')))
            else:
                assert(repr(node_merge) == '->'.join(row[1].strip('{}').split(',')))

if __name__ == '__main__':
    merge_k_lists_test()
