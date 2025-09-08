# 给你一个整数数组nums ，其中元素已经按升序排列，请你将其转换为一棵平衡二叉搜索树。
#
#
#
# 示例
# 1：
#
#
# 输入：nums = [-10, -3, 0, 5, 9]
# 输出：[0, -3, 9, -10, null, 5]
# 解释：[0, -10, 5, null, -3, null, 9]
# 也将被视为正确答案：
#
# 示例
# 2：
#
#
# 输入：nums = [1, 3]
# 输出：[3, 1]
# 解释：[1, null, 3]
# 和[3, 1]
# 都是高度平衡二叉搜索树。
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # 二分
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node

        return build(0, len(nums) - 1)