class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res
'''
算法思路：n不为全0时，n & (n - 1) 会消除 n 中最后一位中的 1
'''