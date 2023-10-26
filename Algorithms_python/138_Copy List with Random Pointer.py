"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        cur = head
        while cur:
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = node.next
        
        cur = head
        while cur:
            cur.next.random = None if cur.random is None else cur.random.next
            cur = cur.next.next
            
        copy = head.next
        cur = head
        while cur:
            next = cur.next
            cur.next = next.next
            next.next = None if next.next is None else next.next.next
            cur = cur.next
        return copy

'''
题目就是深复制。用三遍遍历来复制，思路：
首先，遍历链表，完成对每个旧节点的复制。
接着设置新节点的 ramdom 指针。
然后遍历链表，修改旧节点和新节点的指向，将旧节点指向下一个旧节点，而新节点指向下一个新节点。
最后返回第一个新节点即可。
'''