# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head
        n,cur = 0, head
        while cur:
            n, cur = n+1, cur.next
        k %= n
        if k == 0:
            return head
        
        slow = fast = head
        for _ in range(k):
            fast = fast.next
            #print('fast1 = ',fast.val)
        while fast.next:
            slow, fast = slow.next, fast.next
            #print('slow2 = ',slow.val)
            #print('fast2 = ',fast.val)
        start = slow.next
        slow.next = None
        fast.next = head
        return start
'''
代码分两段，用空格隔开了
上半段是检测特殊情况，如遇到那些总长度不够等的情况，直接返回head
下半段正式开始解题，设置双指针，快和慢，保证slow和fast拉开k长度的距离
最后就是slow就是数列最后一位，而原来的slow.next是数列第一位，fast是接过去数组的最后一位
并记得将fast.next指针指向原数组第一位，将链表接起来
'''