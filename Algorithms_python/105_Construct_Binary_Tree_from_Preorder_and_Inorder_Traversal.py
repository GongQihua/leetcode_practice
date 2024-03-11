# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        v = preorder[0]
        root = TreeNode(val = v)
        i = inorder.index(v)
        root.left = self.buildTree(preorder[1: 1+i], inorder[:i])
        root.right = self.buildTree(preorder[1+i: ], inorder[i + 1: ])
        return root

'''
前序遍历：先遍历根节点，再遍历左右子树；中序遍历：先遍历左子树，再遍历根节点，最后遍历右子树。
这题思路是：前序序列的第一个结点做为根节点，然后在中序序列中找到根节点的位置 i，
再将中序序列划分为左子树 inorder[:i] 、右子树 inorder[i+1:]，以此来构造整个树。
'''