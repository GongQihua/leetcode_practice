# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None
            p = (left + right) // 2
            
            root = TreeNode(nums[p])
            root.left = build(left, p-1)
            root.right = build(p+1, right)
            return root
        return build(0, len(nums)-1)
'''
选择左中间元素：p = (left + right) // 2
启动根：root = TreeNode(nums[p])
递归计算左右子树：root.left = helper(left, p - 1)
root.right = helper(p + 1, right)
'''