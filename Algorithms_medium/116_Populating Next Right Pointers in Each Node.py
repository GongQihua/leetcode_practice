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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
其实就是一个注意放next点的题目，所以每轮循环先加右点再加左点，每轮cur会清零，右点的next会是none
然后逐个扩展左点来对应next，这里给出加入记录点的输出，看一下应该就懂了
output：
node= 1
cur = None
next cur = 1
node= 3
cur = None
next cur = 3
node= 2
cur = <__main__.Node object at 0x7f4b07664b80>
next cur = 2
node= 7
cur = None
next cur = 7
node= 6
cur = <__main__.Node object at 0x7f4b076651b0>
next cur = 6
node= 5
cur = <__main__.Node object at 0x7f4b07665000>
next cur = 5
node= 4
cur = <__main__.Node object at 0x7f4b07664f10>
next cur = 4
'''