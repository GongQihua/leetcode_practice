class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
'''
动态规划题，想法是：
假设 dp[i][j] 表示到达网格 (i,j) 的路径数，则 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]。
'''