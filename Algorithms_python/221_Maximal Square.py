class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        mx = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                    mx = max(mx, dp[i + 1][j + 1])
        return mx * mx

'''
思路就是找最大变长然后乘起来，
具体就是用动态规划。
设 dp[i + 1][j + 1] 表示以下标 (i, j) 作为正方形右下角的最大正方形边长。
当 matrix[i][j] == '1', dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1，否则 dp[i + 1][j + 1] = 0。
'''