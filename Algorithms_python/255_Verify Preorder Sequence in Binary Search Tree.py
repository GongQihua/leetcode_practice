class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stk = []
        last = -inf
        for x in preorder:
            if x < last:
                return False
            while stk and stk[-1] < x:
                last = stk.pop()
            stk.append(x)
        return True
'''
二叉搜索树先序遍历时，每次移向左子树时，值递减，移向右子树时，值递增。
因此，可以维护一个单调递减栈。遍历序列，若当前值大于栈顶元素，说明开始要进入右子树的遍历。只要栈顶元素比当前值小，就表示还是左子树，要移除，也就是从栈中弹出，直至栈顶元素大于当前值，或者栈为空。此过程要记录弹出栈的最后一个元素 last。
接下来继续往后遍历，之后右子树的每个节点，都要比 last 大，才能满足二叉搜索树，否则直接返回 false。
'''