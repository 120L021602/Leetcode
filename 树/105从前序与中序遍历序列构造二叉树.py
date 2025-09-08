# 给定两个整数数组preorder和inorder ，其中preorder
# 是二叉树的先序遍历， inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
#
#
# 示例
# 1:
#
# 输入: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
# 输出: [3, 9, 20, null, null, 15, 7]
# 示例
# 2:
#
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        hashmap = {}
        n = len(inorder)
        for i in range(n):
            hashmap[inorder[i]] = i

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = hashmap[root_val]

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        left_preorder = preorder[1: 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root