# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例
# 1：
#
#
# 输入：l1 = [1, 2, 4], l2 = [1, 3, 4]
# 输出：[1, 1, 2, 3, 4, 4]
# 示例
# 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例
# 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2
        return dummy.next