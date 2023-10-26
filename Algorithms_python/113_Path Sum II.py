# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, s):
            if root is None:
                return
            t.append(root.val)
            s += root.val
            if root.left is None and root.right is None:
                if s == targetSum:
                    ans.append(t[:])
            dfs(root.left, s)
            dfs(root.right, s)
            t.pop()
            
        ans = []
        t = []
        if root is None:
            return ans
        dfs(root, 0)
        return ans

'''
想法就是用dfs，这样能逐层往下深挖树，在dfs的过程中做累加，与目标值做对比，这样就能检验每一条分叉
'''