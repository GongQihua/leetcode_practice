class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            if i >= m and j >= n:
                return True
            k = i + j
            if i < m  and s1[i] == s3[k] and dfs(i+1, j):
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j+1):
                return True
            return False

        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        return dfs(0, 0)

'''
每次从 s1 或 s2 的首部取一个字符，最终组成 s3，用记忆化搜索或者动态规划都可以解决
这里用的python的dfs，逐层搜索
'''