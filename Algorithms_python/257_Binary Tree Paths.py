# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root):
            if root is None:
                return
            t.append(str(root.val))
            if root.left is None and root.right is None:
                ans.append('->'.join(t))
            dfs(root.left)
            dfs(root.right)
            t.pop()
            
        t = []
        ans = []
        dfs(root)
        return ans
'''
已经遇到过很多类似的题目了，dfs直接写就行了
'''