# coding: utf8
from queue.queue import Queue
from tree.node import BinaryNode


class BinaryTree(object):
    @staticmethod
    def create_tree():
        data = raw_input("please input a char(# for blank): ")
        if data == "#":
            return None

        node = BinaryNode(data)
        node.lchild = BinaryTree.create_tree()
        node.rchild = BinaryTree.create_tree()

        return node

    @staticmethod
    def pre_order_traverse(root):
        pass

    @staticmethod
    def in_order_traverse(root):
        pass

    @staticmethod
    def post_order_traverse(root):
        pass

    @staticmethod
    def level_order_traverse(root):
        if root is None:
            return

        queue = Queue()
        queue.enqueue(root)
        while not queue.is_empty():
            node = queue.dequeue()
            print node,
            if node.lchild is not None:
                queue.enqueue(node.lchild)
            if node.rchild is not None:
                queue.enqueue(node.rchild)

        print

    @staticmethod
    def print_tree(root):
        if root is None:
            print None,
            return

        print root.data, "(",
        BinaryTree.print_tree(root.lchild)
        print ", ",
        BinaryTree.print_tree(root.rchild)
        print ")",


if __name__ == "__main__":
    root = BinaryTree.create_tree()
    BinaryTree.level_order_traverse(root)
    BinaryTree.print_tree(root)