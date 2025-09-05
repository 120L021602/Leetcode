# 给你链表的头节点head ，每k个节点一组进行翻转，请你返回修改后的链表。
#
# k是一个正整数，它的值小于或等于链表的长度。如果节点总数不是
# k的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
#
# 示例
# 1：
#
#
# 输入：head = [1, 2, 3, 4, 5], k = 2
# 输出：[2, 1, 4, 3, 5]
# 示例
# 2：
#
#
#
# 输入：head = [1, 2, 3, 4, 5], k = 3
# 输出：[3, 2, 1, 4, 5]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # 计算链表长度
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode()
        dummy.next = head
        pre = dummy

        while length >= k:
            cur = pre.next
            nex = cur.next
            # 翻转k-1次
            for _ in range(k - 1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            length -= k

        return dummy.next