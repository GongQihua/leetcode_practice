class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(i:int):
            if i == n:
                ans.append(["".join(row) for row in g])
                return
            for j in range(n):
                if col[j] + dg[i + j] + udg[n - i + j] == 0:
                    g[i][j] = "Q"
                    col[j] = dg[i + j] = udg[n - i + j] = 1
                    dfs(i + 1)
                    col[j] = dg[i + j] = udg[n - i + j] = 0
                    g[i][j] = "."
        ans = []
        g = [["."] * n for _ in range(n)]
        col = [0] * n
        dg = [0] * (n << 1)
        udg = [0] * (n << 1)
        dfs(0)
        return ans
'''
先把空的表打好，然后dfs，还要一个计数的表。
dfs的思路是，现在一个位置放Q然后把Q涉及到位置的值改成1，往下dfs
记得置位
'''