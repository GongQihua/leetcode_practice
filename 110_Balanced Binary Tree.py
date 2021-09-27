# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return -1
            return 1 + max(height(root.left), height(root.right))
        
        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        '''
        height function寻找左右树的最大深度
        返回语句同时满足三情况，左右树最大深度不超过1，且有左右树
        注意root = [] 的情况
        '''