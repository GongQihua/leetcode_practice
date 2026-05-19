# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightmost = dict()
        max_depth = -1
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if node is not None:
                max_depth = max(max_depth, depth)
                rightmost.setdefault(depth, node.val)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return [rightmost[depth] for depth in range(max_depth + 1)]