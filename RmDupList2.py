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

def leave_uniq_node(node_head):
    if not node_head or not node_head.next:
        return node_head
    pt_dummy = Node(0, node_head)
    pt_head = pt_dummy
    pt_tail = pt_dummy
    pt_cur = node_head

    while pt_cur:
        b_dup_flag = False
        while pt_cur.next and pt_cur.get_value() == pt_cur.next.get_value():
            b_dup_flag = True
            pt_cur = pt_cur.next
        if not b_dup_flag:
            pt_tail.next = pt_cur
            pt_tail = pt_tail.next
        else:
            pt_tail.next = pt_cur.next
        pt_cur = pt_cur.next

    return pt_head.next
            

def leave_uniq_node_test():
    import csv
    with open('RmDupList2Test.csv') as tfile:
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
            ll_uniq = leave_uniq_node(ll_dup_ls.head)
            print ll_dup_ls, ll_uniq
            if not ll_uniq:
                continue
            assert(repr(ll_uniq) == '->'.join(row[1].strip('{}').split(',')))
            
if __name__ == '__main__':
    leave_uniq_node_test()
