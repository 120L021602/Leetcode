# 给定一个二叉树的根节点root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
# 示例
# 1：
#
# 输入：root = [1, 2, 3, null, 5, null, 4]
#
# 输出：[1, 3, 4]
#
# 解释：
#
#
#
# 示例
# 2：
#
# 输入：root = [1, 2, 3, 4, null, null, null, 5]
#
# 输出：[1, 3, 4, 5]
#
# 解释：
#
#
#
# 示例
# 3：
#
# 输入：root = [1, null, 3]
#
# 输出：[1, 3]
#
# 示例
# 4：
#
# 输入：root = []
#
# 输出：[]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        que = deque()
        que.append(root)

        while que:
            n = len(que)
            node = que[-1]
            res.append(node.val)
            for i in range(n):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return res