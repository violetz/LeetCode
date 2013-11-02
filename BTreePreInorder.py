class BinaryTree(object):
    def __init__(self, element):
        self.element = element
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        """preorder transverse the tree"""
        return str(self.preorder())

    def preorder(self):
        if self is None:
            return
        else:
            return [self.element, [self.left_child], [self.right_child]]

    def inorder(self):
        if self is None:
            return
        else:
            return [[self.left_child], self.element, [self.right_child]]

    def postorder(self):
        if self is None:
            return
        else:
            return [[self.left_child], [self.right_child], self.element

    def get_root_value(self):
        return self.element

    def set_root_value(self, val):
        self.element = val

    def insert_left(self, element):
        lchild = self.left_child
        self.left_child = BinaryTree(element)
        if lchild is not None:
            self.left_child.left_child = lchild

    def insert_right(self, element):
        rchild = self.right_child
        self.right_child = BinaryTree(element)
        if rchild is not None:
            sel.right_child.right_child = rchild

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

def pre_in_tree(ls_pre, ls_in):
    if len(ls_pre) == len(ls_in) == 1:
        return BinaryTree(ls_pre[0])
    else:
        root = BinaryTree(ls_pre[0])
        ind_root = ls_in.index(ls_pre[0])
        left_child = pre_in_tree(ls_pre[1:ind_root+1], ls_in[0:ind_root])
        right_child = pre_in_tree(ls_pre[ind_root+1:], ls_in[ind_root+1:])
        root.left_child = left_child
        root.right_child = right_child
        return root
        
def in_post_tree(ls_in, ls_post):
    if len(ls_in) == len(ls_post) == 1:
        return BinaryTree(ls_post[0])
    else:
        root = BinaryTree(ls_post[-1])
        ind_root = ls_in.index(ls_post[-1])
        root.left_child = in_post_tree(ls_in[:ind_root], ls_post[:ind_root])
        root.right_child = in_post_tree(ls_in[ind_root+1:], ls_post[ind_root:-1])
        return root
