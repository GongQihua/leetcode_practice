# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        while cur:
            next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = next
            #print(dummy)
        return dummy.next

'''
创建虚拟头节点dummy，遍历链表，将每个节点依次插入dummy的下一个节点。遍历结束，返回dummy.next。
'''