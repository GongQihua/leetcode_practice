class Solution:
    Symbol_Values = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.Symbol_Values[ch]
            if i < n -1 and value < Solution.Symbol_Values[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans
'''
创一个字典，解决遇到4，9的问题，方法就是,例如IV，先减I再加V
所以，逐字符录入没有问题，检查后一个是否大于前一个，大于前一个说明进4，9的特殊情况
'''