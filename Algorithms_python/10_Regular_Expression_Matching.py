class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i,j):
            if j >= n:
                return i == m
            if j + 1 < n and p[j + 1] == '*':
                return dfs(i, j + 2) or (i < m and (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j))
            return i < m and (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j+ 1)

        m, n = len(s), len(p)
        return dfs(0,0)
'''
看完一圈下来dfs是最好理解的
构建dfs(i,j)，从(0,0)开始，检查本位，如果相等,i,j进一位， 如果有符号"*",j进两位并检查i下一位与j是否相等
最后如果同时到达结尾， 则返回True。
'''