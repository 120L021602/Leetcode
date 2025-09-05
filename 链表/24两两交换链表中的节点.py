# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#
#
#
# 示例
# 1：
#
#
# 输入：head = [1, 2, 3, 4]
# 输出：[2, 1, 4, 3]
# 示例
# 2：
#
# 输入：head = []
# 输出：[]
# 示例
# 3：
#
# 输入：head = [1]
# 输出：[1]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            tmp1 = cur.next
            tmp2 = cur.next.next
            cur.next = tmp2
            tmp1.next = tmp2.next
            tmp2.next = tmp1
            cur = cur.next.next

        return dummy.next