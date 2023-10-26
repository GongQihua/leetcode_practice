# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(head.val, head)
        pre, cur = dummy, head
        while cur:
            if pre.val <= cur.val:
                pre, cur = cur, cur.next
                continue
            p = dummy
            while p.next.val <= cur.val:
                p = p.next
            t = cur.next
            cur.next = p.next
            p.next = cur
            pre.next = t
            cur = t
        return dummy.next

'''
遍历链表，每次将遍历到的结点 cur 与前一个结点 pre 进行值比较：
若结点 cur 的值比 pre 的大，说明当前 cur 已在正确的位置，直接往下遍历。
否则，从链表第一个结点开始遍历，将结点 cur 插入到正确的位置。
依次遍历，直至 cur 指向空，遍历结束。
'''