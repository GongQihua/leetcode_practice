# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        v = postorder[-1]
        root = TreeNode(val=v)
        i = inorder.index(v)
        root.left = self.buildTree(inorder[: i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        return root

'''
与上一题的解法和思路是一模一样的，记得左右树的分割位置不要搞错，从i的那个位置开始，想一想
'''