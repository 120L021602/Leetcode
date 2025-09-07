# 给定一个二叉树的根节点root ，返回它的中序遍历 。
#
#
#
# 示例
# 1：
#
#
# 输入：root = [1, null, 2, 3]
# 输出：[1, 3, 2]
# 示例
# 2：
#
# 输入：root = []
# 输出：[]
# 示例
# 3：
#
# 输入：root = [1]
# 输出：[1]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            []

        res = []
        stack = deque()
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right

        return res

