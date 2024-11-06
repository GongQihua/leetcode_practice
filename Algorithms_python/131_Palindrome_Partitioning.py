class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i: int):
            if i == n:
                ans.append(t[:])
                return
            for j in range(i, n):
                if f[i][j]:
                    t.append(s[i:j+1])
                    dfs(j+1)
                    t.pop()
                    
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]
        t = []
        ans = []
        dfs(0)
        return ans
'''
假设我们当前搜索到字符串的第 i 个字符，且 s[0..i−1] 位置的所有字符已经被分割成若干个回文串，并且分割结果被放入了答案数组 ans 中，那么我们就需要枚举下一个回文串的右边界 j，使得 s[i..j] 是一个回文串。

因此，我们可以从 i 开始，从小到大依次枚举 j。对于当前枚举的 j 值，我们使用双指针的方法判断 s[i..j] 是否为回文串：如果 s[i..j] 是回文串，那么就将其加入答案数组 ans 中，并以 j+1 作为新的 i 进行下一层搜索，并在未来的回溯时将 s[i..j] 从 ans 中移除。
'''