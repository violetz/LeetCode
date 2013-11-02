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

def rev_k(node_head, i_k):
    node_dummy = Node()
    node_dummy._next = node_head
    pt_pre = node_dummy

    while pt_pre:
        pt_next = pt_pre
        ind_node = 0
        while pt_next and ind_node < i_k:
            pt_next = pt_next._next
            ind_node += 1
        if not pt_next:
            break
        pt_cur = pt_pre._next
        for ind_node in range(i_k - 1):
            pt_next = pt_cur._next
            pt_cur._next = pt_next._next
            pt_next._next = pt_pre._next
            pt_pre._next = pt_next
        pt_pre = pt_cur
            
    return node_dummy._next

def rev_k_test():
    with open('RevNodeskGroupTest.csv') as testf:
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
            i_k = int(row[0].split('}, ')[1])
            head_new = rev_k(node_head.head, i_k)
            if not head_new:
                assert('' == '->'.join(row[1].strip('{}').split(',')))
            else:
                assert(repr(head_new) == '->'.join(row[1].strip('{}').split(',')))

if __name__ == '__main__':
    rev_k_test()
