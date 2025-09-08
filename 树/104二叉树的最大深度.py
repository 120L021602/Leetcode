# 给定一个二叉树root ，返回其最大深度。
#
# 二叉树的最大深度是指从根节点到最远叶子节点的最长路径上的节点数。
#
#
#
# 示例
# 1：
#
#
#
#
#
# 输入：root = [3, 9, 20, null, null, 15, 7]
# 输出：3
# 示例
# 2：
#
# 输入：root = [1, null, 2]
# 输出：2


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1