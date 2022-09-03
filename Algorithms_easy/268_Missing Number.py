class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, v in enumerate(nums):
            res ^= i ^ v
        return res
'''
异或求解。两个相同的数异或的结果为 0。
也可以用数学求解。求出 [0..n] 的和，减去数组中所有数的和，就得到了缺失的数字。
'''