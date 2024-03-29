class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def twoSumClosest(nums, start, end, target):
            res = 0
            diff = 100000
            while start < end:
                val = nums[start] + nums[end]
                if val == target:
                    return val
                if abs(val - target) < diff:
                    res = val
                    diff = abs(val - target)
                if val < target:
                    start += 1
                else:
                    end -= 1
            return res

        nums.sort()
        res, n = 0, len(nums)
        diff = 100000
        for i in range(n - 2):
            t = twoSumClosest(nums, i + 1, n - 1, target - nums[i])
            if abs(nums[i] + t - target) < diff:
                res = nums[i] + t
                diff = abs(nums[i] + t - target)
        return res
'''
确定第一个开始的数，用target - 第一个数作为新target，来做two sum closest
再开始大循环，并于diff比较最后得出最小数
'''