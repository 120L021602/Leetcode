# 给你一棵二叉树的根节点，返回该树的直径。
#
# 二叉树的直径是指树中任意两个节点之间最长路径的长度 。这条路径可能经过也可能不经过根节点root 。
#
# 两节点之间路径的长度由它们之间边数表示。
#
#
#
# 示例
# 1：
#
#
# 输入：root = [1, 2, 3, 4, 5]
# 输出：3
# 解释：3 ，取路径[4, 2, 1, 3]
# 或[5, 2, 1, 3]
# 的长度。
# 示例
# 2：
#
# 输入：root = [1, 2]
# 输出：1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        ans = [0]
        self.dfs(root, ans)
        return ans[0]

    def dfs(self, root, ans):
        if not root:
            return 0

        left = self.dfs(root.left, ans)
        right = self.dfs(root.right, ans)

        cur = left + right
        ans[0] = max(ans[0], cur)

        return max(left, right) + 1