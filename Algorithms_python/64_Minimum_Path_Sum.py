class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[grid[0][0]] * n for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
'''
与前两题同一类型的题目，解题思路一致，唯一多加一步在选择dp[i][j]时要选最小解
用上左两个小的那个加上grid现在格子的值，去组成新的f数组，这样就能保证f的每一格都是路径值最小值
'''