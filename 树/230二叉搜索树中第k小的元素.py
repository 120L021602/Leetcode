# 给定一个二叉搜索树的根节点root ，和一个整数k ，请你设计一个算法查找其中第k小的元素（从1开始计数）。
#
#
#
# 示例
# 1：
#
#
# 输入：root = [3, 1, 4, null, 2], k = 1
# 输出：1
# 示例
# 2：
#
#
# 输入：root = [5, 3, 6, 2, 4, null, null, 1], k = 3
# 输出：3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 中序遍历
        self.k = k
        self.res = None

        def dfs(node):
            if not node or self.res is not None:
                return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.res