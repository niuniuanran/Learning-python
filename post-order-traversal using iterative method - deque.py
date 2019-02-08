# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# left, right, root
from collections import deque

class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        tralist = deque()
        if not root:
            return []
        stack = [root]
        while stack:
            current = stack.pop()
            tralist.appendleft(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.appemd(current.right)
        return list(tralist)









