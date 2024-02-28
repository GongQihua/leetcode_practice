class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache #这行可以在dfs中加载缓存，对速度影响很大
        def dfs(i: int, j: int, k: int) -> bool:
            if k == 1:
                return s1[i] == s2[j]
            for h in range(1, k):
                if dfs(i, j, h) and dfs(i + h, j + h, k - h):
                    return True
                if dfs(i + h, j,k - h) and dfs(i, j + k - h, h):
                    return True
            return False
'''
我们设计一个函数 $dfs(i, j, k)$，表示字符串 $s_1$ 从 $i$ 开始长度为 $k$ 的子串是否能变换为字符串 $s_2$ 从 $j$ 开始长度为 $k$ 的子串。如果能变换，返回 `true`，否则返回 `false`。那么答案就是 $dfs(0, 0, n)$，其中 $n$ 是字符串的长度。

函数 $dfs(i, j, k)$ 的计算方式如下：

-   如果 $k=1$，那么只需要判断 $s_1[i]$ 和 $s_2[j]$ 是否相等，如果相等返回 `true`，否则返回 `false`；
-   如果 $k \gt 1$，我们枚举分割部分的长度 $h$，那么有两种情况：如果不交换分割的两个子字符串，那么就是 $dfs(i, j, h) \land dfs(i+h, j+h, k-h)$；如果交换了分割的两个子字符串，那么就是 $dfs(i, j+k-h, h) \land dfs(i+h, j, k-h)$。如果两种情况中有一种情况成立，那么就说明 $dfs(i, j, k)$ 成立，返回 `true`，否则返回 `false`。

最后，我们返回 $dfs(0, 0, n)$。

为了避免重复计算，我们可以使用记忆化搜索的方式。

时间复杂度 $O(n^4)$，空间复杂度 $O(n^3)$。其中 $n$ 是字符串的长度。
'''