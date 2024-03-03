# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
'''
交换方法：
使用三个指针变量 pre、curr、next 来记录反转的过程中需要的变量，它们的意义如下：

curr：指向待反转区域的第一个节点 left；
next：永远指向 curr 的下一个节点，循环过程中，curr 变化以后 next 会变化；
pre：永远指向待反转区域的第一个节点 left 的前一个节点，在循环过程中不变。

操作过程：

先将 curr 的下一个节点记录为 next；
执行操作 ①：把 curr 的下一个节点指向 next 的下一个节点；
执行操作 ②：把 next 的下一个节点指向 pre 的下一个节点；
执行操作 ③：把 pre 的下一个节点指向 next。
具体可以去看一下官方题解的图，更清晰一点
'''