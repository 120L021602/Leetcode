# 给你一个二叉树的根节点root ， 检查它是否轴对称。
#
#
#
# 示例
# 1：
#
#
# 输入：root = [1, 2, 2, 3, 4, 4, 3]
# 输出：true
# 示例
# 2：
#
#
# 输入：root = [1, 2, 2, null, 3, null, 3]
# 输出：false


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 后序遍历
        if not root:
            return True

        # compare用于比较两棵树是否相同
        def compare(left, right):
            if left and not right:
                return False
            elif not left and right:
                return False
            elif not left and not right:
                return True
            else:
                if left.val == right.val:
                    return compare(left.left, right.right) and compare(left.right, right.left)
                else:
                    return False

        return compare(root.left, root.right)