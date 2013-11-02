class BinaryTree(object):
    """Binary Tree"""
    def __init__(self, element):
        self.set_node(element)
        self._lchild = None
        self._rchild = None

    def __repr__(self):
        # str_node = str(self._element)
        # if self._lchild is not None:
        #     str_lchild = repr(self._lchild)
        #     str_node += '(' + str_lchild + ')'
        # else:
        #     str_node += '()'
        # if self._rchild is not None:
        #     str_rchild = repr(self._rchild)
        #     str_node += '(' + str_rchild + ')'
        # else:
        #     str_node += '()'
        # return str_node
        if self is None:
            return None
        return str([self._element, [self._lchild], [self._rchild]])
        
    def get_value(self):
        return self._element

    def set_node(self, element):
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

    def in_order(self):
        if self is None:
            return
        else:
            return [self.get_lchild().in_order(), self.get_value(), self.get_rchild().in_order()]

def build_tree(ls_vals):
    from collections import deque
    q_nodes = deque()
    BT_root = BinaryTree(ls_vals[0])
    q_nodes.append(BT_root)
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

    return BT_root

def rec_in_order(BT_root):
    ls_nodes = []
    if BT_root is not None:
        ls_nodes.extend(rec_in_order(BT_root.get_lchild()))
        ls_nodes.append(BT_root.get_value())
        ls_nodes.extend(rec_in_order(BT_root.get_rchild()))
    
    return ls_nodes

def iter_in_order(node):
    ls_nodes = []
    stk_nodes = []
    while len(stk_nodes) != 0 or node is not None:
        if node is not None:
            stk_nodes.append(node)
            node = node.get_lchild()
        else:
            node = stk_nodes.pop()
            ls_nodes.append(node.get_value())
            node = node.get_rchild()
    return ls_nodes

def sym_tree(BT_root):
    ls_nodes = rec_in_order(BT_root)
    len_nodes = len(ls_nodes)
    if len_nodes % 2 == 0:
        return False
    else:
        ind_mid = len_nodes / 2
        for i in range(1, ind_mid + 1):
            if ls_nodes[ind_mid - i] != ls_nodes[ind_mid + i]:
                return False
        return True

def rec_sym_tre(BT_root):
    return rec_mirror(BT_root.get_lchild(), BT_root.get_rchild())

def rec_mirror(BT_lchild, BT_rchild):
    if BT_lchild is None and BT_rchild is None:
        return True
    elif BT_lchild is None or BT_rchild is None:
        return False
    elif BT_lchild.get_value() != BT_rchild.get_value():
        return False
    else:
        return rec_mirror(BT_lchild.get_lchild(), BT_rchild.get_rchild()) and rec_mirror(BT_lchild.get_rchild(), BT_rchild.get_lchild())
