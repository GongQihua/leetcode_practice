class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

'''
别看题目写的花里胡哨，其实就是找那个移动的点，本来数组从小到达排序的，如果遇到了后一位比前一位小的
那就是找对了，具体方法就是二分查找
'''