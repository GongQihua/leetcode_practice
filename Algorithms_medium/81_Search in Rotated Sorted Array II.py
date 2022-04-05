class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r] or nums[mid] < nums[l]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[l] or nums[mid] > nums[r]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return False
'''
标准答案的二分查找
题目的意思是，原数组是一个升序，现在在一个点前后转了，要用复杂度小的办法
也就是在二分查找的过程中，怎样应对他这个前后转了的问题
代码如图所示，就是标准二分的写法但是要考虑在哪点转了，前后谁大的情况
垃圾题目，直接遍历不好么
'''