from collections import deque
import csv
import sys

sys.setrecursionlimit(10000)

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

def max_depth_rec(node_root):
    if not node_root:
        return 0
    
    return 1 + max(max_depth_rec(node_root.get_lchild()), 
                   max_depth_rec(node_root.get_rchild()))
    

def max_depth_iter(node_root):
    q_nodes = deque()
    q_nodes.append(node_root)
    i_cur_level = 1
    i_next_level = 0
    i_depth = 0

    while q_nodes:
        node_p = q_nodes.popleft()
        i_cur_level -= 1
        if node_p.get_lchild():
            q_nodes.append(node_p.get_lchild())
            i_next_level += 1
        if node_p.get_rchild():
            q_nodes.append(node_p.get_rchild())
            i_next_level += 1

        if i_cur_level == 0:
            i_cur_level = i_next_level
            i_next_level = 0
            i_depth += 1

    return i_depth

def max_depth_test():
    with open('MaxDepthBTreeTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ls_vals = row[0].strip('{}').split(',')
            print row
            if ls_vals == ['']:
                continue
            node_root = BinaryTree()
            node_root.build_tree(ls_vals)
            assert(max_depth_rec(node_root) == int(row[1]))

if __name__ == '__main__':
    max_depth_test()
