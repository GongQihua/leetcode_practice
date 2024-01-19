class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        i = 0
        if s[i] in '+-':
            i += 1
        if i == n:
            return False
        if s[i] == '.' and (i + 1 == n or s[i+1] in "eE"):
            return False
        dot = e = 0
        j = i
        while j < n:
            if s[j] == '.':
                if e or dot:
                    return False
                dot += 1
            elif s[j] in 'eE':
                if e or j == i or j == n - 1:
                    return False
                e += 1
                if s[j + 1] in '+-':
                    j += 1
                    if j == n - 1:
                        return False
            elif not s[j].isnumeric():
                return False
            j += 1
        return True
'''
遍历数组，分情况讨论
首先，我们判断字符串是否以正负号开头，如果是，将指针i向后移动一位。如果此时指针i已经到达字符串末尾，说明字符串只有一个正负号，返回 false。
如果当前指针i指向的字符是小数点，并且小数点后面没有数字，或者小数点后是一个 e 或 E，返回 false。

接着，我们用两个变量dot和e分别记录小数点和 e 或 E 的个数。

用指针j指向当前字符：

如果当前字符是小数点，并且此前出现过小数点或者 e 或 E，返回 false。否则，我们将dot加一；
如果当前字符是 e 或 E，并且此前出现过 e 或 E，或者当前字符是开头或结尾，返回 false。否则，我们将e加一；然后判断下一个字符是否是正负号，如果是，将指针j向后移动一位。如果此时指针j已经到达字符串末尾，返回 false；
如果当前字符不是数字，返回 false。
遍历完字符串后，返回 true。
'''