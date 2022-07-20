class Solution:
    def rob(self, nums: List[int]) -> int:
        def robrange(nums, l, r):
            a, b = 0, nums[l]
            for num in nums[l + 1: r + 1]:
                a, b = b, max(num + a, b)
            return b
        
        n = len(nums)
        if n == 1:
            return nums[0]
        s1, s2 = robrange(nums, 0, n - 2), robrange(nums, 1, n - 1)
        return max(s1, s2)

'''
这题的精髓在两个点，
第一，因为是环形，环状排列意味着第一个房屋和最后一个房屋中最多只能选择一个偷窃，因此可以把此环状排列房间问题约化为两个单排排列房屋子问题。
第二，就是“a, b = b, max(num + a, b)”这步，其实把数字带进去一看就知道了，效果就是1，3和2，4比，看谁大
'''