# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            #print("cur=",cur.val)
            #print("dummy=",dummy.val)
            cur = cur.next
            #print("cur.next=",cur.val)
            #print("dummy.next=",dummy.val)
        cur.next = l1 or l2
        return dummy.next