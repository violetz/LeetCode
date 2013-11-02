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

def level_traversal(ls_nodes):
    ls_level = []

    def get_value(node):
        if node is None:
            return
        else:
            return node._element

    def get_children(node):
        if node is None:
            return 
        else:
            ls_children = [node._lchild, node._rchild]
            return [item for item in ls_children if item is not None]

    ls_level.append(map(get_value, ls_nodes))
    ls_children = map(get_children, ls_nodes)
    ls_children = [item for sublist in ls_children for item in sublist]
    while ls_children != []:
        ls_level.append(map(get_value, ls_children))
        ls_children = map(get_children, ls_children)
        ls_children = [item for sublist in ls_children for item in sublist]

    return ls_level

def l_t_queue(BT_root):
    from collections import deque
    q_nodes = deque([])
    q_nodes.append((1, BT_root))
    ls_level = []

    while len(q_nodes) != 0:
        (i_level, BT_node) = q_nodes.popleft()
        if i_level > len(ls_level):
            ls_level.append([BT_node._element])
        else:
            ls_level[-1].append(BT_node._element)

        lcnode = BT_node.get_lchild()
        rcnode = BT_node.get_rchild()
        if lcnode is not None:
            q_nodes.append((i_level + 1, lcnode))
        if rcnode is not None:
            q_nodes.append((i_level + 1, rcnode))

    return ls_level
