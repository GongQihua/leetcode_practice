class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res |= ((n & 1) << (31 - i))
            n >>= 1
        return res
'''
读取n第一个数，向右移31然后固定res，n向右移一格更新n数列
'''