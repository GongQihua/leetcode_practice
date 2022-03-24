class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n  = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i -1][j] + dp[i][j - 1]
        return dp[-1][-1]
'''
相比上一题，要检测位置是不是有障碍物，有障碍物位置设置为0
假设 dp[i][j] 表示到达网格 (i,j) 的路径数，先初始化 dp 第一列和第一行的所有值，然后判断。
若 obstacleGrid[i][j] == 1,说明路径数为 0,dp[i][j] = 0;
若 obstacleGrid[i][j] == 0,则 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]。
'''