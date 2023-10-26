class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        sum, res = 0, n + 1
        while right < n:
            sum += nums[right]
            while sum >= target:
                res = min(res, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return 0 if res == n + 1 else res

'''
使用指针 left, right 分别表示子数组的开始位置和结束位置，维护变量 sum 表示子数组 nums[left...right] 元素之和。
初始时 left, right 均指向 0。每一次迭代，将 nums[right] 加到 sum，如果此时 sum >= target，更新最小长度即可。
然后将 sum 减去 nums[left]，接着 left 指针右移直至 sum < target。
每一次迭代最后，将 right 指针右移。这个方法的时间复杂度是O(n)
要时间复杂度O(nlogn)的话要用前缀加二分查找，解法用到了一堆函数，就不在这里展示了
'''