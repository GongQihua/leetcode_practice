class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for x in columnTitle:
            res = res * 26 + (ord(x) - ord('A') + 1)
        return res
'''
顺序读取columnTitle的字母，挨个累加
'''