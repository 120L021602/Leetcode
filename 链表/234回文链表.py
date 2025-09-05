# 给你一个单链表的头节点head ，请你判断该链表是否为回文链表。如果是，返回true ；否则，返回false 。
#
#
#
# 示例
# 1：
#
#
# 输入：head = [1, 2, 2, 1]
# 输出：true
# 示例
# 2：
#
#
# 输入：head = [1, 2]
# 输出：false
#
# 提示：
#
# 链表中节点数目在范围[1, 105]
# 内
# 0 <= Node.val <= 9


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 放到数组里面进行判断
class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        nums = []
        if not head:
            return True
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True


# 快慢指针+反转后半部分链表
class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 找到中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分链表
        pre, cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        # 判断回文
        left, right = head, pre
        while right:  # 注意这里是right，因为right长度小于等于left
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
