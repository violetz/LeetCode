from collections import deque
import csv

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

def level_order(node_root):
    if not node_root:
        return []
    ls_levels = deque([[]])
    q_nodes = deque()
    q_nodes.append(node_root)
    i_cur_level = 1
    i_next_level = 0

    while q_nodes:
        node_p = q_nodes.popleft()
        ls_levels[0].append(node_p.get_value())
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
            ls_levels.appendleft([])

    ls_levels.popleft()
    return list(ls_levels)

def level_order2(node_root):
    if not node_root:
        return []
    ls_levels = []
    level_order_rec(node_root, 1, ls_levels)
    ls_levels.reverse()

    return ls_levels

def level_order_rec(node_p, i_level, ls_levels):
    if len(ls_levels) < i_level:
        ls_levels.append([])

    ls_levels[i_level - 1].append(node_p.get_value())
    if node_p.get_lchild():
        level_order_rec(node_p.get_lchild(), i_level + 1, ls_levels)
    if node_p.get_rchild():
        level_order_rec(node_p.get_rchild(), i_level + 1, ls_levels)
    return

def level_order_test():
    with open('BTLevelTraversal2Test.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ls_vals = row[0].strip('{}').split(',')
            print row
            if ls_vals == ['']:
                continue
            node_root = BinaryTree()
            node_root.build_tree(ls_vals)
            assert(level_order2(node_root) == eval(row[1]))

if __name__ == '__main__':
    level_order_test()
