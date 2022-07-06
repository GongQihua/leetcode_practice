# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def inorder(root):
            if root:
                inorder(root.left)
                self.vals.append(root.val)
                inorder(root.right)
        
        self.cur = 0
        self.vals = []
        inorder(root)

    def next(self) -> int:
        res = self.vals[self.cur]
        self.cur += 1
        return res

    def hasNext(self) -> bool:
        return self.cur < len(self.vals)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

'''
中序遍历，将二叉搜索树每个结点的值保存在列表 vals 中。用 cur 指针记录外部即将遍历的位置，初始化为 0。
调用 next() 时，返回 vals[cur]，同时 cur 指针自增。调用 hasNext() 时，
判断 cur 指针是否已经达到 len(vals) 个数，若是，说明已经遍历结束，返回 false，否则返回 true。
'''