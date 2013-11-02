# import sys
# sys.path.append('/media/xiaowei/Study/Software Learning/Python/LeetCode/DataStructures')
# import LinkedQueue as LinkedList

class Node(object):
    __slots__ = '_element', 'next'

    def __init__(self, element, next_node = None):
        self._element = element
        self.next = next_node

    def __repr__(self):
        ls_eles = []
        pt_node = self
        while pt_node:
            ls_eles.append(pt_node.get_value())
            pt_node = pt_node.next
        return '->'.join(map(str, ls_eles))
        
    def get_value(self):
        return self._element

class LinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        return repr(self.head)

    def insert(self, element):
        self.head = Node(element, self.head)

    def delete(self):
        if self.head:
            self.head = self.head.next
        else:
            raise ValueError

def rot_list(node_head, i_k):
    if node_head is None or i_k <= 0:
        return node_head
    pt_cur = node_head
    i_len = 1
    while pt_cur.next:
        i_len += 1
        pt_cur = pt_cur.next
    i_k = i_k % i_len
    if i_k == 0:
        return node_head
    pt_cur.next = node_head
    pt_cur = node_head
    ind_cur = 0
    ind_newhead = i_len - i_k
    while ind_cur < ind_newhead - 1:
        pt_cur = pt_cur.next
        ind_cur += 1
    node_head = pt_cur.next
    pt_cur.next = None
    return node_head

# a = LinkedList()
# a.insert(5)
# a.insert(4)
# a.insert(3)
# a.insert(2)
# a.insert(1)
# b = rot_list(a.head, 2)
# b
# c = rot_list(b, 10)

def change_format(ls_row):
    (str_input_eles, str_input_i_k) = ls_row[0].split(', ')
    try:
        ls_input_eles = map(int, str_input_eles.strip('{}').split(','))
    except ValueError:
        ls_input_eles = []
    i_k = int(str_input_i_k)
    try:
        ls_output_eles = map(int, ls_row[1].strip('{}').split(','))
    except ValueError:
        ls_output_eles = []
    return ls_input_eles, i_k, ls_output_eles

def ls_to_ll(ls_eles):
    ll_a = LinkedList()
    # i_len = len(ls_eles)
    # for i in range(i_len-1, -1, -1):
    #     ll_a.insert(ls_eles[i])
    for i in reversed(ls_eles):
        ll_a.insert(i)
    return ll_a.head    

def rot_list_test():
    import csv
    with open('RotateListTest.csv', 'r') as tfile:
        csvf = csv.reader(tfile, delimiter = ',', quotechar = '"')
        next(csvf)
        for row in csvf:
            (ls_input_eles, i_k, ls_output_eles) = change_format(row)
            node_input = ls_to_ll(ls_input_eles)
            node_output = ls_to_ll(ls_output_eles)
            node_actual = rot_list(node_input, i_k)
            print node_input, i_k, node_actual, node_output
            assert(repr(node_actual) == repr(node_output))

if __name__ == '__main__':
    rot_list_test()
