class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
'''
解法一，遍历再比较，暴力求解
但要满足use only constant extra space，就要用解法二
解法二：异或，原理是两个相同的数异或之后的结果为 0
所以拿一个数于list里的数一一异或，单的那个数将被返回
'''