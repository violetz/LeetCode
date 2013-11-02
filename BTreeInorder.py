from collections import deque

class BinaryTree(object):
    """Binary Tree"""
       
    def __init__(self, element = 0):
        self.set_value(element)
        self._lchild = None
        self._rchild = None
        self.next_right = None

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
        self.set_value(ls_vals[0])
        q_nodes.append(self)
        i = 1
        
        while i < len(ls_vals) and len(q_nodes) != 0:
            pnode = q_nodes.popleft()
            if ls_vals[i] != '#':
                pnode.set_lchild(ls_vals[i])
                q_nodes.append(pnode.get_lchild())
            if i+1 == len(ls_vals):
                break
            elif ls_vals[i+1] != '#':
                pnode.set_rchild(ls_vals[i+1])
                q_nodes.append(pnode.get_rchild())
            i += 2

    def level_traverse(self):
        q_nodes = deque()
        q_nodes.append(self)
        i_cur_level_cnt = 1
        i_next_level_cnt = 0
        ls_vals = []
        while q_nodes:
            ind_most_left = i_cur_level_cnt - 1
            while i_cur_level_cnt > 0:
                node_cur = q_nodes.popleft()
                i_cur_level_cnt -= 1
                if i_cur_level_cnt == ind_most_left:
                    node_most_left = node_cur
                if node_cur.get_lchild():
                    q_nodes.append(node_cur.get_lchild())
                    i_next_level_cnt += 1
                if node_cur.get_rchild():
                    q_nodes.append(node_cur.get_rchild())
                    i_next_level_cnt += 1
            i_cur_level_cnt = i_next_level_cnt
            i_next_level_cnt = 0
            ls_level = []
            while node_most_left:
                ls_level.append(node_most_left.get_value())
                node_most_left = node_most_left.next_right
            ls_vals.append(ls_level)

        return ls_vals

def inorder_traversal_iter(node_root):
    ls_nodes = []
    ls_inorder_trav = []
    pt_node = node_root
    while pt_node or ls_nodes:
        if pt_node:
            ls_nodes.append(pt_node)
            pt_node = pt_node.get_lchild()
            # print '*', ls_nodes, ls_inorder_trav
        else:
            pt_node = ls_nodes.pop()
            ls_inorder_trav.append(pt_node.get_value())
            pt_node = pt_node.get_rchild()
            # print '#', ls_nodes, ls_inorder_trav

    return ls_inorder_trav

def inorder_traversal_rec(node_root):
    ls_inorder_trav = []
    if node_root:
        ls_inorder_trav = (inorder_traversal_rec(node_root.get_lchild()) +
                           [node_root.get_value()] +
                           inorder_traversal_rec(node_root.get_rchild()))
    return ls_inorder_trav

def inorder_traversal_iter_test():
    import csv
    with open('BTreeInorderTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            s_vals = row[0].replace('#', '"#"').replace('{', '[').replace('}', ']')
            node_root = BinaryTree()
            node_root.build_tree(eval(s_vals))
            ls_expected = eval(row[1])
            ls_actual = inorder_traversal_iter(node_root)
            print ls_actual
            if s_vals == '[]':
                assert(inorder_traversal_iter(None) == ls_expected)
            else:
                assert(ls_expected == ls_actual)
    return
            
if __name__ == '__main__':
    inorder_traversal_iter_test()
