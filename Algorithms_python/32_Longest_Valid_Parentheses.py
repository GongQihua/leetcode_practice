class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        f = [0] * (n + 1)
        for i, c in enumerate(s, 1):
            if c == ")":
                if i > 1 and s[i - 2] == "(":
                    f[i] = f[i - 2] + 2
                else:
                    j = i - f[i - 1] - 1
                    if j and s[j - 1] == "(":
                        f[i] = f[i - 1] + 2 + f[j - 1]
        return max(f)
'''
我们定义 $f[i]$ 表示以 $s[i-1]$ 结尾的最长有效括号的长度，那么答案就是 $\max\limits_{i=1}^n f[i]$。

-   如果 $s[i-1]$ 是左括号，那么以 $s[i-1]$ 结尾的最长有效括号的长度一定为 $0$，因此 $f[i] = 0$。
-   如果 $s[i-1]$ 是右括号，有以下两种情况：
    -   如果 $s[i-2]$ 是左括号，那么以 $s[i-1]$ 结尾的最长有效括号的长度为 $f[i-2] + 2$。
    -   如果 $s[i-2]$ 是右括号，那么以 $s[i-1]$ 结尾的最长有效括号的长度为 $f[i-1] + 2$，但是还需要考虑 $s[i-f[i-1]-2]$ 是否是左括号，如果是左括号，那么以 $s[i-1]$ 结尾的最长有效括号的长度为 $f[i-1] + 2 + f[i-f[i-1]-2]$。

'''