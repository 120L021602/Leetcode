# 给你一个二叉树的根节点root ，判断其是否是一个有效的二叉搜索树。
#
# 有效二叉搜索树定义如下：
#
# 节点的左子树只包含严格小于当前节点的数。节点的右子树只包含严格大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例
# 1：
#
#
# 输入：root = [2, 1, 3]
# 输出：true
# 示例
# 2：
#
#
# 输入：root = [5, 1, 4, null, null, 3, 6]
# 输出：false
# 解释：根节点的值是
# 5 ，但是右子节点的值是
# 4 。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # 检查中序遍历序列是否是递增的
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        if not root:
            return True
        if not root.left and not root.right:
            return True

        ans = []
        dfs(root)
        n = len(ans)
        for i in range(1, n):
            if ans[i] <= ans[i - 1]:
                return False
        return True

