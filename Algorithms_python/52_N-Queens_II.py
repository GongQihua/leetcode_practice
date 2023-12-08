class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(i):
            if i == n:
                nonlocal ans
                ans += 1
                return
            for j in range(n):
                if cols[j] or dg[i + j] or udg[i - j + n]:
                    continue
                cols[j] = dg[i + j] = udg[i - j + n] = True
                dfs(i + 1)
                cols[j] = dg[i + j] = udg[i - j + n] = False
        cols = [False] * 10
        dg = [False] * 20
        udg = [False] * 20
        ans = 0
        dfs(0)
        return ans
'''
设计一个函数dfs(i)，表示从第i行开始搜索，搜索到的结果累加到答案中。

在第i行，我们枚举第i行的每一列，如果当前列不与前面已经放置的皇后发生冲突，那么我们就可以放置一个皇后，然后继续搜索下一行，即调用dfs(i+1)。

如果发生冲突，那么我们就跳过当前列，继续枚举下一列。

判断是否发生冲突，我们需要用三个数组分别记录每一列、每一条正对角线、每一条反对角线是否已经放置了皇后。

具体地，我们用cols数组记录每一列是否已经放置了皇后，用dg数组记录每一条正对角线是否已经放置了皇后，用udg数组记录每一条反对角线是否已经放置了皇后。
'''