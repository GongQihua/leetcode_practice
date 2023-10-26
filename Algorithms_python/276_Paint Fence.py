class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = k
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) * (k - 1)
            dp[i][1] = dp[i - 1][0]
        return sum(dp[-1])
'''
动态规划，
定义dp[i][0]表示栅栏[0....i]且最后两个栅栏颜色不同的方案数，$dp[i][1]$ 表示栅栏[0...i]且最后两个栅栏颜色相同的方案数。
答案就是最后dp[]的累加
时间复杂度O(n)，空间复杂度O(1)。其中n是栅栏柱的数量。
'''