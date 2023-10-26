# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        left = False
        ans = []
        q = deque([root])
        while q:
            t =[]
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if left:
                t.reverse()
            ans.append(t)
            left = not left
        return ans

'''
与上一题几乎类似，写法和思路都没有变化，就加一条在每层的内容结束的时候反转，就能完美符合题目
'''