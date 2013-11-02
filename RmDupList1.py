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
            # return '->'.join(map(str, ls_eles))
        return '->'.join(str(s_ele) for s_ele in ls_eles)
                
    def get_value(self):
        return self._element

class LinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        if self.head is None:
            return ''
        else:
            return repr(self.head)

    def insert(self, element):
        self.head = Node(element, self.head)

    def delete(self):
        if self.head:
            self.head = self.head.next
        else:
            raise ValueError

    def build(self, ls_eles):
        for i_ele in reversed(ls_eles):
            self.insert(i_ele)

def rm_dup_node(node_head):
    if node_head is None:
        return node_head
    pt_cur = node_head
    pt_next = node_head
    while pt_next is not None:
        if pt_next.get_value() != pt_cur.get_value():
            pt_cur.next = pt_next
            pt_cur = pt_next
        pt_next = pt_next.next
    pt_cur.next = None
    return node_head

def rm_dup_node1(node_head):
    if node_head is None:
        return node_head
    pt_cur = node_head
    pt_next = node_head.next
    while pt_next:
        if pt_cur.get_value() == pt_next.get_value():
            pt_cur.next = pt_next.next
        else:
            pt_cur = pt_next
        pt_next = pt_cur.next
    return node_head

def rm_dup_node_test():
    import csv
    with open('RmDupList1Test.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            ll_dup_ls = LinkedList()
            try:
                ls_ori = map(int, row[0].strip('{}').split(','))
            except ValueError:
                ls_ori = []
            print row
            ll_dup_ls.build(ls_ori)
            rm_dup_node1(ll_dup_ls.head)
            print ll_dup_ls, '->'.join(row[1].strip('{}').split(','))
            assert(repr(ll_dup_ls) == '->'.join(row[1].strip('{}').split(',')))
            
if __name__ == '__main__':
    rm_dup_node_test()
