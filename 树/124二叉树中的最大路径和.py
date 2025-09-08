# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def maxGain(node):
            if not node:
                return 0

            left_max = max(maxGain(node.left), 0)
            right_max = max(maxGain(node.right), 0)

            cur_max = node.val + left_max + right_max
            self.max_sum = max(self.max_sum, cur_max)

            return node.val + max(left_max, right_max)

        maxGain(root)
        return self.max_sum