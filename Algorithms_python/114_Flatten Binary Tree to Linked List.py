# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

'''
因为要满足复杂度的原因，思路是把原root的右节点换到原左节点右分支的最后，然后把原左节点带着树移到右节点
如此反复就能得到一个只有右节点的树
以题目给的[1,2,5,3,4,null,6]为例子，这是变换过程的输出结果：
root: TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 4, left: None, right: TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}}}}
root: TreeNode{val: 2, left: None, right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: TreeNode{val: 5, left: None, right: TreeNode{val: 6, left: None, right: None}}}}}
'''