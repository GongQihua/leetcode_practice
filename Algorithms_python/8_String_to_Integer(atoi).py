class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        if n == 0:
            return 0
        while s[i] == ' ':
            i += 1
            if i == n:
                return 0
        if s[i] == '-':
            sign = -1
        else:
            sign = 1
        if s[i] in ['-', '+']:
            i += 1
        res = 0
        flag = (2 ** 31 - 1) // 10
        while i < n:
            if not s[i].isdigit():
                break
            c = int(s[i])
            if res > flag or (res == flag and c > 7):
                return 2 ** 31 - 1 if sign > 0 else -2 ** 31
            res = res * 10 + c
            i += 1
        return sign * res
'''
输入的顺序是固定的，必定是空格，符号，数字，再是迷惑的字母
所以按输入的顺序暴力检索，先查空格，再查符号存着，然后查数字
记得不能超过范围，空字符串，只有空格的字符串等等限制，对着test测就完了
用动态规划写，其实思路是一模一样的，时间空间复杂度也都是O(m,n).
'''