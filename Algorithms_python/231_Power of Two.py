class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
'''
这是除了挨个除2的方法外的简单做法，可将最后一个二进制形式n的最后一位1移除，若移除后为0，说明n是2的幂。
'''