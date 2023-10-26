class Solution: #动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        res = f = nums[0] #用f迭代数字相加之和，用res判断最大数
        for i in nums[1:]:
            f = i + max(f,0)
            res = max(res,f)
        return res