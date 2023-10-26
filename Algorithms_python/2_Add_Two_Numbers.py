# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        cur = dummy
        while l1 or l2 or carry:
            s = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + carry
            carry, mod = divmod(s, 10)
            cur.next = ListNode(mod)
            cur = cur.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        return dummy.next
'''
写个循环，依次相加两个链表中的对应数字
用divmod同时取除数和余数
余数输入新建的链表，除数变为carry，加入下一位的两数相加
给的两链表可能数字长度不一，记得检查，16，17行，若超过最后位数，记为None，12行相加数为0
'''