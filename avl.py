import bst
import random


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right))+1


class AVLTree(bst.BSTree):
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent

        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y

        x.right = y.left
        if x.right is not None:
            x.right.parent = x

        y.left = x
        x.parent = y

        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right =y

        x.left = y.right
        if x.left is not None:
            x.left.parent = x

        y.right = x
        x.parent = y

        update_height(x)
        update_height(y)

    def re_balance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, new_key):
        node = super(AVLTree, self).insert(new_key)
        self.re_balance(node)


def main():
    array = [random.randint(1, 100) for _ in range(0, 100)]
    # array = [91, 31, 59, 35, 60, 57, 19, 61, 19, 72]
    print(array)
    root = bst.BSNode(key=array[0])
    tree = AVLTree(root_node=root)
    for key in array[1:]:
        tree.insert(key)
    s = tree.root.in_order()
    print(s)
    print(tree.root)
    print(tree.root.right.left.left)


if __name__ == "__main__":
    main()
