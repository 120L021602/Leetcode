# 给你二叉树的根节点root ，返回其节点值的层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例
# 1：
#
#
# 输入：root = [3, 9, 20, null, null, 15, 7]
# 输出：[[3], [9, 20], [15, 7]]
# 示例
# 2：
#
# 输入：root = [1]
# 输出：[[1]]
# 示例
# 3：
#
# 输入：root = []
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        que = deque()
        que.append(root)

        while que:
            n = len(que)
            cur_list = []
            for _ in range(n):
                node = que.popleft()
                cur_list.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(cur_list)

        return res