# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nums = []

        def dfs(root):
            if not root:
                return
            nums.append(root)
            dfs(root.left)
            dfs(root.right)

        if not root:
            return []
        dfs(root)
        n = len(nums)
        for i in range(n - 1):
            nums[i].right = nums[i + 1]
            nums[i].left = None
        nums[n - 1].left, nums[n - 1].right = None, None

        return nums[0]