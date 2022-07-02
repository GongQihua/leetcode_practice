# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root.left is None:
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return new_root

'''
其实就是一层层向原root左边扩展成新节点然后反转，具体思路：
若根节点为空，或者根节点左子树为空，直接返回根节点。
递归处理左子树，返回的根节点 newRoot，也就是二叉树上下翻转后的根节点。
然后处理根节点 root，根节点变成左子节点的右子节点，而根节点的右子节点变成左子节点的左子节点。
接着将根节点 root 的左右子节点置为空，最后返回 newRoot 即可。
'''