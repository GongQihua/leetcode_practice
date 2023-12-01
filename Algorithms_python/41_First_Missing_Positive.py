class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(i, nums[i] - 1)
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1
'''
我们可以遍历数组，将数组中的每个数x交换到它应该在的位置上，即x应该在的位置为 x-1。
如果 x不在[1, n+1]之间，那么我们就不用管它。
然后再遍历数组，按正整数顺序，找漏的那个数。
'''