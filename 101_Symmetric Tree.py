# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.Symmetric(root.left, root.right)
    
    def Symmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.Symmetric(left.left, right.right) and self.Symmetric(left.right, right.left)
        #没懂，以后再写备注