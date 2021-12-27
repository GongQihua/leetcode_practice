class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0:
            return ""
        if numRows == 1:
            return s
        List  = [ [] for i in range(numRows) ]
        i = 0
        while i < len(s):
            j = 0
            while i < len(s) and j < numRows:
                List[j].append(s[i])
                i += 1
                j += 1
            j -= 2
            while i < len(s) and j > 0:
                List[j].append(s[i])
                j -= 1
                i += 1
                
        return "".join(["".join(n) for n in List])
'''
按照题目要求打出一个数字表，然后返还数列数字，用join消除中间的空格
'''