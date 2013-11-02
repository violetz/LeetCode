class Node(object):
    def __init__(self, value = 0, pt_next = None):
        self.element = value
        self.next = pt_next

    def __repr__(self):
        ls_vals = []
        pt_node = self
        while pt_node:
            ls_vals.append(pt_node.get_value())
            pt_node = pt_node.next
        return '->'.join(str(val) for val in ls_vals)

    def get_value(self):
        return self.element

    def set_value(self, value):
        self.element = value

class LinkedList(object):
    def __init__(self, ls_vals = []):
        self.head = None
        for i_val in reversed(ls_vals):
            self.insert(i_val)            

    def __repr__(self):
        return repr(self.head)

    def insert(self, value):
        self.head = Node(value, self.head)

    def remove(self):
        if self.head:
            self.head = self.head.next
        else:
            raise ValueError('linked list is empty')


def rev_ll_iter(node_head):
    if not node_head:
        return node_head
    pt_pre = None
    pt_cur =  node_head
    while pt_cur.next:
        pt_next = pt_cur.next
        pt_cur.next = pt_pre
        pt_pre = pt_cur
        pt_cur = pt_next
    pt_cur.next = pt_pre
    
    return pt_cur

def rev_ll_rec(node_head):
    # if not node_head or not node_head.next:
    #     return (node_head, node_head)
    # pt_head, pt_tail = rev_ll_rec(node_head.next)
    # pt_tail.next = node_head
    # node_head.next = None
    # return pt_head, node_head

    if not node_head:
        return node_head
    pt_next = node_head.next
    if not pt_next:
        return node_head
    pt_rev_head = rev_ll_rec(pt_next)
    pt_next.next = node_head
    node_head.next = None

    return pt_rev_head

def rev_ll_2(node_head, i_m, i_n):
    if not node_head:
        return None
    pt_pre = None
    pt_cur = node_head
    ind_cur = 1
    while pt_cur and ind_cur < i_m:
        pt_pre = pt_cur
        pt_cur = pt_cur.next
        ind_cur += 1
    pt_pre_m = pt_pre
    pt_m = pt_cur
    
    while pt_cur and ind_cur < i_n + 1:
        pt_next = pt_cur.next
        pt_cur.next = pt_pre
        pt_pre = pt_cur
        pt_cur = pt_next
        ind_cur += 1
    pt_next_n = pt_cur
    pt_n = pt_pre

    if pt_pre_m:
        pt_pre_m.next = pt_n
        pt_m.next = pt_next_n
        return node_head
    else:
        pt_m.next = pt_next_n
        return pt_n

def rev_ll_2_clean(node_head, i_m, i_n):
    if not node_head:
        return None
    node_dummy = Node()
    node_dummy.next = node_head
    pt_pre = node_dummy
    pt_cur = node_head

    for ind_cur in range(1, i_n + 1):
        if ind_cur == i_m:
            pt_pre_m = pt_pre
            
        if i_m < ind_cur <= i_n:
            pt_pre.next = pt_cur.next
            pt_cur.next = pt_pre_m.next
            pt_pre_m.next = pt_cur
            pt_cur = pt_pre

        pt_pre = pt_cur
        pt_cur = pt_cur.next

    return node_dummy.next           
        
def rev_ll_2_test():
    import csv
    with open('RevLinkedListTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ll_a = LinkedList(map(int, row[0].strip('{}').split('}, ')[0].split(',')))
            i_m, i_n = map(int, row[0].strip('{}').split('}, ')[1].split(', '))
            ll_actual = rev_ll_2_clean(ll_a.head, i_m, i_n)
            s_expected = '->'.join(row[1].strip('{}').split(','))
            print s_expected
            assert(repr(ll_actual) == s_expected)

if __name__ == '__main__':
    rev_ll_2_test()
