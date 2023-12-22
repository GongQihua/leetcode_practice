class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        num = 1
        m1, m2 = 0, n-1
        while m1 < m2:
            for i in range(m1, m2):
                res[m1][i] = num
                num += 1
            for j in range(m1, m2):
                res[j][m2] = num
                num += 1
            for i in range(m2, m1, -1):
                res[m2][i] = num
                num += 1
            for j in range(m2, m1, -1):
                res[j][m1] = num
                num += 1
            m1 += 1
            m2 -= 1
        if m1 == m2:
            res[m1][m2] = num
        return res
'''
没有什么好解法，直接暴力循环，从外层向内层循环，注意好数组标识顺序就行，
别忘了最后一个中间数
这个写法很清楚，就没有做新版改进
'''