# coding: utf8


class BinaryNode(object):
    def __init__(self, data, lchild=None, rchild=None):
        self._data = data
        self._lchild = lchild
        self._rchild = rchild

    def __str__(self):
        return str(self._data)

    @property
    def data(self):
        return self._data

    def get_lchild(self):
        return self._lchild

    def set_lchild(self, lchild):
        self._lchild = lchild

    def get_rchild(self):
        return self._rchild

    def set_rchild(self, rchild):
        self._rchild = rchild

    lchild = property(get_lchild, set_lchild)
    rchild = property(get_rchild, set_rchild)


if __name__ == "__main__":
    root = BinaryNode(1, BinaryNode(2), BinaryNode(3))
    for node in (root, root.lchild, root.rchild):
        if node is not None:
            print node.data, node.lchild, node.rchild
