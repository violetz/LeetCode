class BinaryTree(object):
    """Binary Tree"""
    
    from collections import deque
        
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

def complete_next_right(node_root):
    node_root.next_right = None
    node_most_left = node_root
    
    while node_most_left:
        node_cross = node_most_left
        while node_cross:
            if node_cross.get_lchild():
                node_cross.get_lchild().next_right = node_cross.get_rchild()
            else:
                break
            if node_cross.next_right:
                node_cross.get_rchild().next_right = node_cross.next_right.get_lchild()
            else:
                node_cross.get_rchild().next_right = None
            node_cross = node_cross.next_right
        node_most_left = node_most_left.get_lchild()

    return node_root
        

def next_right(node_root):
    from collections import deque
    q_nodes = deque()
    q_nodes.append(node_root)
    i_cur_level_cnt = 1
    i_next_level_cnt = 0

    while q_nodes:
        node_cur = q_nodes.popleft()
        i_cur_level_cnt -= 1
        if node_cur.get_lchild():
            q_nodes.append(node_cur.get_lchild())
            i_next_level_cnt += 1
        if node_cur.get_rchild():
            q_nodes.append(node_cur.get_rchild())
            i_next_level_cnt += 1
        if i_cur_level_cnt == 0:
            node_cur.next_right = None
            i_cur_level_cnt = i_next_level_cnt
            i_next_level_cnt = 0
        else:
            node_cur.next_right = q_nodes[0]

    return node_root
    
