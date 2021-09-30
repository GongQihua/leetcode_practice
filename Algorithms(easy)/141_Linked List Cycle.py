# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
'''
设定两个指针，快指针fast和满指针slow，初始位置相同
快指针每次走两步，慢指针每次走一步，不断循环。
当相遇时，说明链表存在环。如果循环结束依然没有相遇，说明链表不存在环。
'''