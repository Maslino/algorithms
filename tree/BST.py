# coding: utf8
from tree.binary_tree import BinaryTree
from tree.node import BinaryNode


class BST(object):
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def add(self, data):
        last_node = self.find_last(data)
        if last_node is None:
            self._root = BinaryNode(data)
            return

        if data < last_node.data:
            last_node.lchild = BinaryNode(data)
        elif data > last_node.data:
            last_node.rchild = BinaryNode(data)

    def remove(self, data):
        """remove node from BST, handle three cases:
                node without any child;
                node with only one child;
                node with two children;
        """
        node = self.find_last(data)
        if node is None or node.data != data:
            return

        parent = self.parent(node)

        if node.lchild is None and node.rchild is None:
            if parent is None:
                self._root = None
            else:
                if parent.lchild == node:
                    parent.lchild = None
                else:
                    parent.rchild = None
        elif node.lchild is not None and node.rchild is None:
            if parent is None:
                self._root = node.lchild
            else:
                if parent.lchild == node:
                    parent.lchild = node.lchild
                else:
                    parent.rchild = node.lchild
        elif node.lchild is None and node.rchild is not None:
            if parent is None:
                self._root = node.rchild
            else:
                if parent.lchild == node:
                    parent.lchild = node.rchild
                else:
                    parent.rchild = node.rchild
        else:
            p = node.rchild
            while p.lchild is not None:
                p = p.lchild

            pp = self.parent(p)
            assert pp is not None

            node.data = p.data
            if pp.lchild == p:
                pp.lchild = None
            else:
                pp.rchild = None

    def parent(self, node):
        if self._root is None or self._root == node:
            return None

        p = self._root
        parent = None
        while p is not None:
            if node.data < p.data:
                parent = p
                p = p.lchild
            elif node.data > p.data:
                parent = p
                p = p.rchild
            else:
                return parent

        return None

    @staticmethod
    def find_recursive(root, data):
        if root is None:
            return None

        if data < root.data:
            return BST.find_recursive(root.lchild, data)
        elif data > root.data:
            return BST.find_recursive(root.rchild, data)
        else:
            return root

    def find_non_recursive(self, data):
        node = self._root
        while node is not None:
            if data < node.data:
                node = node.lchild
            elif data > node.data:
                node = node.rchild
            else:
                return node

        return None

    def find_last(self, data):
        node = self._root
        prev = None
        while node is not None:
            prev = node
            if data < node.data:
                node = node.lchild
            elif data > node.data:
                node = node.rchild
            else:
                return node

        return prev


if __name__ == "__main__":
    bst = BST()
    BinaryTree.print_tree(bst.root)
    print

    data_tuple = (7, 3, 11, 1, 5, 9, 8)
    for data in data_tuple:
        bst.add(data)
        BinaryTree.print_tree(bst.root)
        print

    for data in data_tuple:
        assert bst.find_recursive(bst.root, data) is not None
        assert bst.find_non_recursive(data) is not None

    assert bst.find_non_recursive(10000) is None

    for data in data_tuple:
        bst.remove(data)
        BinaryTree.print_tree(bst.root)
        print
