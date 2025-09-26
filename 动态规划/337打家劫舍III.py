# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为root 。
#
# 除了root之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果
# 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
#
# 给定二叉树的root 。返回在不触动警报的情况下 ，小偷能够盗取的最高金额 。
#
#
#
# 示例
# 1:
#
# 输入: root = [3, 2, 3, null, 3, null, 1]
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额
# 3 + 3 + 1 = 7
# 示例
# 2:
#
# 输入: root = [3, 4, 5, 1, 3, null, 1]
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额
# 4 + 5 = 9


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        dp_root = self.traversal(root)
        return max(dp_root)

    # 对于树中每个节点，遍历完该节点都返回一个列表[a, b]
    # a表示不偷该节点获得的最大收益，b表示偷该节点获得的最大收益

    def traversal(self, root):
        if not root:
            return [0, 0]

        dp = [0, 0]

        left = self.traversal(root.left)
        right = self.traversal(root.right)

        dp[0] = max(left) + max(right)
        dp[1] = root.val + left[0] + right[0]

        return dp
