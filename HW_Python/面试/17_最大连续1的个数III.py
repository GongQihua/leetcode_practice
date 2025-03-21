# 给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数 。
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = lsum = rsum = 0
        ans = 0
        for right in range(n):
            rsum += 1 - nums[right]
            while rsum - lsum > k:
                lsum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans