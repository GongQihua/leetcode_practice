'''
给你一个字符串 s ，如果可以将它分割成三个 非空 回文子字符串，那么返回 true ，否则返回 false 。
当一个字符串正着读和反着读是一模一样的，就称其为 回文字符串 。
'''
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]
        for length in range(1, n):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 1:
                    isPalindrome[start][end] = 1
                elif length == 2:
                    isPalindrome[start][end] = s[start] == s[end]
                else:
                    isPalindrome[start][end] = s[start] == s[end] and isPalindrome[start+1][end-1]
        for start in range(1, n-1):
            if not isPalindrome[0][start-1]:
                continue
            for end in range(start, n - 1):
                if isPalindrome[start][end] and isPalindrome[end+1][n-1]:
                    return True
        return False