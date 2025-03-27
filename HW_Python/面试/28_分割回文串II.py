'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。
返回符合要求的 最少分割次数 。
'''
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i+1, n):
                g[i][j] = s[i] == s[j] and g[i+1][j-1]
        f = list(range(n))
        for i in range(1, n):
            for j in range(i + 1):
                if g[j][i]:
                    f[i] = min(f[i], 1 + f[j-1] if j else 0)
        return f[-1]