class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = int((left + right)/2)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
        #因为复杂度要为O(log n)，所以不能遍历数组，只能二分查找
        #定义头、尾、中间数，然后开干