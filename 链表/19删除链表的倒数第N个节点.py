# 给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。
#
#
#
# 示例
# 1：
#
#
# 输入：head = [1, 2, 3, 4, 5], n = 2
# 输出：[1, 2, 3, 5]
# 示例
# 2：
#
# 输入：head = [1], n = 1
# 输出：[]
# 示例
# 3：
#
# 输入：head = [1, 2], n = 1
# 输出：[1]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        fast = dummy

        for _ in range(n):
            fast = fast.next

        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow指向要被删除的节点
        slow.next = slow.next.next

        return dummy.next
