class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left = right = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        #print('ans = ',ans)
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        #print('ans = ',ans)
        return ans
'''
除了暴力方法外的一种简便方法，
就是另建一个数组，分别从左至右，从右至左累乘一次即可。
'''