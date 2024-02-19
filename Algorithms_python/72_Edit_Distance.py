class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(1, n + 1):
            f[0][j] = j
        for i, a in enumerate(word1, 1): #enumerate()函数第二位代表起始位置
            f[i][0] = i
            for j, b in enumerate(word2, 1):
                if a == b:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
        return f[m][n]
'''
我们定义 f[i][j] 表示将 word1 的前 i 个字符转换成 word2 的前 j 个字符所使用的最少操作数。初始时 f[i][0] = i, f[0][j] = j。其中 i [1, m], j [0, n]。

考虑 f[i][j]：

-   如果 word1[i - 1] = word2[j - 1]，那么我们只需要考虑将 word1 的前 i - 1 个字符转换成 word2 的前 j - 1 个字符所使用的最少操作数，因此 f[i][j] = f[i - 1][j - 1]；
-   否则，我们可以考虑插入、删除、替换操作，那么 f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1。
'''