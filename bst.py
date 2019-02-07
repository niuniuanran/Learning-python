import random


class BSNode(object):

    def __init__(self, key, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key

    def str(self):
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left.str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right.str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos

        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)

            # middle是出去空格外中间部分的长度
            # width是line的总长度
        label.center(middle, '·')
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
                self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.':
            label = ' ' + label[1:]
        if label[-1] == '.':
            label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle - 2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) + right_line
                 for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        return '\n'.join(self.str()[0])

    def in_order(self):
        s = []
        current = self
        while current is not None:
            if current.left is not None:
                s.extend(current.left.in_order())
            s.append(current.key)
            if current.right is not None:
                s.extend(current.right.in_order())
            return s
        return


class BSTree(object):
    def __init__(self, root_node):
        self.root = root_node

    def insert(self, new_key):
        target = new_key
        new_node = BSNode(key=new_key, left=None, right=None)

        current = self.root
        while True:
            if target >= current.key:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return new_node
                else:
                    current = current.right
                    continue
            else:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return new_node
                else:
                    current = current.left
                    continue


def main():
    array = [random.randint(1, 100) for _ in range(0, 10)]
    # array = [91, 31, 59, 35, 60, 57, 19, 61, 19, 72]

    print(array)
    root = BSNode(key=array[0])
    tree = BSTree(root_node=root)
    for key in array[1:]:
        tree.insert(key)
    s = tree.root.in_order()
    print(s)
    print(tree.root)


if __name__ == "__main__":
    main()
