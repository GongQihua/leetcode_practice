# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            nonlocal prev
            if root is None:
                return True
            if not dfs(root.left):
                return False
            if prev >= root.val:
                return False
            prev = root.val
            if not dfs(root.right):
                return False
            return True
        
        prev = float('-inf')
        return dfs(root)

'''
中序遍历，若是一个有效的二叉搜索树，那么遍历到的序列应该是单调递增的。
所以只要比较判断遍历到的当前数是否 >= 上一个数即可。
设定一个无限小的变量，依次比较然后迭代。
'''