class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, nums[0]
        for num in nums[1:]:
            a, b = b, max(num + a, b)
        return b

'''
其实最基本的思路就是比较第一位加第三位和第二位加第四位谁大，但写法要巧妙一点
这里用的是动态规划，算法核心就是 f(n) = Math.max(f(n - 2) + nums[n], nums[n - 1])
所以就有了题目中的 a, b = b, max(num + a, b)
'''