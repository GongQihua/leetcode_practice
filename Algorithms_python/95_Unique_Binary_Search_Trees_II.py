# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen(left, right):
            ans = []
            if left > right:
                ans.append(None)
            else:
                for i in range(left, right + 1):
                    left_tree = gen(left, i - 1)
                    right_tree = gen(i+1, right)
                    for l in left_tree:
                        for r in right_tree:
                            node = TreeNode(i, l, r)
                            #print('node = ', node)
                            ans.append(node)
            return ans
        return gen(1, n)

'''
从序列 1 ..n 中取出数字 i 并将其用作当前树的根。然后有 i - 1 个元素可用于构建左子树， n - i 个元素可用于构建右子树。
然后对序列 1 ... i - 1 重复上述步骤来构造所有左子树，然后对序列 i + 1 ... n 来构造所有右子树。
这样我们就有了一个根 i 和两个可能的左子树和右子树的列表。最后一步是遍历两个列表以将左右子树链接到根。
'''