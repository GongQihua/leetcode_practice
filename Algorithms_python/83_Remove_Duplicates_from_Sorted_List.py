# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next #迭代next的数字
            else:
                cur = cur.next #更新位置
        return head
'''
具体地，我们从指针 cur\textit{cur}cur 指向链表的头节点，随后开始对链表进行遍历。

如果当前 cur\textit{cur}cur 与 cur.next\textit{cur.next}cur.next 对应的元素相同，那么我们就将 cur.next\textit{cur.next}cur.next 从链表中移除；

否则说明链表中已经不存在其它与 cur\textit{cur}cur 对应的元素相同的节点，因此可以将 cur\textit{cur}cur 指向 cur.next\textit{cur.next}cur.next。

当遍历完整个链表之后，我们返回链表的头节点即可。
'''