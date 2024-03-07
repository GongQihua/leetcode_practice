# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            nonlocal prev, first, second
            if root:
                dfs(root.left)
                if prev:
                    if first is None and root.val < prev.val:
                        first = prev
                    if first and root.val < prev.val:
                        second = root
                prev = root
                dfs(root.right)
        
        prev = first = second = None
        dfs(root)
        first.val, second.val = second.val, first.val

'''
设置两个变量用于存储两个要交换的异常值用于交换，然后用dfs向一个方向搜索比较
这里是向左树搜索，逐层扩展，左树不能比根大，一层层往下找异常值
'''