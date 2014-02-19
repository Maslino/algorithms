# coding: utf8
from queue.queue import Queue
from stack.stack import Stack
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
        """ please refer to http://learn.hackerearth.com/tutorial/trees/19/iterative-tree-traversals/
        """
        stack = Stack()
        p = root
        while True:
            while p is not None:
                # print node and store the node in the stack
                print p,
                stack.push(p)
                p = p.lchild

            # visit the right child
            if not stack.is_empty():
                p = stack.pop()
                p = p.rchild

            if stack.is_empty() and p is None:
                break

        print

    @staticmethod
    def in_order_traverse(root):
        """ please refer to http://learn.hackerearth.com/tutorial/trees/19/iterative-tree-traversals/
        """
        stack = Stack()
        p = root
        while True:
            while p is not None:
                # store a node in the stack and visit its left child
                stack.push(p)
                p = p.lchild

            # if there are nodes in the stack to which we can move up, then pop it
            if not stack.is_empty():
                p = stack.pop()
                print p,
                # visit the right child
                p = p.rchild

            if stack.is_empty() and p is None:
                break

        print

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
    BinaryTree.pre_order_traverse(root)
    BinaryTree.in_order_traverse(root)
    BinaryTree.print_tree(root)