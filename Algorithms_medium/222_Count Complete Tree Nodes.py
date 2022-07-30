# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            res = 0
            while root:
                res += 1
                root = root.left
            return res
        
        if root is None:
            return 0
        left, right = depth(root.left), depth(root.right)
        if left == right:
            return (1 << left) + self.countNodes(root.right)
        return (1 << right) + self.countNodes(root.left)

'''
最简单的，直接遍历，算法复杂度O(n)
这里用另一种方法，利用完全二叉树特性，我们可以先对 root 的左右子树进行高度统计，分别记为 left, right。
若 left == right，说明左子树是一颗满二叉树。所以左子树的结点总数为 2^left - 1，加上 root 结点，就是 2^left，然后递归统计右子树即可。
若 left > right，说明右子树是一个满二叉树。所以右子树的结点总数为 2^right - 1，加上 root 结点，就是 2^right，然后递归统计左子树即可。
时间复杂度 O(log²n)。
'''