# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else (left or right)

'''
思路，分情况讨论：根据“最近公共祖先”的定义，若 root 是 p, q 的最近公共祖先 ，则只可能为以下情况之一：
如果 p 和 q 分别是 root 的左右节点，那么 root 就是我们要找的最近公共祖先；
如果 p 和 q 都是 root 的左节点，那么返回 lowestCommonAncestor(root.left, p, q)；
如果 p 和 q 都是 root 的右节点，那么返回 lowestCommonAncestor(root.right, p, q)。
边界条件讨论：
如果 root 为 null，则说明我们已经找到最底了，返回 null 表示没找到；
如果 root 与 p 相等或者与 q 相等，则返回 root；
如果左子树没找到，递归函数返回 null，证明 p 和 q 同在 root 的右侧，那么最终的公共祖先就是右子树找到的结点；
如果右子树没找到，递归函数返回 null，证明 p 和 q 同在 root 的左侧，那么最终的公共祖先就是左子树找到的结点。
'''