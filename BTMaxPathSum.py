from collections import deque
import csv
import sys

MIN_INT = -sys.maxint - 1

class BinaryTree(object):
    """Binary Tree"""
           
    def __init__(self, element = 0):
        self.set_value(element)
        self._lchild = None
        self._rchild = None

    def __repr__(self):
        if self is None:
            return ''
        return str([self._element, [self._lchild], [self._rchild]])
        
    def get_value(self):
        return self._element

    def set_value(self, element):
        self._element = element

    def get_lchild(self):
        return self._lchild

    def get_rchild(self):
        return self._rchild

    def set_lchild(self, subtree):
        # try:
        #     self._lchild = subtree
        # except TypeError:
        #     self._lchild = BinaryTree(subtree)
        if isinstance(subtree, BinaryTree):
            self._lchild = subtree
        else:
            self._lchild = BinaryTree(subtree)

    def set_rchild(self, subtree):
        # try:
        #     self._rchild = subtree
        # except TypeError:
        #     self._rchild = BinaryTree(subtree)
        if isinstance(subtree, BinaryTree):
            self._rchild = subtree
        else:
            self._rchild = BinaryTree(subtree)

    def build_tree(self, ls_vals):
        if not ls_vals:
            return
        q_nodes = deque()
        self.set_value(int(ls_vals[0]))
        q_nodes.append(self)
        i = 1
        
        while i < len(ls_vals) and len(q_nodes) != 0:
            pnode = q_nodes.popleft()
            if ls_vals[i] != '#':
                pnode.set_lchild(int(ls_vals[i]))
                q_nodes.append(pnode.get_lchild())
            if i+1 == len(ls_vals):
                break
            elif ls_vals[i+1] != '#':
                pnode.set_rchild(int(ls_vals[i+1]))
                q_nodes.append(pnode.get_rchild())
            i += 2

    def leet_code_repr(self):
        if not self:
            return ''
        ls_vals = []
        q_nodes = deque()
        q_nodes.append(self)

        while q_nodes:
            pnode = q_nodes.popleft()
            if pnode:
                ls_vals.append(str(pnode.get_value()))
                q_nodes.append(pnode.get_lchild())
                q_nodes.append(pnode.get_rchild())
            else:
                ls_vals.append('#')

        while ls_vals[-1] == '#':
            ls_vals.pop()
        return ','.join(ls_vals)

def max_path(node_root):
    ls_max = [node_root.get_value()]

    i_max = get_max_path(node_root, ls_max)

    return ls_max[0]


def get_max_path(node_root, ls_max):
    # if not (node_root.get_lchild() or node_root.get_rchild()):
    #     i_max = node_root.get_value()
    #     if i_max > ls_max[0]:
    #         ls_max[0] = i_max
    #     return i_max

    if node_root.get_lchild():
        i_left_max = get_max_path(node_root.get_lchild(), ls_max)
    else:
        i_left_max = MIN_INT

    if node_root.get_rchild():
        i_right_max = get_max_path(node_root.get_rchild(), ls_max)
    else:
        i_right_max = MIN_INT

    i_children_max = max(i_left_max, i_right_max)
    if i_children_max > 0:
        i_max = node_root.get_value() + i_children_max
    else:
        i_max = node_root.get_value()

    i_max_path = node_root.get_value() + max(0, i_left_max, i_right_max, i_left_max + i_right_max)
    if i_max_path > ls_max[0]:
        ls_max[0] = i_max_path

    return i_max

def max_path_test():
    with open('BTMaxPathSumTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_vals = row[0].strip('{}').split(',')
            node_root = BinaryTree()
            node_root.build_tree(ls_vals)
            i_max_path = max_path(node_root)
            assert(i_max_path == int(row[1]))

if __name__ == '__main__':
    max_path_test()
