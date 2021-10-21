# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            if not root:
                return False
            targetSum -= root.val
            if not root.left and not root.right:
                return targetSum == 0
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
'''
直接开始遍历，targetSum减去遇到的数，看是否有一条枝干符合条件
递归地询问它的子节点是否能满足条件即可
'''