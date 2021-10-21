# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointA = headA
        pointB = headB
        while pointA != pointB:
            if pointA == None:
                pointA = headB
            else:
                pointA = pointA.next
            if pointB == None:
                pointB = headA
            else:
                pointB = pointB.next
            '''
            if 部分可缩写为：
            cur1 = headB if cur1 is None else cur1.next
            cur2 = headA if cur2 is None else cur2.
            '''
        return pointA
'''
使用两个指针 cur1, cur2 分别指向两个链表 headA, headB。
同时遍历链表，当 cur1 到达链表 headA 的末尾时，重新定位到链表 headB 的头节点；当 cur2 到达链表 headB 的末尾时，重新定位到链表 headA 的头节点。
若两指针相遇，所指向的结点就是第一个公共节点。若没相遇，说明两链表无公共节点，此时两个指针都指向 null。
'''