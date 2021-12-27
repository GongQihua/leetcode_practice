class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        Max = 1
        for j in range(n):
            for i in range(j + 1):
                if j - i < 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and Max < j -i + 1:
                    start = i
                    Max = j - i + 1
        return s[start:start + Max]

'''
动态规划法。
设 dp[i][j] 表示字符串 s[i..j] 是否为回文串。
当 j - i < 2，即字符串长度为 2 时，只要 s[i] == s[j]，dp[i][j] 就为 true。
当 j - i >= 2，dp[i][j] = dp[i + 1][j - 1] && s[i] == s[j]。
'''
