"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None or (root.left is None and root.right is None):
            return root
        q = deque([root])
        while q:
            size = len(q)
            cur = None
            for _ in range(size):
                node = q.popleft()
                #print('node=', node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                #print('cur =',cur)
                node.next = cur
                cur = node
                #print('next cur =',cur.val)
        return root

'''
不知道这题意义，上一题原装代码，直接用，貌似不用优化，反正我直接用了
'''