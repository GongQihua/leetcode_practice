# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: TreeNode):
        height = 0
        while root:
            root = root.left
            height += 1
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        if leftheight == rightheight:
            return (2 ** leftheight - 1) + self.countNodes(root.right) + 1
        else:
            return (2 ** rightheight - 1) + self.countNodes(root.left) + 1