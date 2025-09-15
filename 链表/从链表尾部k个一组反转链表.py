class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 反转整个链表
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# 反转从 head 开始的 k 个节点，返回新 head 和 new tail 的 next
def reverse_k_nodes(head, k):
    prev = None
    curr = head
    count = 0
    # 先检查是否有 k 个节点
    temp = head
    for _ in range(k):
        if not temp:
            return head, None  # 不足 k，不翻转
        temp = temp.next

    # 正式反转 k 个节点
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    head.next = curr  # 原 head 成了 tail，接上后续部分
    return prev, head  # new_head, new_tail

def reverse_from_tail_k_group(head: ListNode, k: int) -> ListNode:
    # Step 1: 整体反转链表
    head = reverse_list(head)

    # Step 2: 正向每 k 个节点反转
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        new_head, new_tail = reverse_k_nodes(curr, k)
        if new_tail is None:
            break  # 不足 k 个，不翻转

        prev.next = new_head
        prev = new_tail
        curr = new_tail.next

    # Step 3: 再次整体反转链表
    return reverse_list(dummy.next)