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

我们定义二分查找的左边界 l=0，右边界 r=n-1，其中 n 为数组的长度。

每次在二分查找的过程中，我们会得到当前的中点 mid=(l+r)/2。

-   如果 nums[mid] > nums[r]，说明 [l,mid] 是有序的，此时如果 nums[l] <= target <= nums[mid]，说明 target 位于 [l,mid]，否则 target 位于 [mid+1,r]。
-   如果 nums[mid] < nums[r]，说明 [mid+1,r] 是有序的，此时如果 nums[mid] < target <= nums[r]，说明 target 位于 [mid+1,r]，否则 target 位于 [l,mid]。
-   如果 nums[mid] = nums[r]，说明元素 nums[mid] 和 nums[r] 相等，此时无法判断 target 位于哪个区间，我们只能将 r 减少 1。

二分查找结束后，如果 nums[l] = target，则说明数组中存在目标值 target，否则说明不存在。

时间复杂度近似 O(\log n)，空间复杂度 O(1)。其中 n 为数组的长度。
'''