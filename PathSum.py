class BinaryTree(object):
    """Binary Tree"""
    def __init__(self, element):
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
        from collections import deque
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
            

def find_sum(node_root, i_sum):
    # if node_root is None:
    #     return False
    if node_root is None:
        return False
    if node_root.get_lchild() is None and node_root.get_rchild() is None and node_root.get_value() == i_sum:
        return True
    if node_root.get_lchild() is None and node_root.get_rchild() is None and node_root.get_value() != i_sum:
        return False
    if node_root.get_lchild() is not None and node_root.get_rchild() is None:
        return find_sum(node_root.get_lchild(), i_sum - node_root.get_value())
    if node_root.get_lchild() is None and node_root.get_rchild() is not None:
        return find_sum(node_root.get_rchild(), i_sum - node_root.get_value())
    if node_root.get_lchild() is not None and node_root.get_rchild() is not None:
        return find_sum(node_root.get_lchild(), i_sum - node_root.get_value()) or find_sum(node_root.get_rchild(), i_sum - node_root.get_value())

def find_sum_test():
    import csv
    with open('PathSumTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            s_tree, s_sum = row[0].split(', ')
            ls_tree = s_tree.strip('{}').split(',')
            ls_vals = []
            for item in ls_tree:
                try:
                    ls_vals.append(int(item))
                except ValueError:
                    ls_vals.append(item)
            if not ls_vals:
                t_root = None
            else:
                t_root = BinaryTree(ls_vals[0])
                t_root.build_tree(ls_vals)
            i_sum = int(s_sum)
            b_found = find_sum(t_root, i_sum)
            print b_found, row[1]
            assert(b_found == (row[1] == 'true'))

def path_sum(node_root, i_sum):
    if not node_root:
        return []
    from collections import deque
    import copy
    q_nodes = deque()
    q_nodes.append([i_sum, node_root])
    ls_paths = []

    while len(q_nodes) != 0:
        ls_nodes = q_nodes.popleft()
        node_p = ls_nodes[-1]
        # print ls_nodes[0], node_p
        ls_nodes[0] -= node_p.get_value()
        if node_p.get_lchild() is None and node_p.get_rchild() is None and ls_nodes[0] == 0:
            ls_paths.append([item.get_value() for item in ls_nodes[1:]])
            continue
        if node_p.get_lchild() is not None:
            ls_cp_nodes = copy.copy(ls_nodes)
            ls_cp_nodes.append(node_p.get_lchild())
            q_nodes.append(ls_cp_nodes)
        if node_p.get_rchild() is not None:
            ls_cp_nodes = copy.copy(ls_nodes)
            ls_cp_nodes.append(node_p.get_rchild())
            q_nodes.append(ls_cp_nodes)
           
    return ls_paths

def path_sum_test():
    import csv
    with open('PathSum2Test.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            print row
            s_tree, s_sum = row[0].split(', ')
            ls_tree = s_tree.strip('{}').split(',')
            ls_vals = []
            for item in ls_tree:
                if item == '':
                    continue
                try:
                    ls_vals.append(int(item))
                except ValueError:
                    ls_vals.append(item)
            if not ls_vals:
                t_root = None
            else:
                t_root = BinaryTree(ls_vals[0])
                t_root.build_tree(ls_vals)
            i_sum = int(s_sum)
            try:
                ls_expected = map(lambda x: map(int, x.split(',')), row[1].strip('[]').split('],['))
            except ValueError:
                ls_expected = []
            set_expected = set(map(tuple, ls_expected))
            ls_actual = path_sum(t_root, i_sum)
            set_actual = set(map(tuple, ls_actual))
            print set_expected, set_actual
            assert(set_expected == set_actual)

if __name__ == '__main__':
    path_sum_test()
