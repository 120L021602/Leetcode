# 给你链表的头结点head ，请将其按升序排列并返回排序后的链表 。
#
#
#
# 示例
# 1：
#
#
# 输入：head = [4, 2, 1, 3]
# 输出：[1, 2, 3, 4]
# 示例
# 2：
#
#
# 输入：head = [-1, 5, 3, 4, 0]
# 输出：[-1, 0, 3, 4, 5]
# 示例
# 3：
#
# 输入：head = []
# 输出：[]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.mergeTwoList(left, right)

    def mergeTwoList(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
