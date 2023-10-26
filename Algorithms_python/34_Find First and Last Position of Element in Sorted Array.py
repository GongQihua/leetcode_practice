class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        l, right = left, len(nums) - 1
        while left < right:
            mid = (left + right + 1) >> 1
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        return [l, left]
'''
用两次二分查找寻找左边界和右边界
主意找到的最初边界要等于寻找数，而不是在一个范围内
'''