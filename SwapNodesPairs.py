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

def swap(node_head):
    if not node_head or not node_head._next:
        return node_head
    node_dummy = Node()
    node_dummy._next = node_head
    pt_cur = node_dummy

    while pt_cur and pt_cur._next:
        pt_next = pt_cur._next._next
        if not pt_next:
            break
        pt_cur._next._next = pt_next._next
        pt_next._next = pt_cur._next
        pt_cur._next = pt_next
        pt_cur = pt_cur._next._next

    return node_dummy._next

def swap_test():
    with open('SwapNodesPairsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            node_head = LinkedList()
            try:
                ls_vals = map(int, row[0].strip('{}').split(','))
            except ValueError:
                ls_vals = []
            node_head.build(ls_vals)
            head_new = swap(node_head.head)
            if not head_new:
                assert('' == '->'.join(row[1].strip('{}').split(',')))
            else:
                assert(repr(head_new) == '->'.join(row[1].strip('{}').split(',')))

if __name__ == '__main__':
    swap_test()
