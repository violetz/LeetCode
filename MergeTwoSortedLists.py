import csv

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

def merge_two_lists(node_l1, node_l2):
    if not node_l1:
        return node_l2
    if not node_l2:
        return node_l1
    node_dummy = Node()
    pt_merge = node_dummy

    while node_l1 and node_l2:
        if node_l1.get_value() < node_l2.get_value():
            pt_merge._next = node_l1
            node_l1 = node_l1._next
        else:
            pt_merge._next = node_l2
            node_l2 = node_l2._next
        pt_merge = pt_merge._next
        pt_merge._next = None

    if node_l1:
        pt_merge._next = node_l1
    if node_l2:
        pt_merge._next = node_l2

    return node_dummy._next

def merge_two_lists_test():
    with open('MergeTwoSortedListsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_vals1, ls_vals2 = eval(row[0].replace('{', '[').replace('}', ']'))
            l1 = LinkedList()
            if ls_vals1:
                l1.build(ls_vals1)
            l2 = LinkedList()
            if ls_vals2:
                l2.build(ls_vals2)
            node_merge = merge_two_lists(l1.head, l2.head)
            if not node_merge:
                assert('' == '->'.join(row[1].strip('{}').split(',')))
            else:
                assert(repr(node_merge) == '->'.join(row[1].strip('{}').split(',')))

if __name__ == '__main__':
    merge_two_lists_test()
