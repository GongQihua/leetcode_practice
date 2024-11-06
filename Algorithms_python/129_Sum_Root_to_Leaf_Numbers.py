# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, num):
            if root is None:
                return 0
            s = 10 * num + root.val
            if root.left is None and root.right is None:
                return s
            return dfs(root.left, s) + dfs(root.right, s)
        
        return dfs(root, 0)

'''
很简单的题目，dfs逐层挖树，然后累加
唯一注意挖树的过程中，挖一层要进一位，即这行代码“s = 10 * num + root.val”
'''