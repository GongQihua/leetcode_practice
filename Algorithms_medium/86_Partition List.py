# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1, d2 = ListNode(), ListNode()
        t1, t2 = d1, d2
        while head:
            if head.val < x:
                t1.next = head
                t1 = t1.next
            else:
                t2.next = head
                t2 = t2.next
            head = head.next
        t1.next = d2.next
        t2.next = None
        return d1.next
'''
创建两个链表，一个存放小于 x 的节点，另一个存放大于等于 x 的节点
在排序的循环结束后，将t1.next接上d2.next，完成算法
'''